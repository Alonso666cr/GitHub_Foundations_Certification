import streamlit as st
import uuid
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

from question_bank import QUESTION_BANK
from database import save_attempt, load_stats, init_db

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

st.set_page_config(
    page_title="GitHub Foundations Trainer",
    layout="centered"
)

init_db()

EXAM_DURATION = 75 * 60  # 75 minutos

# --------------------------------------------------
# USER ID (NIVEL 1)
# --------------------------------------------------

if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# --------------------------------------------------
# ESTADO GLOBAL
# --------------------------------------------------

defaults = {
    "questions": [],
    "current_index": 0,
    "exam_started": False,
    "answered": False,
    "last_result": None,
    "exam_mode": False,
    "exam_start_time": None,
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("⚙️ Configuración")

num_questions = st.sidebar.selectbox(
    "Número de preguntas",
    options=[20, 40, 60, 80],
    index=3
)

st.session_state.exam_mode = st.sidebar.toggle(
    "Modo examen cronometrado",
    value=False,
    help="80 preguntas · 75 minutos · sin feedback inmediato"
)

if st.sidebar.button("🔄 Reiniciar"):
    for k in defaults:
        st.session_state[k] = defaults[k]
    st.rerun()

# --------------------------------------------------
# UI PRINCIPAL
# --------------------------------------------------

st.title("🎓 GitHub Foundations – Entrenamiento")

# ---------------- INICIO ---------------------------

if not st.session_state.exam_started:

    st.write(
        "Entrenamiento interactivo para la certificación **GitHub Foundations**.\n\n"
        "- Entrenamiento: feedback inmediato\n"
        "- Examen: sin feedback, cronometrado\n"
    )

    if st.button("▶️ Comenzar"):
        total = 80 if st.session_state.exam_mode else num_questions

        st.session_state.questions = random.sample(
            QUESTION_BANK,
            k=min(total, len(QUESTION_BANK))
        )

        st.session_state.current_index = 0
        st.session_state.exam_started = True
        st.session_state.answered = False
        st.session_state.last_result = None

        if st.session_state.exam_mode:
            st.session_state.exam_start_time = time.time()
        else:
            st.session_state.exam_start_time = None

        st.rerun()

# ---------------- EXAMEN / ENTRENAMIENTO -----------

else:
    idx = st.session_state.current_index
    total = len(st.session_state.questions)

    # ⏱️ TIMER
    if st.session_state.exam_mode:
        elapsed = time.time() - st.session_state.exam_start_time
        remaining = max(0, EXAM_DURATION - elapsed)

        mins, secs = divmod(int(remaining), 60)
        st.warning(f"⏱️ Tiempo restante: {mins:02d}:{secs:02d}")

        if remaining <= 0:
            st.session_state.current_index = total
            st.rerun()

    # FIN
    if idx >= total:
        st.success("🏁 Finalizado")

        stats = load_stats(st.session_state.user_id)
        exam_stats = stats.tail(total)

        score = exam_stats["correct"].mean()
        st.metric("Resultado final", f"{score:.0%}")

        if st.session_state.exam_mode:
            if score >= 0.8:
                st.success("🎉 APROBADO")
            else:
                st.error("❌ NO APROBADO")

        st.stop()

    # PREGUNTA
    q = st.session_state.questions[idx]

    st.progress((idx + 1) / total)
    st.caption(f"Pregunta {idx + 1} de {total}")

    selected = st.radio(
        q["question"],
        q["options"],
        key=f"q_{q['id']}"
    )

    # RESPONDER
    if not st.session_state.answered:
        if st.button("Responder"):
            is_correct = (
                q["options"].index(selected) == q["answer"]
            )

            save_attempt(
                st.session_state.user_id,
                q["id"],
                q["concept"],
                is_correct
            )

            if st.session_state.exam_mode:
                st.session_state.current_index += 1
            else:
                st.session_state.last_result = is_correct
                st.session_state.answered = True

            st.rerun()

    # FEEDBACK (solo entrenamiento)
    else:
        if st.session_state.last_result:
            st.success("✅ Respuesta correcta")
        else:
            st.error("❌ Respuesta incorrecta")
            st.info(f"Respuesta correcta: **{q['options'][q['answer']]}**")

        if st.button("➡️ Siguiente"):
            st.session_state.current_index += 1
            st.session_state.answered = False
            st.session_state.last_result = None
            st.rerun()

# --------------------------------------------------
# MÉTRICAS (SIEMPRE FILTRADAS POR USUARIO)
# --------------------------------------------------

st.divider()
st.subheader("📊 Tu progreso")

stats = load_stats(st.session_state.user_id)

if not stats.empty:
    st.metric("Precisión histórica", f"{stats['correct'].mean():.0%}")

    errors = stats[stats["correct"] == 0]
    if not errors.empty:
        fig, ax = plt.subplots()
        errors.groupby("concept").size().plot(kind="bar", ax=ax)
        ax.set_ylabel("Errores")
        st.pyplot(fig)
else:
    st.info("Aún no hay datos suficientes.")
