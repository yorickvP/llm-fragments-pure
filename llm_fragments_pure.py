import os
import httpx
import llm


@llm.hookimpl
def register_fragment_loaders(register):
    register("pure", pure_loader)


def pure_loader(argument: str) -> llm.Fragment:
    """
    Use pure.md to convert a URL to clean Markdown text.

    Example usage:
      llm -f 'pure:https://example.com' ...
    """
    url = f"https://pure.md/{argument}"
    
    headers = {}
    api_key = os.environ.get("PUREMD_API_KEY")
    if api_key:
        headers["x-puremd-api-token"] = api_key
    
    response = httpx.get(url, headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Failed to load fragment from {url}: {response.status_code}")
    return llm.Fragment(response.text, url)