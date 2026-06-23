from database.database import (
    get_connection,
    initialize_database
)


class MemoryService:

    def __init__(self):

        initialize_database()

    def _normalize_scope(
        self,
        user_id=None,
        chat_id=None
    ):

        scoped_user_id = str(
            user_id or "local_cli"
        )
        scoped_chat_id = str(
            chat_id or scoped_user_id
        )

        return (
            scoped_user_id,
            scoped_chat_id
        )

    # ==========================
    # SHORT TERM MEMORY
    # ==========================

    def add_message(
        self,
        role,
        content,
        user_id=None,
        chat_id=None
    ):

        scoped_user_id, scoped_chat_id = (
            self._normalize_scope(
                user_id,
                chat_id
            )
        )
        conn = get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO conversation_messages (
                    user_id,
                    chat_id,
                    role,
                    content,
                    created_at
                )
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
                """,
                (
                    scoped_user_id,
                    scoped_chat_id,
                    role,
                    content
                )
            )

            conn.commit()
        finally:
            conn.close()

    def get_context(
        self,
        user_id=None,
        chat_id=None,
        limit=20
    ):

        scoped_user_id, scoped_chat_id = (
            self._normalize_scope(
                user_id,
                chat_id
            )
        )
        conn = get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT role, content
                FROM (
                    SELECT role, content, id
                    FROM conversation_messages
                    WHERE user_id = ?
                    AND chat_id = ?
                    ORDER BY id DESC
                    LIMIT ?
                ) recent_messages
                ORDER BY id ASC
                """,
                (
                    scoped_user_id,
                    scoped_chat_id,
                    limit
                )
            )

            rows = cursor.fetchall()
        finally:
            conn.close()

        context = ""

        for role, content in rows:

            context += (
                f"{role}: "
                f"{content}\n"
            )

        return context

    def clear(
        self,
        user_id=None,
        chat_id=None
    ):

        scoped_user_id, scoped_chat_id = (
            self._normalize_scope(
                user_id,
                chat_id
            )
        )
        conn = get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM conversation_messages
                WHERE user_id = ?
                AND chat_id = ?
                """,
                (
                    scoped_user_id,
                    scoped_chat_id
                )
            )

            conn.commit()
        finally:
            conn.close()

    # ==========================
    # LONG TERM MEMORY
    # ==========================

    def save_memory(
        self,
        key,
        value,
        user_id=None,
        chat_id=None
    ):

        scoped_user_id, scoped_chat_id = (
            self._normalize_scope(
                user_id,
                chat_id
            )
        )
        conn = get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO user_memories (
                    user_id,
                    chat_id,
                    key,
                    value,
                    created_at
                )
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(user_id, chat_id, key)
                DO UPDATE SET
                    value = excluded.value,
                    created_at = CURRENT_TIMESTAMP
                """,
                (
                    scoped_user_id,
                    scoped_chat_id,
                    key,
                    value
                )
            )

            conn.commit()
        finally:
            conn.close()

    def get_memory(
        self,
        key,
        user_id=None,
        chat_id=None
    ):

        scoped_user_id, scoped_chat_id = (
            self._normalize_scope(
                user_id,
                chat_id
            )
        )
        conn = get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT value
                FROM user_memories
                WHERE user_id = ?
                AND chat_id = ?
                AND key = ?
                """,
                (
                    scoped_user_id,
                    scoped_chat_id,
                    key
                )
            )

            row = cursor.fetchone()
        finally:
            conn.close()

        if row:
            return row[0]

        return None

    def get_all_memories(
        self,
        user_id=None,
        chat_id=None
    ):

        scoped_user_id, scoped_chat_id = (
            self._normalize_scope(
                user_id,
                chat_id
            )
        )
        conn = get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT key, value
                FROM user_memories
                WHERE user_id = ?
                AND chat_id = ?
                ORDER BY key ASC
                """,
                (
                    scoped_user_id,
                    scoped_chat_id
                )
            )

            rows = cursor.fetchall()
        finally:
            conn.close()

        return rows
