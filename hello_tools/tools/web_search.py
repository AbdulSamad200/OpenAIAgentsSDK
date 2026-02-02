"""
Web search tool using Tavily API.
"""

import os
from agents import function_tool
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
# Initialize Tavily client
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@function_tool
def web_search(query: str) -> str:
    """
    Search the web for the given query using Tavily API.
    
    Args:
        query: The search query to look up on the web.
        
    Returns:
        Search results from the web for the given query.
    """
    if not query or not query.strip():
        return "Error: No search query provided."
    
    try:
        print(f"Searching for: {query}")
        results = tavily_client.search(query)
        return str(results)
    except Exception as e:
        return f"Error performing web search: {str(e)}"
