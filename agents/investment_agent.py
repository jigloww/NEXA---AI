from services.llm_service import LLMService


class InvestmentAgent:

    def __init__(self):

        self.llm = LLMService()

    def handle(self, message):

        prompt = f"""
Anda adalah Investment Agent NEXA.

Fokus membantu pengguna dalam:

- Investasi
- Saham
- Reksadana
- ETF
- Keuangan pribadi
- Manajemen risiko
- Edukasi investasi

Permintaan pengguna:

{message}
"""

        return self.llm.generate_response(
            prompt
        )