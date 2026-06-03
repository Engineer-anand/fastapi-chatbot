from App.ai.groq import ai_platform
import os
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware - taaki frontend se backend ko call kar sakein
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files serve karne ke liye (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- Pydantic Models ---
class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str

# --- Routes ---

@app.get("/", response_class=HTMLResponse)
async def root():
    """Main UI page serve karta hai"""
    with open("static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Non-streaming: poora response ek baar mein return karta hai"""
    response_chunks = []
    async for chunk in ai_platform.chat(request.prompt):
        response_chunks.append(chunk)
    response_text = "".join(response_chunks)
    return ChatResponse(response=response_text)

@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """Streaming: response chunks real-time mein send karta hai"""
    async def generator():
        async for chunk in ai_platform.chat(request.prompt):
            yield chunk.encode("utf-8")
    return StreamingResponse(generator(), media_type="text/plain; charset=utf-8")
