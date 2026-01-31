from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_tavily import TavilySearch

from src.config.model import main_agent_model
from src.config.mcp import mcp_tools
from src.meta_prompt import get_meta_prompt
from src.prompts.working_instruction_prompt import get_working_instruction_prompt
from src.prompts.user_profile import get_user_profile


tavily_search_tool = TavilySearch(
    max_results=3,
    topic="general",
)

tools = mcp_tools + [tavily_search_tool]
checkpointer = InMemorySaver()

system_prompt = (
    get_meta_prompt()
    + get_working_instruction_prompt()
    + get_user_profile()
)

# Create and export agent for LangGraph with MCP tools
# Run with: langgraph dev --allow-blocking
agent = create_agent(
    model=main_agent_model,
    system_prompt=system_prompt,
    tools=tools,
    name="main_agent",
    # checkpointer=checkpointer,
)
