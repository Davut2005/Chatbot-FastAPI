from fastapi import APIRouter
from openai import OpenAI
from core.config import settings
import ollama

# client = OpenAI( api_key=settings.OPENAI_API_KEY )

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)


@router.post("")
async def createChat(msg: str):
    print("req came", flush=True)
    
    response = ollama.chat(
        model="llama2",
        messages= [
            {"role": "system", "content": "You are QA expert. Answer the questions with code blocks where possible"},
            {"role": "user", "content": msg}
        ]
    )

    print(f"response: {response['message']['content']} ", flush=True)

    return { "response": response["message"]["content"] }
