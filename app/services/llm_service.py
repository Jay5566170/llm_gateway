from app.services.llm_router import LLMRouter


router = LLMRouter()


def generate_response(prompt):

    return router.generate(
        prompt
    )