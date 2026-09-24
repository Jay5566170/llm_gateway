from app.providers.gemini import generate_with_gemini
from app.providers.openai import generate_with_openai


def generate_with_fallback(prompt):

    try:

        response = generate_with_gemini(prompt)

        return response


    except Exception:

        response = generate_with_openai(prompt)

        return response