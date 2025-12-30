from typing import TypedDict, Annotated, Literal

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.func import entrypoint, task
from langgraph.graph import StateGraph, add_messages, START, END
from langgraph.types import interrupt, Command


def task1(input_):
    print(f"task1: {input_}")
    print("Task 1")


def task2() -> Literal["task1", "task2"]:
    print("Task 2")
    value = interrupt("please input value")
    if "ok" in value:
        return "task1"
    else:
        return "task3"


def task3():
    print("Task 3")


def task4():
    print("Task 4")


class State(TypedDict):
    messages: Annotated[list, add_messages]


workflow = StateGraph(State)

workflow.add_node(task1)
workflow.add_node(task2)
workflow.add_node(task3)
workflow.add_node(task4)

workflow.add_edge(START, "task1")
workflow.add_edge("task1", "task2")
workflow.add_edge("task3", "task4")
workflow.add_edge("task4", END)
config = {"configurable": {"thread_id": "1"}}

inputs = {
    "messages": "你好"
}
print("------")
graph = workflow.compile()

for event in graph.stream(inputs,config):
    print("event",event)

# print("++++++++")
# workflow.stream(Command(resume="ok"),thread=thread)
