from langgraph.func import task, entrypoint
from langgraph.types import Command, interrupt
from langgraph.checkpoint.memory import MemorySaver

print("dddddddd")


@task
def step_1():
    print("---Step 1---")
    pass

@task
def human_feedback(ddd):
    print("---human_feedback---")
    # feedback = interrupt("Please provide feedback:")
    return {"user_feedback": "sss"}

@task
def judge():
    print("---judge---")
    feedback = interrupt("Please judge feedback:")
    return "ok" in feedback

@task
def step_3():
    print("---Step 3---")
    pass


# builder = StateGraph(State)
# builder.add_node("step_1", step_1)
# builder.add_node("human_feedback", human_feedback)
# builder.add_node("step_3", step_3)
# builder.add_edge(START, "step_1")
# builder.add_edge("step_1", "human_feedback")
# builder.add_edge("human_feedback", "step_3")
# builder.add_edge("step_3", END)
#
# # Set up memory
# memory = MemorySaver()
#
# # Add
# graph = builder.compile(checkpointer=memory)

@entrypoint(checkpointer = MemorySaver())
def graph(ii:str):
    step_1()
    human_feedback(ddd=111)
    if judge():
        human_feedback(ddd=222)
    else:

        step_3()
# View
# Input
initial_input = {"input": "hello world"}

# Thread
thread = {"configurable": {"thread_id": "1"}}

# Run the graph until the first interruption
# Continue the graph execution
# for event in graph.stream(initial_input, thread, stream_mode="updates"):
#     print(event)
#     print("\n")
#
# # Continue the graph execution
# for event in graph.stream(
#     Command(resume="go to step 3!"), thread, stream_mode="updates"
# ):
#     print(event)
#     print("\n")
# graph=workflow
# print("dddd")
for event in graph.stream(initial_input, thread):#
    print(event)
    print("\n")

for event in graph.stream(Command(resume="ok"), thread, stream_mode="updates"):
    print(event)
    print("\n")