from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(
    # repo_id="CohereLabs/tiny-aya-earth",
    repo_id="nex-agi/Nex-N2-Pro",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
schema=[
    ResponseSchema(name='name',description='Name of that youtuber or instagram influencer'),
    ResponseSchema(name='subscriber_count',description="Count of that subsriber or followers in million"),
    ResponseSchema(name='country',description='Country of that person')
]
parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="Tell me about famous indian gaming youtuber and instagram influencer \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)
chain =template | model | parser 
ans=chain.invoke({})
print(ans)

