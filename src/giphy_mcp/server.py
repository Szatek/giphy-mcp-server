import os
import httpx
import anyio
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastMCP Server
mcp = FastMCP("Giphy Search")

# Giphy API endpoint
GIPHY_API_URL = "https://api.giphy.com/v1/gifs/search"

@mcp.tool()
async def search_gifs(query: str, limit: int = 5, rating: str = "g") -> str:
    """Search for GIFs using the Giphy API.

    Args:
        query: The search term to find GIFs for.
        limit: The maximum number of GIFs to return (default: 5).
        rating: Filters results by specified rating (default: 'g').
    
    Returns:
        A formatted string describing the GIFs found with their URLs.
    """
    api_key = os.getenv("GIPHY_API_KEY")
    if not api_key:
        return "Error: GIPHY_API_KEY environment variable is not set. Please set it in your .env file."

    params = {
        "api_key": api_key,
        "q": query,
        "limit": limit,
        "rating": rating
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(GIPHY_API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
            gifs = data.get("data", [])
            
            if not gifs:
                return f"No GIFs found for query: '{query}'"
                
            result_lines = [f"Found {len(gifs)} GIFs for '{query}':\n"]
            for index, gif in enumerate(gifs, start=1):
                title = gif.get("title", "Untitled GIF")
                url = gif.get("url", "")
                embed_url = gif.get("embed_url", "")
                result_lines.append(f"{index}. Title: {title}")
                result_lines.append(f"   URL: {url}")
                result_lines.append(f"   Embed URL: {embed_url}\n")
                
            return "\n".join(result_lines)
            
        except httpx.HTTPStatusError as e:
            return f"HTTP error occurred while searching Giphy: {e}"
        except httpx.RequestError as e:
            return f"A request error occurred while searching Giphy: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

import sys

def main():
    """Run the Giphy MCP server or display help."""
    if len(sys.argv) == 1 or sys.argv[1] in ["help", "--help"]:
        print("========================================")
        print("          Giphy MCP Server              ")
        print("========================================")
        print("Usage:")
        print("  giphy-mcp run      - Run the MCP server on stdio (for agent tool integration)")
        print("  giphy-mcp help     - Show this help message")
        print("\nTo use with Antigravity, add this to your mcp_config.json:")
        print('  "giphy": {')
        print('    "command": "giphy-mcp",')
        print('    "args": ["run"],')
        print('    "env": {')
        print('      "GIPHY_API_KEY": "<your_api_key>"')
        print('    }')
        print('  }')
        sys.exit(0)
    
    if sys.argv[1] == "run":
        mcp.run(transport='stdio')
    else:
        print(f"Unknown argument: {sys.argv[1]}")
        print("Use 'giphy-mcp help' for usage instructions.")
        sys.exit(1)

if __name__ == "__main__":
    main()
