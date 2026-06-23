import sqlite3

DATABASE_NAME = "nexa.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def _table_columns(cursor, table_name):

    cursor.execute(
        f"PRAGMA table_info({table_name})"
    )

    return {
        row[1]
        for row in cursor.fetchall()
    }


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    # Legacy tables kept for backward compatibility.
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

    # Multi-user short-term conversation history.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            chat_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    # Multi-user long-term profile memory.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            chat_id TEXT NOT NULL,
            key TEXT NOT NULL,
            value TEXT NOT NULL,
            created_at TEXT NOT NULL,
            UNIQUE(user_id, chat_id, key)
        )
    """)

    legacy_memory_columns = _table_columns(
        cursor,
        "memories"
    )
    if {
        "user_id",
        "chat_id"
    }.issubset(legacy_memory_columns):
        cursor.execute("""
            INSERT INTO conversation_messages (
                user_id,
                chat_id,
                role,
                content,
                created_at
            )
            SELECT
                user_id,
                chat_id,
                role,
                content,
                COALESCE(created_at, CURRENT_TIMESTAMP)
            FROM memories
            WHERE NOT EXISTS (
                SELECT 1
                FROM conversation_messages
            )
        """)
    else:
        cursor.execute("""
            INSERT INTO conversation_messages (
                user_id,
                chat_id,
                role,
                content,
                created_at
            )
            SELECT
                'local_cli',
                'local_cli',
                role,
                content,
                CURRENT_TIMESTAMP
            FROM memories
            WHERE NOT EXISTS (
                SELECT 1
                FROM conversation_messages
            )
        """)

    legacy_profile_columns = _table_columns(
        cursor,
        "user_memory"
    )
    if {
        "user_id",
        "chat_id"
    }.issubset(legacy_profile_columns):
        cursor.execute("""
            INSERT INTO user_memories (
                user_id,
                chat_id,
                key,
                value,
                created_at
            )
            SELECT
                user_id,
                chat_id,
                key,
                value,
                COALESCE(created_at, CURRENT_TIMESTAMP)
            FROM user_memory
            WHERE NOT EXISTS (
                SELECT 1
                FROM user_memories
            )
        """)
    else:
        cursor.execute("""
            INSERT INTO user_memories (
                user_id,
                chat_id,
                key,
                value,
                created_at
            )
            SELECT
                'local_cli',
                'local_cli',
                key,
                value,
                CURRENT_TIMESTAMP
            FROM user_memory
            WHERE NOT EXISTS (
                SELECT 1
                FROM user_memories
            )
        """)

    conn.commit()
    conn.close()
