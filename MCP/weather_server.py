from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather_status(location:str)->str:
    """Get weather details for the given location"""
    return "It's currently raining in San Francisco."

if __name__=="__main__":
    mcp.run(transport="stdio")