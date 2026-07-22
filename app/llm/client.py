import ollama

from ..config import OLLAMA_MODEL
from ..exceptions import LLMServiceError

def generate_summary(text: str) -> str:
    """
    Generates a summary using Ollama
    """
    try:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            options={
                "temperature": 0.2
            },
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a text summarisation assistant. "
                        "Create concise summaries that are shorter than the original text. "
                        "Only include the key points. "
                        "Do not add explanations, introductions, or bullet points unless requested."
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        return response["message"]["content"]
    
    except Exception as e:
        raise LLMServiceError(
            "Unable to generate summary"
        ) from e
    
def check_health() -> bool:
    try:
        models = ollama.list()
        available_models = [
            model.model for model in models.models
        ]

        return OLLAMA_MODEL in available_models
    except Exception:
        return False