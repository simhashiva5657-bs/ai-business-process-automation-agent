from pathlib import Path

from mcp.client.stdio import stdio_client, StdioServerParameters
from strands.tools.mcp.mcp_client import MCPClient


SERVER_PATH = (
    Path(__file__).resolve().parents[1]
    / "mcp_server"
    / "server.py"
)


def get_mcp_client() -> MCPClient:
    """Create an MCP client for the local business-agent MCP server."""

    server_params = StdioServerParameters(
        command="python",
        args=[str(SERVER_PATH)],
    )

    return MCPClient(
        lambda: stdio_client(server_params)
    )