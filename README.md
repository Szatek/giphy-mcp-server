# Giphy MCP Server

[![CI](https://github.com/TODO_OWNER/giphy-mcp-server/actions/workflows/ci.yml/badge.svg)](https://github.com/TODO_OWNER/giphy-mcp-server/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/giphy-mcp.svg)](https://badge.fury.io/py/giphy-mcp)

An MCP (Model Context Protocol) server that allows AI agents to search and retrieve GIFs using the Giphy API. This provides a rich way for agents to express humor, reactions, or find relevant visual context.

## Prerequisites

- Python 3.10+
- A Giphy API Key. You can get a free API key at the [Giphy Developer Portal](https://developers.giphy.com/).

## Installation

For general use, install the package via pip:
```bash
pip install giphy-mcp
```

For development:
1. Clone the repository:
   ```bash
   git clone https://github.com/TODO_OWNER/giphy-mcp-server.git
   cd giphy-mcp-server
   ```
2. Create a virtual environment and install in editable mode:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Linux/macOS
   source venv/bin/activate
   
   pip install -e ".[dev]"
   ```

## Configuration

The server requires a Giphy API Key to function. It reads this from the `GIPHY_API_KEY` environment variable. 

You can configure this by:
1. Creating a `.env` file in the project root:
   ```env
   GIPHY_API_KEY=your_api_key_here
   ```
2. Or by passing it directly via your MCP client's configuration.

## Available Tools

- `search_gifs`
  - **Description**: Search for GIFs using the Giphy API.
  - **Parameters**: 
    - `query` (string): The search term to find GIFs for.
    - `limit` (int, optional): The maximum number of GIFs to return (default: 5).
    - `rating` (string, optional): Filters results by specified rating (default: 'g').

## Example Use Case (Agent Interaction)

When this server is registered with an AI agent (like Claude Desktop or Cursor), the agent can autonomously use it to attach GIFs to its responses.

**User**: "Can you celebrate that we finally deployed to production?"

**Agent (Internal Thought)**: *The user wants to celebrate. A celebratory GIF would be perfect here. I will use the `search_gifs` tool with the query "celebrate".*

**Agent (Tool Call)**:
```json
{
  "name": "search_gifs",
  "arguments": {
    "query": "celebrate",
    "limit": 1
  }
}
```

**Agent (Response)**: "Woohoo! That's awesome news! Here's a celebratory GIF to match the mood:
https://giphy.com/embed/artj92V8o75VPL7AeQ"

## Using with MCP Clients

To use this with an MCP client like Claude Desktop, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "giphy": {
      "command": "giphy-mcp",
      "args": [],
      "env": {
        "GIPHY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

*Note: You may need to specify the absolute path to the `giphy-mcp` executable if it's not in your system's PATH.*
