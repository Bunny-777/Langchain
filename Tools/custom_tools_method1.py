from langchain_core.tools import tool

def multiply(a,b):
    return a*b

def multiply(a:int ,b:int) -> int:
        """Multiply the given two numbers"""
        return a*b

@tool
def multiply(a:int, b:int) ->int:
      """Mutltiply the given two numbers"""
      return a*b

result=multiply.invoke({"a":4,"b":5})
print(result)


print(multiply.name)
print(multiply.args)
print(multiply.description)