from datetime import datetime
import os
import random
from typing import Literal
from typing_extensions import Annotated, TypedDict
from langchain_ollama import ChatOllama

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


def get_temperature(
        location: str, date: str = datetime.strftime(datetime.now(), "%Y-%m-%d")
):
    """获得某地区某日期的问题

    Args:
        location: 一个地区名，使用三级标准地区格式，如"中国-河北-秦皇岛"
        date: 日期，格式为"%Y-%m-%d"，默认为当天

    Returns:
        dict: 包含地区、日期和温度的字典
    """
    return {"location": location, "date": date, "temperature": random.uniform(10, 30), "temp_scale": "摄氏度"}


llm = ChatOllama(model="llama3.1:8b").bind_tools([get_temperature])


class State(TypedDict):
    messages: Annotated[list, add_messages]


workflow = StateGraph(State)


def get_user_input(state: State) -> dict[str, HumanMessage]:
    return {"messages": HumanMessage(content=input("User: "))}


def get_response(state: State) -> dict[str, AIMessage]:
    print("get_response ", state["messages"])
    res = llm.invoke(state["messages"])
    return {"messages": res}


def get_tool_response(state: State) -> dict[str, list[ToolMessage]]:
    tool_calls = state["messages"][-1].tool_calls
    print(f"state: {state["messages"]}")
    ret = []
    for tool_call in tool_calls:
        print(tool_call)
        tool_name = tool_call["name"]
        args = tool_call["args"]
        tool_id = tool_call["id"]
        ret.append(ToolMessage(content=eval(tool_name)(**args), tool_call_id=tool_id))
    return {"messages": ret}


def relpy_or_end(state: State) -> Literal["get_response", END]:
    if state["messages"][-1].content == "exit":
        return END
    return "get_response"


def user_or_tool_call(state: State) -> Literal["get_user_input", "get_tool_response"]:
    if state["messages"][-1].tool_calls:
        return "get_tool_response"
    print("Assistant:", state["messages"][-1].content)
    return "get_user_input"


workflow.add_node("get_user_input", get_user_input)
workflow.add_node("get_response", get_response)
workflow.add_node("get_tool_response", get_tool_response)

workflow.add_edge(START, "get_user_input")
workflow.add_conditional_edges("get_user_input", relpy_or_end)
workflow.add_conditional_edges("get_response", user_or_tool_call)
workflow.add_edge("get_tool_response", "get_response")

app = workflow.compile()

# app.get_graph().draw_mermaid_png(output_file_path="1.png")

for event in app.stream(
        {"messages": [SystemMessage(content="You are a helpful assistant.")]}
):
    print(event, end="\n\n")
    pass
