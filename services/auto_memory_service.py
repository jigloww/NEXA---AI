class AutoMemoryService:

    def __init__(self, memory):
        self.memory = memory

    def extract(
        self,
        user_message,
        user_id=None,
        chat_id=None
    ):

        user_lower = user_message.lower()

        # =================================
        # FAVORITE FRAMEWORK
        # =================================

        if "flutter" in user_lower:

            self.memory.save_memory(
                "favorite_framework",
                "Flutter",
                user_id=user_id,
                chat_id=chat_id
            )

        # =================================
        # FAVORITE LANGUAGE
        # =================================

        if "python" in user_lower:

            self.memory.save_memory(
                "favorite_language",
                "Python",
                user_id=user_id,
                chat_id=chat_id
            )

        # =================================
        # CURRENT LEARNING
        # =================================

        if (
            "machine learning"
            in user_lower
        ):

            self.memory.save_memory(
                "current_learning",
                "Machine Learning",
                user_id=user_id,
                chat_id=chat_id
            )

        if (
            "deep learning"
            in user_lower
        ):

            self.memory.save_memory(
                "current_learning",
                "Deep Learning",
                user_id=user_id,
                chat_id=chat_id
            )
