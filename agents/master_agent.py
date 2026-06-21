from services.llm_service import LLMService
from services.memory_service import MemoryService
from services.prompt_service import load_system_prompt


class MasterAgent:

    def __init__(self):

        self.memory = MemoryService()
        self.llm = LLMService()

    def chat(self, user_message):

        user_lower = user_message.lower()

        # ==========================
        # USER NAME
        # ==========================

        if user_lower.startswith("nama saya "):

            name = user_message[10:].strip()

            self.memory.save_memory(
                "user_name",
                name
            )

            return (
                f"Baik, saya akan mengingat bahwa nama Anda {name}."
            )

        if "siapa nama saya" in user_lower:

            name = self.memory.get_memory(
                "user_name"
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
                len("Saya sedang membangun "):
            ].strip()

            self.memory.save_memory(
                "current_project",
                project
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
                "current_project"
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
                len("Bahasa favorit saya "):
            ].strip()

            self.memory.save_memory(
                "favorite_language",
                language
            )

            return (
                f"Baik, saya akan mengingat bahwa bahasa favorit Anda adalah {language}."
            )

        if (
            "bahasa favorit saya apa"
            in user_lower
        ):

            language = self.memory.get_memory(
                "favorite_language"
            )

            if language:

                return (
                    f"Bahasa favorit Anda adalah {language}."
                )

            return (
                "Saya belum mengetahui bahasa favorit Anda."
            )

        # ==========================
        # SHORT TERM MEMORY
        # ==========================

        self.memory.add_message(
            "User",
            user_message
        )

        system_prompt = load_system_prompt()

        context = self.memory.get_context()

        # ==========================
        # LONG TERM MEMORY INJECTION
        # ==========================

        all_memories = (
            self.memory.get_all_memories()
        )

        memory_context = ""

        for key, value in all_memories:

            memory_context += (
                f"{key}: {value}\n"
            )

        prompt = f"""
{system_prompt}

Informasi yang Anda ketahui tentang pengguna:

{memory_context}

Riwayat Percakapan:

{context}

Jawablah sebagai NEXA.
"""

        response = self.llm.generate_response(
            prompt
        )

        self.memory.add_message(
            "NEXA",
            response
        )

        return response