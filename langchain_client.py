import asyncio
from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters, stdio_client

load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano")

stdio_server_params = StdioServerParameters(
    command="python",
    args=[
        "/Users/praveenantony/dev/repos/mcp-servers/mcp-crash-course/servers/math_server.py"
    ],
)


async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_agent(llm, tools)
            result = await agent.ainvoke(
                {"messages": [HumanMessage(content="What is 54 + 2 * 3?")]}
            )
            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
