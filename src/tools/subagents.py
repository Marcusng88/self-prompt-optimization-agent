from langchain.tools import tool
from langchain.agents import create_agent
from src.config.model import financial_news_agent_model
from src.prompts.financial_news_agent_prompt import get_financial_news_agent_prompt
import os
from langchain_tavily import TavilySearch

tavily_search_tool = TavilySearch(
    max_results=3,
    topic="finance"
)
    
    

@tool(description="research for financial news articles")
def call_financial_news_agent(query: str) -> str:
    agent = create_agent(
        model=financial_news_agent_model,
        system_prompt=get_financial_news_agent_prompt(),
        tools=[tavily_search_tool]
    )
    result = agent.invoke({"messages": [{"role": "user", "content": query}]})
    return result["messages"][-1].content
    