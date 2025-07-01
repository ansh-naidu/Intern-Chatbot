from fastapi import APIRouter
from app.services.chatbot import ask_chatbot

router = APIRouter()

@router.get("/chatbot")
def chatbot_ask(question: str):
    answer = ask_chatbot(question)
    return {"question": question, "answer": answer}
