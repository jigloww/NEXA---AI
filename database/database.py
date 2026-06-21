import sqlite3

DATABASE_NAME = "nexa.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    # Short-Term Memory
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    # Long-Term Memory
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_memory (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()