# src/fact_checker.py

from search_tools import web_search

def fact_check(query: str) -> str:
    """
    Minimal fact-checking logic that uses real DuckDuckGo search results.
    """
    results = web_search(query)
    if not results:
        return f"No search results found for '{query}'."
    return f"Fact-check results for '{query}':\n" + "\n".join(results)



