def is_valid_question(text: str) -> bool:
    """Check whether the student entered a question."""

    cleaned = text.strip()

    return len(cleaned) > 0