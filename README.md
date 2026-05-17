# AI Operations Copilot

AI Operations Copilot is a multi-agent AI business assistant built using LangGraph, FastAPI, Ollama, Streamlit, and SQLite. The system simulates a real-world AI operations platform capable of routing customer requests between specialized AI agents for scheduling, customer support, and CRM workflows.

This project demonstrates modern AI engineering concepts including:
- Multi-agent orchestration
- Workflow routing
- Local LLM inference
- Backend API development
- Persistent memory
- Full-stack AI application architecture

---

# Features

- Multi-agent AI workflow system
- Intelligent request routing using LangGraph
- AI-powered customer support agent
- Appointment scheduling agent
- CRM/customer issue management agent
- Local LLM inference using Ollama
- Persistent SQLite database memory
- FastAPI backend API
- Streamlit interactive frontend dashboard
- Completely free and locally runnable

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangGraph | Multi-agent workflow orchestration |
| FastAPI | Backend API framework |
| Ollama | Local LLM inference |
| Streamlit | Frontend dashboard |
| SQLite | Persistent memory/database |
| LangChain | LLM integration |

---

# Project Architecture

```text
Frontend (Streamlit)
        ↓
FastAPI Backend
        ↓
LangGraph Router Agent
        ↓
Specialized AI Agents

```
# Setup and Run Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-operations-copilot.git
cd ai-operations-copilot
   ├── Support Agent
   ├── Scheduling Agent
   └── CRM Agent
        ↓
```
## 2. Create the virtual enviornment
SQLite Database + Ollama LLM
python3 -m venv venv
source venv/bin/activate

## 3. Install Requirements.txt
## 4. Install Ollama
## 5. Start Backend
python -m uvicorn app.main:app --reload
## 6. Start Frontend
streamlit run app/frontend.py
