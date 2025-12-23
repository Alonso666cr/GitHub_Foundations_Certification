# database.py
import sqlite3
import pandas as pd

DB_NAME = "results.db"

def get_connection():
    return sqlite3.connect("results.db", check_same_thread=False)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            question_id INTEGER,
            concept TEXT,
            correct INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()

def save_attempt(user_id, question_id, concept, correct):
    conn = sqlite3.connect("results.db")
    conn.execute(
        "INSERT INTO attempts (user_id, question_id, concept, correct) VALUES (?, ?, ?, ?)",
        (user_id, question_id, concept, int(correct))
    )
    conn.commit()
    conn.close()

def load_stats():
    conn = get_connection()
    df = conn.execute("SELECT * FROM attempts").fetchall()
    conn.close()
    return df

def load_stats(user_id):
    conn = sqlite3.connect("results.db")
    df = pd.read_sql_query(
        "SELECT * FROM attempts WHERE user_id = ?",
        conn,
        params=(user_id,)
    )
    conn.close()
    return df
