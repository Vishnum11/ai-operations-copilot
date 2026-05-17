from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import run_agent
from app.database import init_db, get_customers, get_appointments

app = FastAPI(title="AI Operations Copilot")

init_db()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Operations Copilot is running."}

@app.post("/chat")
def chat(request: ChatRequest):
    response = run_agent(request.message)
    return {"response": response}

@app.get("/customers")
def customers():
    return {"customers": get_customers()}

@app.get("/appointments")
def appointments():
    return {"appointments": get_appointments()}