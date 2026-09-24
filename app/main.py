from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session


from app.database.dependencies import get_db

from app.repositories.request_repository import create_request_log
from app.repositories.conversation_repository import create_conversation
from app.repositories.message_repository import create_message

from app.services.llm_service import generate_response


app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():

    return {
        "message": "LLM Gateway is running"
    }


@app.post("/generate")
def generate(
    request: PromptRequest,
    db: Session = Depends(get_db)
):

    conversation = create_conversation(
        db=db,
        title=request.prompt[:50]
    )


    create_message(
        db=db,
        conversation_id=conversation.id,
        role="user",
        content=request.prompt
    )


    result = generate_response(request.prompt)


    create_message(
        db=db,
        conversation_id=conversation.id,
        role="assistant",
        content=result
    )


    create_request_log(
        db=db,
        prompt=request.prompt,
        response=result,
        provider="gemini"
    )


    return {
        "conversation_id": conversation.id,
        "response": result
    }