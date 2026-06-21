from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile")
parser=StrOutputParser()
prompt1=PromptTemplate(
    template="Generate a joke on the {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Explain the following {joke}",
    input_variables=['joke']
)

chain=RunnableSequence(prompt1,llm,parser,prompt2,llm,parser)
print(chain.invoke({"topic":"pubg"}))
