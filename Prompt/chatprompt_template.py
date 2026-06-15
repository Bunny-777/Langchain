# This is slighlty different from prompt template
# where we can simple use the invoke function to pass the values
# but in this we have to define the reole before passing anything


# below is the code for prompt template 
'''
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()]
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)
prompt = template2.invoke({'name':'nitish'})
result = model.invoke(prompt)
print(result.content)
'''

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)

