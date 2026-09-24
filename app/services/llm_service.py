from app.services.provider_manager import generate_with_fallback


def generate_response(prompt):

    response = generate_with_fallback(prompt)

    return response