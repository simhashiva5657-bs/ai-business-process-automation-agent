from strands import Agent

from agent.prompts import SYSTEM_PROMPT
from model.load import load_model
from mcp_client.client import get_mcp_client


def create_agent() -> Agent:
    """
    Create the business process automation agent
    using the local Ollama model and MCP tools.
    """

    model = load_model()
    mcp_client = get_mcp_client()

    return Agent(
        model=model,
        system_prompt=SYSTEM_PROMPT,
        tools=[mcp_client],
    )