import json
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

model = ChatOpenAI(model="gpt-4o-mini")

# Load store hours
with open("data/stores.json") as f:
    STORE_DATA = json.load(f)


class StoreState(dict):
    question: str
    store: str
    hours: dict
    answer: str


# Node 1 — Extract store name using LLM
def extract_store_node(state: StoreState):
    prompt = (
    "Extract the store name from this question: "
    + state["question"]
    + ". Return only the store name, lowercased."
)


    resp = model.invoke(prompt)
    state["store"] = resp.content.strip()
    return state


# Node 2 — Lookup hours
def lookup_hours_node(state: StoreState):
    store = state["store"]
    state["hours"] = STORE_DATA.get(store, None)
    return state


# Node 3 — Answer the user
def answer_node(state: StoreState):
    if not state["hours"]:
        state["answer"] = f"Sorry, I don't have hours for {state['store']}."
        return state

    open_time = state["hours"]["open"]
    close_time = state["hours"]["close"]

    state["answer"] = (
        f"{state['store'].title()} is open from {open_time} to {close_time}."
    )
    return state


# Build LangGraph
graph = StateGraph(StoreState)
graph.add_node("extract_store", extract_store_node)
graph.add_node("lookup_hours", lookup_hours_node)
graph.add_node("answer", answer_node)

graph.set_entry_point("extract_store")
graph.add_edge("extract_store", "lookup_hours")
graph.add_edge("lookup_hours", "answer")
graph.add_edge("answer", END)

app = graph.compile()


if __name__ == "__main__":
    result = app.invoke({"question": "What time does tkmaxx close?"})
    print(result["answer"])
