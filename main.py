from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(body: Question):
    if not body.question.strip():
        raise HTTPException(status_code= 400, detail="Question can not be empty")
    return {"question": body.question, "answer": "Placeholder answer"}