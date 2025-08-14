# src/search_tools.py

try:
    from ddgs import DDGS  # Preferred package for DuckDuckGo search
    ddgs_available = True
except ImportError:
    ddgs_available = False


def web_search(query: str):
    """
    Searches DuckDuckGo if ddgs is available, otherwise returns dummy results.
    """
    if ddgs_available:
        try:
            results = []
            with DDGS() as ddgs:
                for r in ddgs.text(query, max_results=5):
                    title = r.get("title", "No title")
                    link = r.get("href", "")
                    results.append(f"{title} - {link}")
            return results if results else [f"No search results found for '{query}'."]
        except Exception as e:
            return [f"Search error: {e}"]

    # Fallback: dummy results
    return [
        f"Dummy result 1 for '{query}'",
        f"Dummy result 2 for '{query}'",
        f"Dummy result 3 for '{query}'"
    ]






