from database.database import (
    get_connection,
    initialize_database
)


class MemoryService:

    def __init__(self):

        initialize_database()

    # ==========================
    # SHORT TERM MEMORY
    # ==========================

    def add_message(
        self,
        role,
        content
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO memories (
                role,
                content
            )
            VALUES (?, ?)
            """,
            (role, content)
        )

        conn.commit()
        conn.close()

    def get_context(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT role, content
            FROM memories
            ORDER BY id ASC
        """)

        rows = cursor.fetchall()

        conn.close()

        context = ""

        for role, content in rows:

            context += (
                f"{role}: "
                f"{content}\n"
            )

        return context

    def clear(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM memories"
        )

        conn.commit()
        conn.close()

    # ==========================
    # LONG TERM MEMORY
    # ==========================

    def save_memory(
        self,
        key,
        value
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO user_memory
            (
                key,
                value
            )
            VALUES (?, ?)
            """,
            (key, value)
        )

        conn.commit()
        conn.close()

    def get_memory(
        self,
        key
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT value
            FROM user_memory
            WHERE key = ?
            """,
            (key,)
        )

        row = cursor.fetchone()

        conn.close()

        if row:
            return row[0]

        return None

    def get_all_memories(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT key, value
            FROM user_memory
            """
        )

        rows = cursor.fetchall()

        conn.close()

        return rows