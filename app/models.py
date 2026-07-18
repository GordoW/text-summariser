from pydantic import BaseModel, Field


class TextRequest(BaseModel):
    text: str = Field(
        min_length=10,
        max_length=5000,
        description="Text to summarise"
    )

class SummaryResponse(BaseModel):
    summary: str
    original_word_count: int
    summary_word_count: int
