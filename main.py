from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from config import APP_NAME, APP_DESC, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    description=APP_DESC,
    version=APP_VERSION
)

class TextRequest(BaseModel):
    text: str = Field(
        min_length=10,
        max_length=5000,
        description="Text to summarise"
    )

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

@app.get("/health")
def health_check():
    return {"status": "healthy"}