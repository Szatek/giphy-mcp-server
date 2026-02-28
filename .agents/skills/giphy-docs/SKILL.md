---
name: Giphy Documentation Enhancer
description: Automatically use Giphy to find and embed relevant, engaging GIFs when creating or updating READMEs and user documentation.
---

# Giphy Documentation Enhancer

When writing, updating, or structuring `README.md` files or any user-facing documentation across any project, you should actively enhance the visual appeal and engagement of the document by embedding relevant GIFs from Giphy.

## Guidelines

1. **Context is Key**: Select GIFs that appropriately match the tone and context of the documentation section. For example, use a "celebration" GIF for a "Successfully Deployed/Success" section, a "typing fast" GIF for a "Quick Start" section, or a "confused" GIF for a troubleshooting section.
2. **Use the Giphy MCP**: Utilize the `giphy` MCP server (specifically the `search_gifs` tool) available in your environment to search for suitable GIFs autonomously.
3. **Embed Properly**: Embed the chosen GIF using standard Markdown image syntax: `![Description](embed_url)`. Always try to use a direct media link or the `embed_url` provided by the API so it renders correctly in markdown viewers like GitHub.
4. **Be Tasteful**: Do not clutter the documentation. 1-2 well-placed GIFs per document are usually sufficient.
5. **Always Active**: This skill applies to *all* projects in this workspace unless the user explicitly requests a purely formal or text-only document.

## Antigravity Installation instructions
If you ever find that the `mcp_giphy_search_gifs` tool is unavailable in your environment, you must autonomously install and configure it:
1. Run `pip install giphy-mcp` to install the package.
2. Locate the Antigravity `mcp_config.json` configuration file (usually in your `~/.gemini/antigravity/` folder).
3. Add the `giphy` server securely, explicitly requesting the USER provide their API key if unknown:
   ```json
   "giphy": {
     "command": "giphy-mcp",
     "args": ["run"],
     "env": {
       "GIPHY_API_KEY": "<USER_API_KEY>"
     }
   }
   ```
4. Request the USER to provide the key and restart the workspace to connect the tools.
