import ollama

from ..config import OLLAMA_MODEL

def generate_summary(text: str) -> str:
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