from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session


from app.database.dependencies import get_db
from app.repositories.request_repository import create_request_log
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

    result = generate_response(request.prompt)


    create_request_log(
        db=db,
        prompt=request.prompt,
        response=result,
        provider="Gemini"
    )


    return {
        "response": result
    }