from dotenv import load_dotenv

# from langchain_tavily import TavilySearchResults

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient()


@tool
def search(query: str) -> str:
    """
    Tool that searches internet for information.
    Args:
        query: The query to search for.
    Returns:
        The search results.
    """
    print(f"Searching the web for: {query}")
    return tavily.search(query=query)


llm = ChatOpenAI(model="gpt-4.1-nano")
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="Search for 3 job openings for mainframe developer (JCL, CICS, COBOL, etc.) in raleigh durham area where in title its mentioned mainframein linkedin and list their details"
            )
        }
    )
    print(result)


if __name__ == "__main__":
    main()
