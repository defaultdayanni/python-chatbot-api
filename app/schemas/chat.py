from pydantic import BaseModel
from datetime import datetime
from typing import List

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str



class Conversation(BaseModel):
    id: int
    user_message: str
    bot_response: str
    created_at: datetime


class ConversationList(BaseModel):
    conversations: List[Conversation]
