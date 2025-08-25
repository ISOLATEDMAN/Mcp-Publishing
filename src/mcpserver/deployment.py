from mcp.server.fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("PublishIt Demo Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers together."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two integers together."""
    return a * b

@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}! Welcome to PublishIt MCP Server!"  