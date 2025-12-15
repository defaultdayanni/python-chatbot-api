from fastapi import APIRouter

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
    Conversation,
    ConversationList
)

from app.database.repository import save_conversation
from app.repositories.conversation_repository import get_conversations

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    user_message = request.message

    # resposta mock (simples de propósito)
    bot_response = f"Você disse: {user_message}"

    # salva no banco
    save_conversation(user_message, bot_response)

    return ChatResponse(response=bot_response)




@router.get("/conversations", response_model=ConversationList)
def list_conversations(limit: int = 10):
    rows = get_conversations(limit)

    conversations = [
        {
            "id": row.id,
            "user_message": row.user_message,
            "bot_response": row.bot_response,
            "created_at": row.created_at,
        }
        for row in rows
    ]

    return {"conversations": conversations}

@router.get("/teste")
def teste():
    return {"msg": "rota funcionando"}
