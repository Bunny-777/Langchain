from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()


parser=StrOutputParser()
llm=HuggingFaceEndpoint(
    repo_id="CohereLabs/tiny-aya-earth",
    task="text-generation"
)
model1=ChatHuggingFace(llm=llm)
model2=ChatGroq(
    model="qwen/qwen3-32b"
)

prompt1=PromptTemplate(
    template="Generate a brief summary from the given {topic}",
    input_variables=["topic"]

)
prompt2=PromptTemplate(
    template="Generate 5 one word question and answer from the given {topic}",
    input_variables=["topic"]
)

prompt3=PromptTemplate(
    template="Merge the following summary and qna answer into a single document \n notes-> {notes} and question & answer-> {qna}",
    input_variables=["notes","qna"]
)

parallel_chain= RunnableParallel({
    'notes' : prompt1 | model1 | parser,
    'qna' : prompt2 | model2 | parser
})

merge_chain= prompt3 | model1 | parser

chain= parallel_chain | merge_chain
result=chain.invoke({"topic":"the role of adult industry in reducing rapes"})

print(result)

chain.get_graph().print_ascii()