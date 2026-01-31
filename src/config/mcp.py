import asyncio
import os
from pathlib import Path

from langchain_mcp_adapters.client import MultiServerMCPClient

# MCP Server Configurations
_PROJECT_ROOT = Path(__file__).resolve().parents[1]
_DEFAULT_MCP_ROOT = _PROJECT_ROOT / "prompts"
_MCP_ROOT = Path(os.getenv("MCP_FILESYSTEM_ROOT", str(_DEFAULT_MCP_ROOT)))

MCP_SERVERS_CONFIG = {
    "filesystem": {
        "transport": "stdio",
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            str(_MCP_ROOT),
        ],
    }
}


_mcp_tools_cache = None


async def get_mcp_tools_async():
    """Initialize MCP client and retrieve tools (async)."""
    mcp_client = MultiServerMCPClient(MCP_SERVERS_CONFIG)
    return await mcp_client.get_tools()


def get_mcp_tools():
    """Initialize MCP client and retrieve tools (sync)."""
    global _mcp_tools_cache
    if _mcp_tools_cache is not None:
        return _mcp_tools_cache

    try:
        asyncio.get_running_loop()
    except RuntimeError:
        _mcp_tools_cache = asyncio.run(get_mcp_tools_async())
        return _mcp_tools_cache

    raise RuntimeError(
        "get_mcp_tools() called from async context; use await get_mcp_tools_async()."
    )


# Initialize MCP tools (sync import contexts)
mcp_tools = get_mcp_tools()
