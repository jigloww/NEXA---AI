from services.llm_service import LLMService


class BusinessAgent:

    def __init__(self):

        self.llm = LLMService()

    def handle(self, message):

        prompt = f"""
Anda adalah Business Agent NEXA.

Fokus membantu pengguna dalam:

- Bisnis
- Startup
- Analisis pasar
- Strategi pemasaran
- Monetisasi
- Model bisnis
- Validasi ide usaha

Permintaan pengguna:

{message}
"""

        return self.llm.generate_response(
            prompt
        )