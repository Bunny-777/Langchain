from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()
parser=JsonOutputParser()
llm=HuggingFaceEndpoint(
    repo_id="CohereLabs/tiny-aya-earth",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
parser=JsonOutputParser()
template=PromptTemplate(
    template="Give me the name,age,channel/page name and city of 5 famous indian youtuber and instagram influencer \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)
chain =template | model | parser 
ans=chain.invoke({})
for i in ans:
    print(i['channel'])

