'''from langsmith import evaluate, Client

# 1. Create and/or select your dataset
client = Client()
dataset_name = "store-hours-eval"

# 2. Define an evaluator
def exact_match(outputs: dict, reference_outputs: dict) -> bool:
    return outputs == reference_outputs

# 3. Run an evaluation
# For more info on evaluators, see: https://docs.langchain.com/langsmith/evaluation-concepts

# To evaluate an LCEL chain, replace lambda with chain.invoke
# To evaluate a LangGraph graph, replace lambda with graph.invoke
evaluate(
    lambda x: x: {"answer": app.invoke({"question": x["question"]})["answer"]},
    # chain.invoke
    # graph.invoke
    data=dataset_name,
    evaluators=[exact_match],
    experiment_prefix="store-hours-eval experiment"
)'''


from langsmith import evaluate, Client
from graph import app  # <-- add this

client = Client()
dataset_name = "store-hours-eval"

# Evaluator comparing the “expected” field vs your agent output
def exact_match(outputs: dict, reference_outputs: dict) -> bool:
    return outputs == reference_outputs

# Replace lambda with your LangGraph app
evaluate(
    lambda x: {"answer": app.invoke({"question": x["question"]})["answer"]},
    data=dataset_name,
    evaluators=[exact_match],
    experiment_prefix="store-hours-eval"
)
