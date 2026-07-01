from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

search_tool = DuckDuckGoSearchRun()

llm = ChatGroq(
    model="qwen/qwen3-32b"
)

agent = create_agent(
    model=llm,
    tools=[search_tool],
    system_prompt="You are a helpful assistant. Use search when needed."
)

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "tell me any 3 smartphones under 90k in India"
        }
    ]
})

print(response["messages"][-1].content)