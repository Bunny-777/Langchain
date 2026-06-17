from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=0)  # specify model explicitly

response = model.invoke("Who is the Prime Minister of India?")
print(response.content)