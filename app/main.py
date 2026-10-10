from fastapi import FastAPI

app = FastAPI(
    title="ExpenseAI",
    description="AI-powered personal expense tracker",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}