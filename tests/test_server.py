import pytest
from unittest.mock import patch, MagicMock
from giphy_mcp.server import search_gifs

@pytest.mark.asyncio
@patch("giphy_mcp.server.httpx.AsyncClient")
@patch("giphy_mcp.server.os.getenv")
async def test_search_gifs_success(mock_getenv, mock_async_client):
    # Setup mock env
    mock_getenv.return_value = "TEST_API_KEY"
    
    # Setup mock response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "data": [
            {
                "title": "Funny Cat",
                "url": "https://giphy.com/gifs/funny-cat",
                "embed_url": "https://giphy.com/embed/funny-cat"
            }
        ]
    }
    
    mock_client_instance = MagicMock()
    # `get` is awaited, so make sure it returns the mock_response asynchronously
    from unittest.mock import AsyncMock
    mock_client_instance.get = AsyncMock(return_value=mock_response)
    
    # Mock context manager
    mock_async_client.return_value.__aenter__.return_value = mock_client_instance
    
    result = await search_gifs("cat")
    
    assert "Found 1 GIFs for 'cat'" in result
    assert "Title: Funny Cat" in result
    assert "URL: https://giphy.com/gifs/funny-cat" in result

@pytest.mark.asyncio
@patch("giphy_mcp.server.os.getenv")
async def test_search_gifs_no_api_key(mock_getenv):
    mock_getenv.return_value = None
    result = await search_gifs("cat")
    assert "Error: GIPHY_API_KEY environment variable is not set" in result
