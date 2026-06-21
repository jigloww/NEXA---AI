from database.database import (
    get_connection,
    initialize_database
)


class MemoryService:

    def __init__(self):

        initialize_database()

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