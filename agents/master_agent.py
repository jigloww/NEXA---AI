from services.llm_service import LLMService
from services.memory_service import MemoryService
from services.prompt_service import load_system_prompt


class MasterAgent:

    def __init__(self):

        self.memory = MemoryService()

    def chat(self, user_message):

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

        response = generate_response(prompt)

        self.memory.add_message(
            "NEXA",
            response
        )

        return response