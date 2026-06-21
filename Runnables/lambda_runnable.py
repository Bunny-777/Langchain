from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile")
parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Generate a short poem on the {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Summarise the poem from the given {text}",
    input_variables=['text']
)

def wordct(word):
    lis=word.split()
    return len(lis)

poem_chain=RunnableSequence(prompt1,llm,parser)

parallel_chain=RunnableParallel({
    "poem":RunnablePassthrough(),
    "word_count":RunnableLambda(wordct)
})

final_chain=RunnableSequence(poem_chain,parallel_chain)
print(final_chain.invoke({"topic":"girlfriend"}))