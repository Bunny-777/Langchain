from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile")
parser=StrOutputParser()
prompt1=PromptTemplate(
    template="Generate a x post on the {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Generate a linkedin post on the {topic}",
    input_variables=["topic"]
)

parallel_chain=RunnableParallel(
    {"x":RunnableSequence(prompt1,llm,parser),
    "linkedin":RunnableSequence(prompt2,llm,parser)}
)

result=parallel_chain.invoke({"leetcode knight"})
print(result['x'])
print('\n\n\n')
print(result['linkedin'])