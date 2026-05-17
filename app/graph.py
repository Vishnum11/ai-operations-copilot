from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1:8b")

class AgentState(TypedDict):
    user_message: str
    route: str
    response: str

def router_node(state: AgentState):
    message = state["user_message"].lower()

    if "appointment" in message or "book" in message or "schedule" in message:
        route = "scheduler"
    elif "customer" in message or "billing" in message or "crm" in message:
        route = "crm"
    else:
        route = "support"

    return {
        "user_message": state["user_message"],
        "route": route,
        "response": ""
    }

def support_agent(state: AgentState):
    prompt = f"""
    You are a helpful AI support assistant.

    Customer message:
    {state["user_message"]}
    """

    result = llm.invoke(prompt)

    return {
        "user_message": state["user_message"],
        "route": state["route"],
        "response": result.content
    }

def scheduler_agent(state: AgentState):
    prompt = f"""
    You are an AI scheduling assistant.

    Customer message:
    {state["user_message"]}
    """

    result = llm.invoke(prompt)

    return {
        "user_message": state["user_message"],
        "route": state["route"],
        "response": result.content
    }

def crm_agent(state: AgentState):
    prompt = f"""
    You are a CRM assistant helping organize customer issues.

    Customer message:
    {state["user_message"]}
    """

    result = llm.invoke(prompt)

    return {
        "user_message": state["user_message"],
        "route": state["route"],
        "response": result.content
    }

def route_decision(state: AgentState):
    return state["route"]

graph_builder = StateGraph(AgentState)

graph_builder.add_node("router", router_node)
graph_builder.add_node("support", support_agent)
graph_builder.add_node("scheduler", scheduler_agent)
graph_builder.add_node("crm", crm_agent)

graph_builder.set_entry_point("router")

graph_builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "support": "support",
        "scheduler": "scheduler",
        "crm": "crm"
    }
)

graph_builder.add_edge("support", END)
graph_builder.add_edge("scheduler", END)
graph_builder.add_edge("crm", END)

app_graph = graph_builder.compile()

def run_agent(message: str):
    result = app_graph.invoke({
        "user_message": message,
        "route": "",
        "response": ""
    })

    return result["response"]