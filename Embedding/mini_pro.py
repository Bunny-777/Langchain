from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
document =[
    "Bunny is an AI engineer",
    "Dex is a gawar bitch",
    "Kajal is an artist",
    "Meet is an accountant",
    "Dell is a content creator"
]

query=input("Enter any name ")
doc_embedding=embedding.embed_documents(document)
vector=embedding.embed_query(query)
scores=cosine_similarity([vector],doc_embedding)

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(document[index])



