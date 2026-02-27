import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from dotenv import load_dotenv

async def run_demo_agent():
    # We load the .env file so the child process inherits GIPHY_API_KEY
    load_dotenv()
    
    print("[Agent]: Starting up and connecting to the Giphy MCP Server...")
    
    server_params = StdioServerParameters(
        command=".\\venv\\Scripts\\python.exe",
        args=["giphy-mcp.py"],
    )

    # Connect to the server using standard input/output
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize connection to the server
            await session.initialize()
            
            # List available tools on the server
            tools = await session.list_tools()
            print("\n[Agent]: Connected! Here are the tools available on the server:")
            for tool in tools.tools:
                print(f"  - Tool: {tool.name}")
                print(f"    Description: {tool.description}")
                
            print("\n[Agent]: I want to send a funny coding GIF to the user.")
            print("[Agent]: Calling the 'search_gifs' tool with query='debugging code'...")
            
            # Call the target tool with arguments
            result = await session.call_tool(
                "search_gifs", 
                arguments={"query": "debugging code", "limit": 2} # Ask for top 2 GIFs
            )
            
            print("\n================ TOOL RESPONSE ================")
            for content in result.content:
                if content.type == "text":
                    print(content.text)
            print("===============================================\n")
            
            print("[Agent]: Perfect, I'll return these GIFs to the user now!")

if __name__ == "__main__":
    asyncio.run(run_demo_agent())
