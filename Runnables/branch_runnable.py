from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv
load_dotenv()

class Feedback(BaseModel):
    sentiment : Literal['positive','negative']= Field(description="This is used to classify the sentiment of the feedback as positive or negative")

llm=ChatGroq(model="llama-3.3-70b-versatile")
parser1=StrOutputParser()
parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="classify the following {text} as positive or negative \n {format_instruction}",
    input_variables=['text'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

prompt2=PromptTemplate(
    template="Generate a response to the following positive {feedback} ",
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template="Generate a response to the following negative {feedback}",
    input_variables=['feedback']
)

Feedback_chain=RunnableSequence(prompt1,llm,parser2)
branch_chain=RunnableBranch(
    (lambda x : x.sentiment=='positive',RunnableSequence(prompt2,llm,parser1)),
    RunnableSequence(prompt3,llm,parser1)
)

final_chain=RunnableSequence(Feedback_chain,branch_chain)
print(final_chain.invoke("This is a fucking bad smartphone"))