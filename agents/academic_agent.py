from services.llm_service import LLMService


class AcademicAgent:

    def __init__(self):

        self.llm = LLMService()

    def handle(self, message):

        prompt = f"""
Anda adalah Academic Agent NEXA.

Bantu pengguna memahami:
- Materi kuliah
- Tugas
- Skripsi
- Pemrograman
- Pembelajaran

Pertanyaan:

{message}
"""

        return self.llm.generate_response(
            prompt
        )