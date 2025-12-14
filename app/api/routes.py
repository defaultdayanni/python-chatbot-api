from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Resposta temporária (mock)
    reply = f"Você disse: {request.message}"
    return ChatResponse(response=reply)
