from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    # model="qwen/qwen3-32b",
    model="openai/gpt-oss-120b" #alternative model by chatGPT works very fast
)

chathistory=[]
while(True):
    prompt=input("User: ")
    chathistory.append(prompt)
    if(prompt=="Exit"):
        break
    response=llm.invoke(chathistory)
    chathistory.append(response.content)
    print("AI: ",response.content)

print(chathistory)