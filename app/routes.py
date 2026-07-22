from fastapi import APIRouter
import logging

from .models import TextRequest, SummaryResponse
from .services import summarise_text
from .llm.client import check_health
from .config import OLLAMA_MODEL

logger = logging.getLogger(__name__)
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
    logger.info(
        "Summarisation request recieved. "
        "Characters: %s",
        len(request.text)
    )

    summary = summarise_text(request.text)

    logger.info(
        "Summary generated successfully"
    )

    return {
        "summary": summary,
        "original_word_count": len(request.text.split()),
        "summary_word_count": len(summary.split())
    }