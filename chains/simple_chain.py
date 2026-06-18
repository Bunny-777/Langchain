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

prompt=PromptTemplate(
    template="Write down 5 facts about {person}",
    input_variables=["person"]
)

chain=prompt | model | parser

result=chain.invoke({"Virat kohli"})
print(result)

chain.get_graph().print_ascii()