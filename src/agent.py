import asyncio
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from src.config.model import main_agent_model
from src.prompts.main_agent_prompt import get_main_agent_prompt


# Load MCP tools (requires blocking I/O)
# Run with: langgraph dev --allow-blocking
def _get_mcp_tools():
    """Initialize MCP client and retrieve tools."""
    async def _async_get_tools():
        mcp_client = MultiServerMCPClient({
            "filesystem": {
                "transport": "stdio",
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    r"C:\\Users\\PREDATOR\\Desktop\\AI_learn\\agent\\self-prompt-optimization-agent\\src\\prompts"
                ]
            }
        })
        return await mcp_client.get_tools()
    
    return asyncio.run(_async_get_tools())


# Initialize MCP tools
mcp_tools = _get_mcp_tools()

# Create and export agent for LangGraph with MCP tools
agent = create_agent(
    model=main_agent_model,
    system_prompt=get_main_agent_prompt(),
    tools=mcp_tools
)