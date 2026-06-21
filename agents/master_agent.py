from services.llm_service import LLMService
from services.memory_service import MemoryService
from services.prompt_service import load_system_prompt


class MasterAgent:

    def __init__(self):

        self.memory = MemoryService()
        self.llm = LLMService()

    def chat(self, user_message):

        # ==========================
        # SMART MEMORY
        # ==========================

        user_lower = user_message.lower()

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
                "Maaf, saya belum mengetahui nama Anda."
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

        prompt = f"""
{system_prompt}

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