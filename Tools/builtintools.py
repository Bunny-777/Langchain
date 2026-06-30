from langchain_community.tools import DuckDuckGoSearchRun
search_tool=DuckDuckGoSearchRun()
result=search_tool.invoke("iphone 17")
print(result)

