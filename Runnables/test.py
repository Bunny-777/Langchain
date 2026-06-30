from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile")
print(llm.invoke("how to test the battery health of a windows laptop using the command prompt?"))