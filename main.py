from email.policy import default
from typing import List

from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


class Source(BaseModel):
    """Schema for a source used by agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response"""

    answer: str = Field(description="The agent's answer to the query")
    sources: List(Source) = Field(
        default_factory=list, description="The list of sources to generate the answer"
    )


llm = ChatOpenAI(model="gpt-4.1-nano")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


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
