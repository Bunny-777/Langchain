from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


llm=HuggingFaceEndpoint(
    repo_id="CohereLabs/tiny-aya-earth",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Tell me in detail about {person}",
    input_variables=["person"]
)
 
prompt2=PromptTemplate(
    template="Give a 5 line summary about the {topic} ",
    input_variables=["topic"]
)


chain = prompt1 | model | parser | prompt2 | model | parser

result=chain.invoke({"person":"Sunny leone"})
print(result)

chain.get_graph().print_ascii()