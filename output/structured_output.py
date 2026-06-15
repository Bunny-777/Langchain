from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()
llm=ChatGroq(
    model="llama-3.3-70b-versatile" #old GPT model doesn't supports tool calling so this is used
)

class Review(TypedDict):
    summary : Annotated[str,"A brief summary of the text given"]
    sentiment : Annotated[str,"A sentiment about the text either positive, negative or neutral"]


structured_model=llm.with_structured_output(Review)

result=structured_model.invoke("Today when i wake up i got my girlfriend's message as good morning baby, she was very excited to tell me that today is her exam and she is missing me a lot and it gave me butterflies")
print(result)