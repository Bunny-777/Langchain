from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

class Feedback(BaseModel):
    sentiment : Literal['positive','negative']= Field(description="This is used to classify the sentiment of the feedback as positive or negative")

parser=StrOutputParser()
parser2=PydanticOutputParser(pydantic_object=Feedback)

llm=HuggingFaceEndpoint(
    repo_id="CohereLabs/tiny-aya-earth",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
prompt1=PromptTemplate(
    template="From the following {feedback} classify the sentiment into positive or negative \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":parser2.get_format_instructions()}
)

chain=prompt1 | model | parser2
result=chain.invoke({"feedback":"This is so awesome product"})
print(result.sentiment)
