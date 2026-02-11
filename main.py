from fastapi import FastAPI
from api_routers import chat

app = FastAPI()

app.include_router(chat)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
