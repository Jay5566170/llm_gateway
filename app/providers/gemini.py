import os
from dotenv import load_dotenv
from google import genai

from app.providers.base import LLMProvider


load_dotenv()


class GeminiProvider(LLMProvider):

    def __init__(self, api_key=None):

        if api_key is None:
            api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise Exception(
                "GEMINI_API_KEY is missing"
            )

        self.client = genai.Client(
            api_key=api_key
        )


    def generate(self, prompt: str) -> str:

        try:

            response = self.client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print("Gemini Error:", e)
            raise e