from langchain_openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model="gpt-3.5-turbo-instruct")

ans=llm.invoke("what is the capital of america?")
print(ans)