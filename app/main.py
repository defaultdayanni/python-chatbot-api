from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Python Chatbot API")

@app.get("/")
def health_check():
    return {"status": "API rodando corretamente"}

app.include_router(router)
