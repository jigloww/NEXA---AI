from services.llm_service import generate_response
from services.memory_service import MemoryService


class MasterAgent:

    def __init__(self):
        self.memory = MemoryService()

    def chat(self, user_message):

        self.memory.add_message("User", user_message)

        context = self.memory.get_context()

        prompt = f"""
Berikut adalah riwayat percakapan:

{context}

Jawablah sebagai NEXA.
"""

        response = generate_response(prompt)

        self.memory.add_message("NEXA", response)

        return response