from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.ai import ai_engine

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
def generate_text(request: PromptRequest):
    response = ai_engine.generate(request.prompt)
    if not response:
        raise HTTPException(status_code=500, detail="Ошибка генерации ответа.")
    return {"response": response}
router = APIRouter()

@router.get('/run')
def run_task():
    return {'status': 'running', 'message': 'Команда выполняется!'}
