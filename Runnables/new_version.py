from abc import ABC, abstractmethod
class Runnable(ABC):
    @abstractmethod
    def invoke(self,input_data):
        pass

import random
class NakliLLm(Runnable):
    def __init__ (self):
        print("LLM created")
    def predict(self,prompt):
        response_list=[
            "Dex is gawar bitch",
            "Kajal is an artist",
            "Chijji is an accountant"
        ]
        print("Older method to call the function") # this is used to tell the users that do not use this method use new instead
        return {"response":random.choice(response_list)}
    def invoke(self,prompt):
        response_list=[
            "Dex is gawar bitch",
            "Kajal is an artist",
            "Chijji is an accountant"
        ]
        return {"response":random.choice(response_list)}

class NakliPromptTemplate(Runnable):
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables

    def format(self,input_dict):
        return self.template.format(**input_dict)
    def invoke(self,input_dict):
        return self.template.format(**input_dict)

class RunnableConnector(Runnable):
    def __init__(self,runnable_list): #here we work like Chain=RunnableConnector([llm,prompt]) so list will be made
        self.runnable_list=runnable_list

    def invoke(self,input_data):
        for runnable in self.runnable_list: # iterating over each item of list i.e. llm and prompt
            input_data=runnable.invoke(input_data)  # calling the invoke function of iterator and then passing it input value and storing it again in input value so that the next iterator has the output as its input to make a chain
        return input_data

llm=NakliLLm()
prompt=NakliPromptTemplate(
    template="who is the father of {person}",
    input_variables=["person"]
)
chain=RunnableConnector([prompt,llm])

print(chain.invoke({"person":"milka singh"}))