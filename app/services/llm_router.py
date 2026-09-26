from app.providers.gemini import GeminiProvider


class LLMRouter:

    def __init__(self):

        self.providers = {
            "gemini": GeminiProvider()
        }


    def generate(
        self,
        prompt: str,
        provider="gemini"
    ):

        llm = self.providers.get(provider)

        if not llm:
            raise Exception(
                "Provider not found"
            )

        return llm.generate(prompt)