#Method2 using stringOUtput parser

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

llm = HuggingFaceEndpoint(
    repo_id="CohereLabs/tiny-aya-earth",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)
parser=StrOutputParser()
template1=PromptTemplate(
    template="Write a detailed report on the {topic}",
    input_variables=["topic"]
)
template2=PromptTemplate(
    template="Write a 5 line summary report on the following text {text}",
    input_variables=["text"]
)

chain=template1 | model | parser | template2 | model | parser 
result=chain.invoke({'topic':'black hole'})
print(result)

#Method 1 using promptTemplate 

# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="CohereLabs/tiny-aya-earth",
#     task="text-generation",
# )

# model = ChatHuggingFace(llm=llm)

# template1=PromptTemplate(
#     template="Write a detailed report on the {topic}",
#     input_variables=["topic"]
# )
# template2=PromptTemplate(
#     template="Write a 5 line summary report on the following text {text}",
#     input_variables=["text"]
# )

# prompt1=template1.invoke({'topic':'Black hole'})
# result1=model.invoke(prompt1)
# prompt2=template2.invoke({'text':result1.content})
# result2=model.invoke(prompt2)


# print(result2.content) 

