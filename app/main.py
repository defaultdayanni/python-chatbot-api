from fastapi import FastAPI

app = FastAPI(title="Chatbot API")

@app.get("/")
def health_check():
    return {"status": "API rodando corretamente"}
