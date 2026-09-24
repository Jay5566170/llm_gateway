
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session


from app.database.dependencies import get_db
from app.repositories.request_repository import create_request_log
from app.repositories.conversation_repository import (
    create_conversation,
    get_all_conversations
)

from app.repositories.message_repository import (
    create_message,
    get_messages_by_conversation
)
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

@app.get("/conversations")
def get_conversations(
    db: Session = Depends(get_db)
):

         conversations = get_all_conversations(db)

         return conversations

@app.get("/conversations/{conversation_id}")
def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db)
):

    messages = get_messages_by_conversation(
        db=db,
        conversation_id=conversation_id
    )

    return {
        "conversation_id": conversation_id,
        "messages": messages
    }