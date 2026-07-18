from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Text summariser API",
    description="An API for summarising text",
    version="1.0.0"
)

class TextRequest(BaseModel):
    text: str

def summarise_text(text: str) -> str:
    """
    Placeholder summarisation function.
    This will later be replaced with an AI model.
    """

    words = text.split()

    # Simple placeholder: return first 20 words
    summary = " ".join(words[:20])

    return summary

@app.get("/")
def home():
    return {"message": "Text Summariser API is running"}

@app.post("/summarise")
def summarise(request: TextRequest):
    summary = summarise_text(request.text)

    return {
        "original_text": request.text,
        "summary": summary,
        "original_word_count": len(request.text.split()),
        "summary_word_count": len(summary.split())
    }