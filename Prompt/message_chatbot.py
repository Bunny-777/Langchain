from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(
    model="openai/gpt-oss-120b"
)

chathistory=[
    SystemMessage(content="You are a doctor ai")
]

while(True):
    prompt=input("User: ")
    chathistory.append(HumanMessage(content=prompt))
    if(prompt=="Exit"):
        break
    response=llm.invoke(chathistory)
    chathistory.append(AIMessage(content=response.content))
    print("AI: ",response.content)

print(chathistory)