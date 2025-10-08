"""Local LLM orchestration endpoints for Noah core."""
from __future__ import annotations

from pathlib import Path
from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["ai"])


class ChatRequest(BaseModel):
    prompt: str
    model: Literal["mistral", "phi-3", "llama3"] = "mistral"


class ChatResponse(BaseModel):
    response: str
    model: str


OLLAMA_ENDPOINT = Path("configs/settings.yaml")


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Return a deterministic response to showcase the API contract."""
    response_text = (
        "[Noah] This is a placeholder response. Configure Ollama to enable on-device LLM inference."
    )
    return ChatResponse(response=response_text, model=request.model)
