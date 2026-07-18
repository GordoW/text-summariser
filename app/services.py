from .llm.client import generate_summary

def summarise_text(text: str) -> str:
    """
    Summarise text using an LLM
    """

    summary = generate_summary(text)

    return summary