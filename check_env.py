import langchain_core
import langchain
import langchain_openai
import pydantic

print("langchain_core:", langchain_core.__version__)
print("langchain:", langchain.__version__)
print("langchain_openai:", langchain_openai.__version__)
print("pydantic:", pydantic.__version__)

from langchain.agents import create_tool_calling_agent, AgentExecutor
print("OK: create_tool_calling_agent + AgentExecutor available")

from langchain_core.tools import tool
from langchain_core.pydantic_v1 import BaseModel as V1BaseModel
print("OK: langchain_core.tools.tool available")

try:
    from pydantic import BaseModel
    print("OK: pydantic.BaseModel available")
except Exception as e:
    print("pydantic.BaseModel import issue:", e)
