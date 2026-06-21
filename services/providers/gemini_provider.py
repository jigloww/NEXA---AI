import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


class GeminiProvider:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY tidak ditemukan"
            )

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate(self, prompt):

        try:

            response = self.model.generate_content(
                prompt
            )

            return response.text

        except Exception as e:

            error_text = str(e)

            if "429" in error_text:
                return (
                    "Terjadi kesalahan pada API Gemini, Anda sudah mencapai limit penggunaan."
                )

            return (
                "Terjadi kesalahan pada API Gemini. Silakan coba lagi nanti."
            )