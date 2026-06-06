from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from agent import ask_agent

# =========================
# FASTAPI
# =========================

app = FastAPI()

# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# REQUEST MODEL
# =========================

class ChatRequest(BaseModel):
    message: str

# =========================
# HOME
# =========================

@app.get("/")
def home():

    return {
        "message": "AI Persona Backend Running"
    }

# =========================
# CHAT API
# =========================

@app.post("/chat")
async def chat(req: ChatRequest):

    response = ask_agent(req.message)

    return {
        "response": response
    }