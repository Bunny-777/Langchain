from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-3.5-flash")
response=model.invoke("who is the president of america and who is the vice president?")
print(response.content)