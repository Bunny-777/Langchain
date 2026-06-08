from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="CohereLabs/tiny-aya-earth",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of Pakistan?")
print(response.content)