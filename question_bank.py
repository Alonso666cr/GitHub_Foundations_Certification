# question_bank.py
# GitHub Foundations – Question Bank v2 (60 preguntas)

QUESTION_BANK = [

# ==================================================
# GIT BASICS (1–12)
# ==================================================

{
    "id": 1,
    "question": "¿Cuál es el propósito principal de Git?",
    "options": [
        "Alojar código en la nube",
        "Controlar versiones de archivos",
        "Ejecutar aplicaciones",
        "Gestionar usuarios"
    ],
    "answer": 1,
    "concept": "Git Basics",
    "explanation": "Git es un sistema de control de versiones distribuido."
},
{
    "id": 2,
    "question": "¿Qué comando inicializa un repositorio Git?",
    "options": ["git start", "git init", "git create", "git new"],
    "answer": 1,
    "concept": "Git Basics",
    "explanation": "git init crea un repositorio Git vacío."
},
{
    "id": 3,
    "question": "¿Qué comando muestra el estado actual del repositorio?",
    "options": ["git diff", "git log", "git status", "git show"],
    "answer": 2,
    "concept": "Git Basics",
    "explanation": "git status indica archivos modificados y preparados."
},
{
    "id": 4,
    "question": "¿Qué archivo define qué archivos debe ignorar Git?",
    "options": [".gitconfig", ".gitignore", ".ignore", ".exclude"],
    "answer": 1,
    "concept": "Git Basics",
    "explanation": ".gitignore evita versionar archivos no deseados."
},
{
    "id": 5,
    "question": "¿Qué área contiene los cambios listos para commit?",
    "options": ["Working directory", "Staging area", "Remote repo", "Branch"],
    "answer": 1,
    "concept": "Git Basics",
    "explanation": "La staging area prepara los cambios para confirmarlos."
},
{
    "id": 6,
    "question": "¿Qué comando agrega cambios al área de preparación?",
    "options": ["git commit", "git add", "git push", "git stage"],
    "answer": 1,
    "concept": "Git Basics",
    "explanation": "git add mueve archivos al staging area."
},
{
    "id": 7,
    "question": "¿Qué es un commit?",
    "options": [
        "Un repositorio remoto",
        "Un punto guardado del historial",
        "Una rama",
        "Un conflicto"
    ],
    "answer": 1,
    "concept": "Git Basics",
    "explanation": "Un commit registra un conjunto de cambios."
},
{
    "id": 8,
    "question": "¿Qué comando muestra el historial de commits?",
    "options": ["git status", "git history", "git log", "git commits"],
    "answer": 2,
    "concept": "Git Basics",
    "explanation": "git log muestra el historial del repositorio."
},
{
    "id": 9,
    "question": "¿Git es un sistema centralizado o distribuido?",
    "options": ["Centralizado", "Distribuido", "Híbrido", "Remoto"],
    "answer": 1,
    "concept": "Git Basics",
    "explanation": "Cada copia contiene todo el historial."
},
{
    "id": 10,
    "question": "¿Qué comando sube cambios a un repositorio remoto?",
    "options": ["git pull", "git fetch", "git push", "git sync"],
    "answer": 2,
    "concept": "Git Basics",
    "explanation": "git push envía commits al remoto."
},
{
    "id": 11,
    "question": "¿Qué comando descarga cambios del repositorio remoto?",
    "options": ["git push", "git pull", "git add", "git clone"],
    "answer": 1,
    "concept": "Git Basics",
    "explanation": "git pull trae y fusiona cambios remotos."
},
{
    "id": 12,
    "question": "¿Qué es HEAD en Git?",
    "options": [
        "La rama principal",
        "El último commit actual",
        "Un repositorio remoto",
        "Un conflicto"
    ],
    "answer": 1,
    "concept": "Git Basics",
    "explanation": "HEAD apunta al commit actual."
},

# ==================================================
# GITHUB BASICS (13–25)
# ==================================================

{
    "id": 13,
    "question": "¿Qué es GitHub?",
    "options": [
        "Un lenguaje de programación",
        "Un servicio de hosting para repositorios Git",
        "Un editor de texto",
        "Un sistema operativo"
    ],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "GitHub aloja repositorios Git."
},
{
    "id": 14,
    "question": "¿Cuál es la diferencia clave entre Git y GitHub?",
    "options": [
        "Git es local, GitHub es remoto",
        "GitHub reemplaza Git",
        "Git solo funciona online",
        "No hay diferencia"
    ],
    "answer": 0,
    "concept": "GitHub Basics",
    "explanation": "Git es la herramienta, GitHub la plataforma."
},
{
    "id": 15,
    "question": "¿Qué es un repositorio?",
    "options": [
        "Un usuario",
        "Un contenedor de código y su historial",
        "Un commit",
        "Una rama"
    ],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "Contiene código, historial y configuración."
},
{
    "id": 16,
    "question": "¿Qué es un fork?",
    "options": [
        "Una rama local",
        "Una copia de un repositorio",
        "Un commit especial",
        "Un pull request"
    ],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "Permite trabajar sin afectar el original."
},
{
    "id": 17,
    "question": "¿Para qué sirve clonar un repositorio?",
    "options": [
        "Eliminarlo",
        "Crear una copia local",
        "Cambiar permisos",
        "Crear un release"
    ],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "Clonar descarga el repositorio localmente."
},
{
    "id": 18,
    "question": "¿Qué es un pull request?",
    "options": [
        "Un commit",
        "Una propuesta de cambios",
        "Un fork",
        "Una rama"
    ],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "Permite revisión y discusión."
},
{
    "id": 19,
    "question": "¿Qué rama suele ser la principal?",
    "options": ["dev", "main/master", "feature", "test"],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "main es la rama principal por defecto."
},
{
    "id": 20,
    "question": "¿Dónde se gestionan los permisos del repositorio?",
    "options": ["Issues", "Actions", "Settings", "Commits"],
    "answer": 2,
    "concept": "GitHub Basics",
    "explanation": "Los permisos se configuran en Settings."
},
{
    "id": 21,
    "question": "¿Qué es un release?",
    "options": [
        "Un commit",
        "Una versión publicada",
        "Un fork",
        "Un issue"
    ],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "Los releases representan versiones estables."
},
{
    "id": 22,
    "question": "¿Qué archivo describe el proyecto?",
    "options": ["LICENSE", "README.md", ".gitignore", "CONTRIBUTING.md"],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "README explica el propósito del proyecto."
},
{
    "id": 23,
    "question": "¿Qué es GitHub CLI?",
    "options": [
        "Una interfaz gráfica",
        "Una herramienta de línea de comandos",
        "Un lenguaje",
        "Un runner"
    ],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "Permite interactuar con GitHub desde terminal."
},
{
    "id": 24,
    "question": "¿Qué significa que un repositorio sea público?",
    "options": [
        "Solo accesible por admins",
        "Visible para cualquiera",
        "Editable por cualquiera",
        "Privado por defecto"
    ],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "Cualquiera puede ver un repo público."
},
{
    "id": 25,
    "question": "¿Qué ventaja ofrece un repositorio privado?",
    "options": [
        "Más velocidad",
        "Control de acceso",
        "Más forks",
        "Más issues"
    ],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "Permite limitar quién accede."
},

# ==================================================
# COLLABORATION & ISSUES (26–42)
# ==================================================

{
    "id": 26,
    "question": "¿Para qué se usan las ramas?",
    "options": [
        "Eliminar código",
        "Trabajar en paralelo",
        "Reducir commits",
        "Aumentar seguridad"
    ],
    "answer": 1,
    "concept": "Collaboration",
    "explanation": "Permiten desarrollo independiente."
},
{
    "id": 27,
    "question": "¿Qué es un merge?",
    "options": [
        "Eliminar ramas",
        "Combinar cambios",
        "Crear commits",
        "Cerrar issues"
    ],
    "answer": 1,
    "concept": "Collaboration",
    "explanation": "Integra cambios entre ramas."
},
{
    "id": 28,
    "question": "¿Qué archivo define reglas de contribución?",
    "options": ["README.md", "LICENSE", "CONTRIBUTING.md", "CODEOWNERS"],
    "answer": 2,
    "concept": "Collaboration",
    "explanation": "Define cómo contribuir."
},
{
    "id": 29,
    "question": "¿Qué es un conflicto de merge?",
    "options": [
        "Error de red",
        "Cambios incompatibles",
        "Un commit fallido",
        "Un issue abierto"
    ],
    "answer": 1,
    "concept": "Collaboration",
    "explanation": "Git no puede fusionar automáticamente."
},
{
    "id": 30,
    "question": "¿Para qué sirve CODEOWNERS?",
    "options": [
        "Definir responsables de código",
        "Crear forks",
        "Ejecutar workflows",
        "Asignar issues"
    ],
    "answer": 0,
    "concept": "Collaboration",
    "explanation": "Asigna revisores automáticamente."
},
{
    "id": 31,
    "question": "¿Para qué sirven los code reviews?",
    "options": [
        "Eliminar PRs",
        "Mejorar calidad",
        "Cerrar repositorios",
        "Reducir ramas"
    ],
    "answer": 1,
    "concept": "Collaboration",
    "explanation": "Detectan errores y mejoran calidad."
},
{
    "id": 32,
    "question": "¿Qué es un Issue?",
    "options": [
        "Un error del sistema",
        "Una tarea o bug",
        "Un commit",
        "Una rama"
    ],
    "answer": 1,
    "concept": "Issues",
    "explanation": "Sirve para seguimiento del trabajo."
},
{
    "id": 33,
    "question": "¿Qué es un label?",
    "options": [
        "Comentario",
        "Etiqueta de clasificación",
        "Permiso",
        "Commit"
    ],
    "answer": 1,
    "concept": "Issues",
    "explanation": "Organiza issues y PRs."
},
{
    "id": 34,
    "question": "¿Qué es un milestone?",
    "options": [
        "Un commit",
        "Un objetivo con fecha",
        "Una rama",
        "Un fork"
    ],
    "answer": 1,
    "concept": "Issues",
    "explanation": "Agrupa trabajo por objetivos."
},
{
    "id": 35,
    "question": "¿Para qué sirven GitHub Projects?",
    "options": [
        "Alojar código",
        "Gestionar trabajo",
        "Ejecutar Actions",
        "Crear forks"
    ],
    "answer": 1,
    "concept": "Projects",
    "explanation": "Ayudan a organizar tareas."
},
{
    "id": 36,
    "question": "¿Qué vista ofrecen Projects?",
    "options": [
        "Solo lista",
        "Kanban, tabla y timeline",
        "Solo calendario",
        "Solo gráfico"
    ],
    "answer": 1,
    "concept": "Projects",
    "explanation": "Permite distintas vistas."
},
{
    "id": 37,
    "question": "¿Qué es un draft pull request?",
    "options": [
        "PR cerrado",
        "PR en borrador",
        "PR fusionado",
        "PR rechazado"
    ],
    "answer": 1,
    "concept": "Collaboration",
    "explanation": "Indica que no está listo para revisión."
},
{
    "id": 38,
    "question": "¿Quién puede cerrar un issue?",
    "options": [
        "Solo el creador",
        "Colaboradores con permiso",
        "Cualquiera",
        "Solo GitHub"
    ],
    "answer": 1,
    "concept": "Issues",
    "explanation": "Depende de los permisos."
},
{
    "id": 39,
    "question": "¿Qué ventaja tiene vincular PRs con issues?",
    "options": [
        "Cerrar repositorios",
        "Trazabilidad",
        "Reducir commits",
        "Eliminar ramas"
    ],
    "answer": 1,
    "concept": "Collaboration",
    "explanation": "Facilita seguimiento del trabajo."
},
{
    "id": 40,
    "question": "¿Qué significa cerrar un issue automáticamente?",
    "options": [
        "Borrarlo",
        "Cerrarlo al fusionar un PR",
        "Eliminar el repo",
        "Archivar el proyecto"
    ],
    "answer": 1,
    "concept": "Issues",
    "explanation": "Se cierra al completar el trabajo."
},
{
    "id": 41,
    "question": "¿Qué es una plantilla de issue?",
    "options": [
        "Un bot",
        "Un formulario predefinido",
        "Un permiso",
        "Un commit"
    ],
    "answer": 1,
    "concept": "Issues",
    "explanation": "Estandariza la creación de issues."
},
{
    "id": 42,
    "question": "¿Para qué sirven los discussions?",
    "options": [
        "Ejecutar código",
        "Conversaciones comunitarias",
        "Crear forks",
        "Cerrar issues"
    ],
    "answer": 1,
    "concept": "Community",
    "explanation": "Fomentan interacción comunitaria."
},

# ==================================================
# ACTIONS, SECURITY & COMMUNITY (43–60)
# ==================================================

{
    "id": 43,
    "question": "¿Qué es GitHub Actions?",
    "options": [
        "Un lenguaje",
        "Un sistema de automatización",
        "Un repositorio",
        "Un editor"
    ],
    "answer": 1,
    "concept": "GitHub Actions",
    "explanation": "Automatiza flujos de trabajo."
},
{
    "id": 44,
    "question": "¿Dónde se definen los workflows?",
    "options": [
        ".github/workflows",
        "/actions",
        "/ci",
        "/pipelines"
    ],
    "answer": 0,
    "concept": "GitHub Actions",
    "explanation": "Se definen en archivos YAML."
},
{
    "id": 45,
    "question": "¿Qué es un runner?",
    "options": [
        "Un ejecutor de workflows",
        "Un usuario",
        "Un commit",
        "Un repo"
    ],
    "answer": 0,
    "concept": "GitHub Actions",
    "explanation": "Ejecuta los jobs."
},
{
    "id": 46,
    "question": "¿Qué tipo de runner ofrece GitHub?",
    "options": [
        "Solo self-hosted",
        "Hosted y self-hosted",
        "Solo local",
        "Solo cloud privado"
    ],
    "answer": 1,
    "concept": "GitHub Actions",
    "explanation": "GitHub ofrece ambos tipos."
},
{
    "id": 47,
    "question": "¿Qué es Dependabot?",
    "options": [
        "Un bot de dependencias",
        "Un runner",
        "Un lenguaje",
        "Un usuario"
    ],
    "answer": 0,
    "concept": "Security",
    "explanation": "Mantiene dependencias actualizadas."
},
{
    "id": 48,
    "question": "¿Qué analiza GitHub Advanced Security?",
    "options": [
        "Usuarios",
        "Commits",
        "Vulnerabilidades y secretos",
        "Ramas"
    ],
    "answer": 2,
    "concept": "Security",
    "explanation": "Detecta riesgos en el código."
},
{
    "id": 49,
    "question": "¿Qué es secret scanning?",
    "options": [
        "Buscar passwords",
        "Detectar secretos expuestos",
        "Eliminar commits",
        "Escanear issues"
    ],
    "answer": 1,
    "concept": "Security",
    "explanation": "Evita filtración de secretos."
},
{
    "id": 50,
    "question": "¿Para qué sirve CodeQL?",
    "options": [
        "Analizar código",
        "Ejecutar workflows",
        "Crear forks",
        "Gestionar usuarios"
    ],
    "answer": 0,
    "concept": "Security",
    "explanation": "Detecta vulnerabilidades."
},
{
    "id": 51,
    "question": "¿Para qué sirve una licencia?",
    "options": [
        "Ejecutar código",
        "Definir uso legal",
        "Crear forks",
        "Ejecutar Actions"
    ],
    "answer": 1,
    "concept": "Licensing",
    "explanation": "Define derechos del software."
},
{
    "id": 52,
    "question": "¿Cuál es una licencia permisiva?",
    "options": ["GPL", "MIT", "AGPL", "LGPL"],
    "answer": 1,
    "concept": "Licensing",
    "explanation": "MIT es permisiva."
},
{
    "id": 53,
    "question": "¿Qué es un Code of Conduct?",
    "options": [
        "Un contrato",
        "Normas de comportamiento",
        "Una licencia",
        "Un workflow"
    ],
    "answer": 1,
    "concept": "Community",
    "explanation": "Define normas comunitarias."
},
{
    "id": 54,
    "question": "¿Por qué es importante documentar un proyecto?",
    "options": [
        "Reducir forks",
        "Facilitar uso y contribución",
        "Aumentar commits",
        "Eliminar issues"
    ],
    "answer": 1,
    "concept": "Community",
    "explanation": "Mejora adopción y colaboración."
},
{
    "id": 55,
    "question": "¿Qué es GitHub Discussions?",
    "options": [
        "Un sistema de chat",
        "Un foro de la comunidad",
        "Un runner",
        "Un workflow"
    ],
    "answer": 1,
    "concept": "Community",
    "explanation": "Permite debates abiertos."
},
{
    "id": 56,
    "question": "¿Qué beneficio ofrece la automatización?",
    "options": [
        "Menos control",
        "Mayor consistencia",
        "Más errores",
        "Más trabajo manual"
    ],
    "answer": 1,
    "concept": "GitHub Actions",
    "explanation": "Reduce errores humanos."
},
{
    "id": 57,
    "question": "¿Qué evento puede disparar un workflow?",
    "options": [
        "Push",
        "Pull request",
        "Schedule",
        "Todos los anteriores"
    ],
    "answer": 3,
    "concept": "GitHub Actions",
    "explanation": "Actions soporta múltiples triggers."
},
{
    "id": 58,
    "question": "¿Qué es un workflow reutilizable?",
    "options": [
        "Un template",
        "Un workflow llamado por otro",
        "Un fork",
        "Un runner"
    ],
    "answer": 1,
    "concept": "GitHub Actions",
    "explanation": "Permite reutilización."
},
{
    "id": 59,
    "question": "¿Qué ventaja tiene una comunidad activa?",
    "options": [
        "Menos forks",
        "Mejor soporte y evolución",
        "Menos commits",
        "Más conflictos"
    ],
    "answer": 1,
    "concept": "Community",
    "explanation": "Acelera mejoras y adopción."
},
{
    "id": 60,
    "question": "¿Cuál es el objetivo principal de GitHub?",
    "options": [
        "Ejecutar código",
        "Facilitar colaboración en software",
        "Eliminar bugs",
        "Reemplazar Git"
    ],
    "answer": 1,
    "concept": "GitHub Basics",
    "explanation": "GitHub se centra en colaboración."
},

# ==================================================
# ADVANCED USAGE, BEST PRACTICES & GOVERNANCE (61–80)
# ==================================================

{
    "id": 61,
    "question": "¿Qué es un protected branch?",
    "options": [
        "Una rama eliminada",
        "Una rama con reglas de protección",
        "Una rama privada",
        "Una rama local"
    ],
    "answer": 1,
    "concept": "Governance",
    "explanation": "Evita cambios directos sin revisión."
},
{
    "id": 62,
    "question": "¿Qué acción puede impedir un protected branch?",
    "options": [
        "Clonar repositorios",
        "Hacer push directo",
        "Crear forks",
        "Abrir issues"
    ],
    "answer": 1,
    "concept": "Governance",
    "explanation": "Requiere PRs aprobados."
},
{
    "id": 63,
    "question": "¿Para qué sirve un required review?",
    "options": [
        "Eliminar PRs",
        "Forzar revisión antes del merge",
        "Cerrar issues",
        "Crear commits automáticos"
    ],
    "answer": 1,
    "concept": "Governance",
    "explanation": "Mejora calidad y control."
},
{
    "id": 64,
    "question": "¿Qué es un status check requerido?",
    "options": [
        "Un permiso de usuario",
        "Un workflow que debe pasar",
        "Un comentario",
        "Un label"
    ],
    "answer": 1,
    "concept": "Governance",
    "explanation": "Impide merge si falla."
},
{
    "id": 65,
    "question": "¿Qué es una organización en GitHub?",
    "options": [
        "Un repositorio",
        "Un grupo de usuarios y repositorios",
        "Un fork",
        "Un commit"
    ],
    "answer": 1,
    "concept": "Organizations",
    "explanation": "Facilita gestión a gran escala."
},
{
    "id": 66,
    "question": "¿Qué rol tiene permisos administrativos completos?",
    "options": ["Read", "Triage", "Write", "Admin"],
    "answer": 3,
    "concept": "Organizations",
    "explanation": "Admin controla configuración y acceso."
},
{
    "id": 67,
    "question": "¿Para qué sirven los teams en una organización?",
    "options": [
        "Ejecutar workflows",
        "Gestionar permisos por grupo",
        "Crear forks",
        "Eliminar issues"
    ],
    "answer": 1,
    "concept": "Organizations",
    "explanation": "Simplifican la administración."
},
{
    "id": 68,
    "question": "¿Qué es GitHub Pages?",
    "options": [
        "Un gestor de repositorios",
        "Un servicio de hosting estático",
        "Un runner",
        "Un sistema de CI"
    ],
    "answer": 1,
    "concept": "GitHub Pages",
    "explanation": "Permite publicar sitios web."
},
{
    "id": 69,
    "question": "¿Desde dónde puede publicarse GitHub Pages?",
    "options": [
        "Issues",
        "Actions",
        "Una rama o carpeta",
        "Releases"
    ],
    "answer": 2,
    "concept": "GitHub Pages",
    "explanation": "Usualmente desde main o docs."
},
{
    "id": 70,
    "question": "¿Qué es un environment en GitHub Actions?",
    "options": [
        "Un lenguaje",
        "Un contexto con reglas y secretos",
        "Un runner",
        "Un repositorio"
    ],
    "answer": 1,
    "concept": "GitHub Actions",
    "explanation": "Controla despliegues."
},
{
    "id": 71,
    "question": "¿Para qué sirven los secrets?",
    "options": [
        "Guardar contraseñas de forma segura",
        "Crear issues",
        "Definir licencias",
        "Ejecutar workflows"
    ],
    "answer": 0,
    "concept": "Security",
    "explanation": "Protegen información sensible."
},
{
    "id": 72,
    "question": "¿Qué diferencia hay entre secrets y variables?",
    "options": [
        "No hay diferencia",
        "Los secrets están cifrados",
        "Las variables son privadas",
        "Los secrets son públicos"
    ],
    "answer": 1,
    "concept": "Security",
    "explanation": "Secrets nunca se muestran."
},
{
    "id": 73,
    "question": "¿Qué es una plantilla de repositorio?",
    "options": [
        "Un fork",
        "Un repositorio base reutilizable",
        "Un workflow",
        "Un runner"
    ],
    "answer": 1,
    "concept": "Best Practices",
    "explanation": "Estandariza proyectos."
},
{
    "id": 74,
    "question": "¿Qué ventaja ofrece una buena convención de commits?",
    "options": [
        "Más commits",
        "Historial claro",
        "Menos ramas",
        "Menos issues"
    ],
    "answer": 1,
    "concept": "Best Practices",
    "explanation": "Facilita mantenimiento."
},
{
    "id": 75,
    "question": "¿Qué es Semantic Versioning?",
    "options": [
        "Un sistema de licencias",
        "Un esquema de versiones",
        "Un workflow",
        "Un commit especial"
    ],
    "answer": 1,
    "concept": "Releases",
    "explanation": "Usa MAJOR.MINOR.PATCH."
},
{
    "id": 76,
    "question": "¿Cuándo se incrementa la versión MAJOR?",
    "options": [
        "Correcciones menores",
        "Cambios incompatibles",
        "Nueva documentación",
        "Refactor interno"
    ],
    "answer": 1,
    "concept": "Releases",
    "explanation": "Rompe compatibilidad."
},
{
    "id": 77,
    "question": "¿Para qué sirve el archivo SECURITY.md?",
    "options": [
        "Definir licencias",
        "Reportar vulnerabilidades",
        "Ejecutar análisis",
        "Crear secrets"
    ],
    "answer": 1,
    "concept": "Security",
    "explanation": "Guía reportes responsables."
},
{
    "id": 78,
    "question": "¿Qué es un audit log?",
    "options": [
        "Un historial de commits",
        "Un registro de eventos de seguridad",
        "Un workflow",
        "Un issue"
    ],
    "answer": 1,
    "concept": "Security",
    "explanation": "Permite auditoría."
},
{
    "id": 79,
    "question": "¿Qué beneficio tiene automatizar releases?",
    "options": [
        "Más errores",
        "Consistencia y rapidez",
        "Menos control",
        "Menos versiones"
    ],
    "answer": 1,
    "concept": "Releases",
    "explanation": "Reduce errores manuales."
},
{
    "id": 80,
    "question": "¿Cuál es una buena práctica clave en GitHub?",
    "options": [
        "Trabajar directamente en main",
        "Usar PRs y revisiones",
        "Evitar documentación",
        "Eliminar issues cerrados"
    ],
    "answer": 1,
    "concept": "Best Practices",
    "explanation": "Mejora calidad y colaboración."
}

]

#print("Preguntas cargadas:", len(QUESTION_BANK))


# Validación
# assert len(QUESTION_BANK) == 60
