from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="qwen/qwen3-32b",
    # model="openai/gpt-oss-120b" alternative model by chatGPT works very fast
)

while(True):
    prompt=input("User: ")
    if(prompt=="Exit"):
        break
    response=llm.invoke(prompt)
    print("AI: ",response.content)

