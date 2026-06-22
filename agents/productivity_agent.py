from services.llm_service import LLMService


class ProductivityAgent:

    def __init__(self):

        self.llm = LLMService()

    def handle(self, message):

        prompt = f"""
Anda adalah Productivity Agent NEXA.

Fokus membantu pengguna dalam:
- Produktivitas
- Jadwal belajar
- To-do list
- Target mingguan
- Target bulanan
- Manajemen waktu

Permintaan pengguna:

{message}
"""

        return self.llm.generate_response(
            prompt
        )