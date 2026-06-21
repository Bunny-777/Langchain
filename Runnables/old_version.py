import random

class NakliLLm():
    def __init__ (self):
        print("LLM created")
    def predict(self,prompt):
        response_list=[
            "Dex is gawar bitch",
            "Kajal is an artist",
            "Chijji is an accountant"
        ]
        return {"response":random.choice(response_list)}

class NakliPromptTemplate():
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables

    def format(self,input_dict):
        return self.template.format(**input_dict)

class NakliLLMChain():
    def __init__(self,llm,prompt):
        self.llm=llm
        self.prompt=prompt
        
    def run(self,input_dict):
        final=self.prompt.format(input_dict)
        result=self.llm.predict(final)
        return result['response']

        


llm=NakliLLm()
prompt=NakliPromptTemplate(
    template="who is the {topic}",
    input_variables=["topic"]
)
chain=NakliLLMChain(llm,prompt)

result=chain.run({"topic":"sunny leone"})
print(result)


