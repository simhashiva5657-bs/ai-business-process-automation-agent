from strands.models.ollama import OllamaModel


def load_model():
    """
    Load the local Ollama model used by the business agent.
    """

    return OllamaModel(
        host="http://localhost:11434",
        model_id="llama3.2:3b",
    )