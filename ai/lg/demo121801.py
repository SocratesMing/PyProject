# 步骤1: 定义对话状态 - 记录流水线上的所有信息
from typing import TypedDict, Annotated, List
from langgraph.graph.message import add_messages
import operator

class AgentState(TypedDict):
    # 对话消息历史，这是实现多轮对话的基础
    messages: Annotated[List, add_messages]
    # 用户提出的原始问题
    user_query: str
    # 其他需要跟踪的槽位信息，例如订单号
    order_id: str

# 步骤2: 构建包含中断机制的工具
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.prebuilt import ToolNode, tools_condition

# 假设我们有一个需要人工确认的“创建工单”工具
def create_ticket(order_id: str, issue: str) -> str:
    """这是一个需要人工确认的危险操作。实际调用外部API。"""
    # 这里可以编写真实的API调用逻辑
    return f"工单已为订单 {order_id} 创建，问题：{issue}"

# 关键：在工具节点中加入中断(interrupt)以等待人工确认
def human_approval_tool_node(state: AgentState):
    from langgraph import interrupt
    # 1. 暂停图执行，将工具调用信息呈现给人工审批界面
    approval = interrupt({
        "tool": "create_ticket",
        "parameters": {"order_id": state["order_id"], "issue": state["user_query"]},
        "message": "是否批准创建工单？"
    })
    # 2. 根据人工的输入决定下一步
    if approval == "APPROVE":
        # 执行真正的工具函数
        result = create_ticket(state["order_id"], state["user_query"])
        return {"messages": [("assistant", f"操作已执行：{result}")]}
    else:
        return {"messages": [("assistant", "用户取消了工单创建操作。")]}

# 步骤3: 构建主图（工作流）
builder = StateGraph(AgentState)

# 添加节点：包括LLM推理节点、普通工具节点和带人工确认的工具节点
builder.add_node("llm_agent", your_llm_agent_function)  # 你的LLM代理逻辑
builder.add_node("approved_tool", human_approval_tool_node)  # 带人工确认的工具
builder.add_node("normal_tools", ToolNode([normal_tool1, normal_tool2]))  # 普通工具集

# 设置路由逻辑：LLM决定下一步是调用普通工具、需要确认的工具，还是直接回复
def route_after_llm(state: AgentState):
    # 这里根据LLM的输出或state的内容决定路由
    # 例如，如果检测到用户想创建工单，则路由到人工确认节点
    if "create_ticket" in state["user_query"]:
        return "approved_tool"
    else:
        return "normal_tools"

builder.add_conditional_edges(
    "llm_agent",
    route_after_llm,
    {"approved_tool": "approved_tool", "normal_tools": "normal_tools", END: END}
)
builder.add_edge("approved_tool", "llm_agent")
builder.add_edge("normal_tools", "llm_agent")
builder.add_edge(START, "llm_agent")

# 启用检查点，这是支持多轮对话和中断恢复的关键[citation:9]
memory = SqliteSaver.from_conn_string(":memory:")
graph = builder.compile(checkpointer=memory)