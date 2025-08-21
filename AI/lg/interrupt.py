import time

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.func import entrypoint, task
from langgraph.types import interrupt, Command


@task
def task1():
    print("Task 1")
    time.sleep(2)

@task
def task2()->bool:
    print("Task 2")
    value = interrupt("please input value")
    return "ok" in  value

@task
def task3():
    print("Task 3")

@task
def task4():
    print("Task 4")


@entrypoint(checkpointer=InMemorySaver())
def workflow(input_):
    print("Workflow 1",input_)
    task1()
    # if task2():
    #     print("True")
    #     task1()
    # else:
    #     print("False")
    #     task3()
    task4()

config = {"configurable": {"thread_id": "1"}}
inputs={
    "messages":"你好"
}
print("------")
for event in workflow.stream(inputs,config):
    print("event",event)

# print("++++++++")
# workflow.stream(Command(resume="ok"),thread=thread)