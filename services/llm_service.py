from services.providers.gemini_provider import (
    GeminiProvider
)

class LLMService:

    def __init__(self):

        self.provider = GeminiProvider()

    def generate_response(
        self,
        prompt
    ):

        return self.provider.generate(
            prompt
        )