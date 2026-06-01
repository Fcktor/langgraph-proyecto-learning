import sqlite3
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langgraph.checkpoint.sqlite import SqliteSaver

load_dotenv()

_conn = sqlite3.connect("conversations.db", check_same_thread=False)
memory = SqliteSaver(_conn)
tavily_tool = TavilySearch(max_results=2)
tools = [tavily_tool]

llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq", temperature=0.9)
llm_with_tools = llm.bind_tools(tools)

graph_config = {
    "configurable": {"thread_id": "1"}}