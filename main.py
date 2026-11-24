from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ask")
def ask(question: str):
    return {"question": question, "answer": "Placeholder answer"}