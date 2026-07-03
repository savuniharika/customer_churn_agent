from langgraph.graph import StateGraph, END

from graphs.state import ChurnState
from agents.risk_agent import risk_agent
from agents.explanation_agent import explanation_agent
from agents.priority_agent import priority_agent
from agents.strategy_agent import strategy_agent


# ---------------------------
# Risk Node
# ---------------------------
def risk_node(state: ChurnState):
    result = risk_agent(state["customer_data"])

    state["prediction"] = result["prediction"]
    state["confidence"] = result["confidence"]

    return state


# ---------------------------
# Explanation Node
# ---------------------------
def explanation_node(state: ChurnState):
    result = explanation_agent(state["customer_data"])

    state["explanation"] = result["explanation"]

    return state


# ---------------------------
# Priority Node
# ---------------------------
def priority_node(state: ChurnState):
    result = priority_agent(
        state["prediction"],
        state["confidence"]
    )

    state["priority"] = result["priority"]

    return state


# ---------------------------
# Strategy Node
# ---------------------------
def strategy_node(state: ChurnState):
    result = strategy_agent(
        state["prediction"],
        state["priority"]
    )

    state["strategy"] = result["strategy"]

    return state


# ---------------------------
# Build Graph
# ---------------------------
graph = StateGraph(ChurnState)

graph.add_node("Risk", risk_node)
graph.add_node("Explanation", explanation_node)
graph.add_node("Priority", priority_node)
graph.add_node("Strategy", strategy_node)

graph.set_entry_point("Risk")

graph.add_edge("Risk", "Explanation")
graph.add_edge("Explanation", "Priority")
graph.add_edge("Priority", "Strategy")
graph.add_edge("Strategy", END)

supervisor = graph.compile()
if __name__ == "__main__":

    sample_customer = {
        "age": 45,
        "gender": 1,
        "tenure_months": 24,
        "total_orders": 30,
        "avg_order_value": 550,
        "total_spent": 16500,
        "last_purchase_days": 40,
        "app_opens_last_30d": 8,
        "support_tickets": 4,
        "satisfaction_score": 5,
        "referrals": 1,
        "discount_usage": 1,
        "membership": 1
    }

    state = {
        "customer_data": sample_customer
    }

    result = supervisor.invoke(state)

    print(result)