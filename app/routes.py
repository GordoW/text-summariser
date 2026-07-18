from fastapi import APIRouter

from .models import TextRequest
from .services import summarise_text


router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@router.post("/summarise")
def summarise(request: TextRequest):

    summary = summarise_text(request.text)

    return {
        "summary": summary,
        "original_word_count": len(request.text.split()),
        "summary_word_count": len(summary.split())
    }