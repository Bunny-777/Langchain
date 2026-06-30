from langchain_community.tools import DuckDuckGoSearchRun,ShellTool
search_tool=DuckDuckGoSearchRun()
shell_tool=ShellTool()


result=search_tool.invoke("iphone 17")
# print(result)


query=shell_tool.invoke("whoami")
print(query)
