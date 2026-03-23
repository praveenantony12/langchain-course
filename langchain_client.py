import asyncio
from pathlib import Path

from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import StdioServerParameters

load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano")

stdio_server_params = StdioServerParameters(
    command="python",
    args=[
        "/Users/praveenantony/dev/repos/mcp-servers/mcp-crash-course/servers/math_server.py"
    ],
)


async def main():
    print("Hello langchain MCP client!")


if __name__ == "__main__":
    asyncio.run(main())
