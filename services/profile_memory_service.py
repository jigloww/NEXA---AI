class ProfileMemoryService:

    def __init__(self, memory):

        self.memory = memory

    def handle(
        self,
        user_message,
        user_id=None,
        chat_id=None
    ):

        user_lower = user_message.lower().strip()

        # ==========================
        # USER NAME
        # ==========================

        if user_lower.startswith(
            "nama saya "
        ):

            name = user_message[
                len("nama saya "):
            ].strip()

            self.memory.save_memory(
                "user_name",
                name,
                user_id=user_id,
                chat_id=chat_id
            )

            return (
                f"Baik, saya akan mengingat bahwa nama Anda {name}."
            )

        if (
            "siapa nama saya"
            in user_lower
        ):

            name = self.memory.get_memory(
                "user_name",
                user_id=user_id,
                chat_id=chat_id
            )

            if name:

                return (
                    f"Nama Anda adalah {name}."
                )

            return (
                "Saya belum mengetahui nama Anda."
            )

        # ==========================
        # CURRENT PROJECT
        # ==========================

        if user_lower.startswith(
            "saya sedang membangun "
        ):

            project = user_message[
                len("saya sedang membangun "):
            ].strip()

            self.memory.save_memory(
                "current_project",
                project,
                user_id=user_id,
                chat_id=chat_id
            )

            return (
                f"Baik, saya akan mengingat proyek Anda: {project}."
            )

        if (
            "apa proyek saya" in user_lower
            or
            "proyek yang sedang saya kerjakan" in user_lower
        ):

            project = self.memory.get_memory(
                "current_project",
                user_id=user_id,
                chat_id=chat_id
            )

            if project:

                return (
                    f"Saat ini Anda sedang mengerjakan {project}."
                )

            return (
                "Saya belum mengetahui proyek Anda."
            )

        # ==========================
        # FAVORITE LANGUAGE
        # ==========================

        if user_lower.startswith(
            "bahasa favorit saya "
        ):

            language = user_message[
                len("bahasa favorit saya "):
            ].strip()

            self.memory.save_memory(
                "favorite_language",
                language,
                user_id=user_id,
                chat_id=chat_id
            )

            return (
                f"Baik, saya akan mengingat bahwa bahasa favorit Anda adalah {language}."
            )

        if (
            "bahasa favorit saya apa" in user_lower
            or
            "apa bahasa favorit saya" in user_lower
        ):

            language = self.memory.get_memory(
                "favorite_language",
                user_id=user_id,
                chat_id=chat_id
            )

            if language:

                return (
                    f"Bahasa favorit Anda adalah {language}."
                )

            return (
                "Saya belum mengetahui bahasa favorit Anda."
            )

        # ==========================
        # EDUCATION
        # ==========================

        if user_lower.startswith(
            "saya mahasiswa "
        ):

            education = user_message[
                len("saya mahasiswa "):
            ].strip()

            self.memory.save_memory(
                "education",
                education,
                user_id=user_id,
                chat_id=chat_id
            )

            return (
                f"Baik, saya akan mengingat bahwa Anda mahasiswa {education}."
            )

        if (
            "apa pendidikan saya" in user_lower
            or
            "saya mahasiswa apa" in user_lower
            or
            "pendidikan saya apa" in user_lower
        ):

            education = self.memory.get_memory(
                "education",
                user_id=user_id,
                chat_id=chat_id
            )

            if education:

                return (
                    f"Anda adalah mahasiswa {education}."
                )

            return (
                "Saya belum mengetahui pendidikan Anda."
            )

        # ==========================
        # CAREER GOAL
        # ==========================

        if user_lower.startswith(
            "target karier saya "
        ):

            goal = user_message[
                len("target karier saya "):
            ].strip()

            self.memory.save_memory(
                "career_goal",
                goal,
                user_id=user_id,
                chat_id=chat_id
            )

            return (
                f"Baik, saya akan mengingat bahwa target karier Anda adalah {goal}."
            )

        if (
            "apa target karier saya" in user_lower
            or
            "target karier saya apa" in user_lower
        ):

            goal = self.memory.get_memory(
                "career_goal",
                user_id=user_id,
                chat_id=chat_id
            )

            if goal:

                return (
                    f"Target karier Anda adalah {goal}."
                )

            return (
                "Saya belum mengetahui target karier Anda."
            )

        # ==========================
        # CURRENT LEARNING
        # ==========================

        if user_lower.startswith(
            "saya sedang belajar "
        ):

            learning = user_message[
                len("saya sedang belajar "):
            ].strip()

            self.memory.save_memory(
                "current_learning",
                learning,
                user_id=user_id,
                chat_id=chat_id
            )

            return (
                f"Baik, saya akan mengingat bahwa Anda sedang belajar {learning}."
            )

        if (
            "apa yang sedang saya pelajari"
            in user_lower
            or
            "saya sedang belajar apa"
            in user_lower
        ):

            learning = self.memory.get_memory(
                "current_learning",
                user_id=user_id,
                chat_id=chat_id
            )

            if learning:

                return (
                    f"Saat ini Anda sedang belajar {learning}."
                )

            return (
                "Saya belum mengetahui apa yang sedang Anda pelajari."
            )

        # ==========================
        # SKILL
        # ==========================

        if user_lower.startswith(
            "skill saya "
        ):

            skill = user_message[
                len("skill saya "):
            ].strip()

            self.memory.save_memory(
                "skill",
                skill,
                user_id=user_id,
                chat_id=chat_id
            )

            return (
                f"Baik, saya akan mengingat bahwa skill utama Anda adalah {skill}."
            )

        if (
            "apa skill saya" in user_lower
            or
            "skill saya apa" in user_lower
        ):

            skill = self.memory.get_memory(
                "skill",
                user_id=user_id,
                chat_id=chat_id
            )

            if skill:

                return (
                    f"Skill utama Anda adalah {skill}."
                )

            return (
                "Saya belum mengetahui skill Anda."
            )

        # ==========================
        # FAVORITE FRAMEWORK
        # ==========================

        if user_lower.startswith(
            "framework favorit saya "
        ):

            framework = user_message[
                len("framework favorit saya "):
            ].strip()

            self.memory.save_memory(
                "favorite_framework",
                framework,
                user_id=user_id,
                chat_id=chat_id
            )

            return (
                f"Baik, saya akan mengingat bahwa framework favorit Anda adalah {framework}."
            )

        if (
            "framework favorit saya apa" in user_lower
            or
            "apa framework favorit saya" in user_lower
        ):

            framework = self.memory.get_memory(
                "favorite_framework",
                user_id=user_id,
                chat_id=chat_id
            )

            if framework:

                return (
                    f"Framework favorit Anda adalah {framework}."
                )

            return (
                "Saya belum mengetahui framework favorit Anda."
            )

        return None
