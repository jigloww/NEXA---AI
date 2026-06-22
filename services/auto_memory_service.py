class AutoMemoryService:

    def __init__(self, memory):
        self.memory = memory

    def extract(self, user_message):

        user_lower = user_message.lower()

        # =================================
        # FAVORITE FRAMEWORK
        # =================================

        if "flutter" in user_lower:

            self.memory.save_memory(
                "favorite_framework",
                "Flutter"
            )

        # =================================
        # FAVORITE LANGUAGE
        # =================================

        if "python" in user_lower:

            self.memory.save_memory(
                "favorite_language",
                "Python"
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
                "Machine Learning"
            )

        if (
            "deep learning"
            in user_lower
        ):

            self.memory.save_memory(
                "current_learning",
                "Deep Learning"
            )