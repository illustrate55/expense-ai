from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="ExpenseAI",
    description="AI-powered personal expense tracker",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "app": settings.app_name,
        "enviroment": settings.app_env,
    }