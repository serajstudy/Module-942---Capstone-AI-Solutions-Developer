import ollama


def ask_model(prompt: str, model_name: str) -> str:
    """Send a prompt to the Ollama model and return the answer."""

    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"].strip()