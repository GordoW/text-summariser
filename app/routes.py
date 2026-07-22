from fastapi import APIRouter

from .models import TextRequest, SummaryResponse
from .services import summarise_text
from .llm.client import check_health
from .config import OLLAMA_MODEL


router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@router.get("/health/ai")
def ai_health():
    healthy = check_health()

    return {
        "status": "healthy" if healthy else "unavailable",
        "provider": "Ollama",
        "model": OLLAMA_MODEL
    }


@router.post("/summarise", response_model=SummaryResponse)
def summarise(request: TextRequest):

    summary = summarise_text(request.text)

    return {
        "summary": summary,
        "original_word_count": len(request.text.split()),
        "summary_word_count": len(summary.split())
    }