from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from langchain_classic.agents import create_react_agent,AgentExecutor
from langchain_core.prompts import PromptTemplate
import requests
load_dotenv()

search_tool=DuckDuckGoSearchRun()
llm=ChatGroq(
    model="qwen/qwen3-32b"
)


template = """Answer the following questions as best you can. You have access to the following tools: {tools}
Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
Begin!
Question: {input}
Thought:{agent_scratchpad}"""

prompt = PromptTemplate.from_template(template)


agent=create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

agent_executor=AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

respose=agent_executor.invoke({"input":"tell me any 3 smartphones under 90k"})
print(respose)
