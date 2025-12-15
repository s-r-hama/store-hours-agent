
# Store Hours Agent (LangGraph + LangSmith Evaluation)

This project implements a simple LangGraph workflow that answers questions about store opening and closing hours.
It also demonstrates how to evaluate a LangGraph application using LangSmith through both the UI and the SDK.


# 1. Project Structure

```
store-hours-agent/
│
├── graph.py               # LangGraph workflow
├── evaluate.py            # LangSmith SDK evaluation
├── data/
│   └── stores.json        # Store hours data
└── README.md              # Documentation

```

# 2. Overview

The agent receives a natural-language question such as:

What time does TK Maxx close?

It performs three steps:

1. Extracts the store name using an LLM

2. Looks up the store’s hours from JSON data

3. Returns a formatted answer

The workflow is implemented using LangGraph, which allows defining stateful, multi-step logic with nodes and edges.


# 3. LangGraph Workflow

The graph contains the following nodes:

extract_store → lookup_hours → answer → END



3.1  extract_store

Uses the LLM to extract a store name from the user question.

3.2 lookup_hours

Searches for the store in data/stores.json.

3.3 answer

Constructs the final human-readable response.

3.4 Shared State

All nodes operate on a shared state dictionary (StoreState).


# 4. Dataset (LangSmith)

A dataset named store-hours-eval was created in the LangSmith UI.

| question                     | expected |
| ---------------------------- | -------- |
| What time does TK Maxx open? | 09:00    |
| When does Tesco close?       | 22:00    |
| What time does Primark open? | 10:00    |


# 5. Running the Agent Locally

Run:
``` python3 graph.py ```


Example output:
``` Tkmaxx is open from 09:00 to 18:00. ```


# 6. Running the Evaluation (LangSmith SDK)

6.1 Environment variables
export OPENAI_API_KEY="your-openai-key"
export LANGSMITH_API_KEY="your-langsmith-key"
export LANGSMITH_PROJECT="store-hours-eval"


6.2 Run the evaluation script
``` python3 evaluate.py ```


The script will output a link to the LangSmith UI where you can inspect:

* Inputs

* Model outputs

* Expected outputs

* Scores

* Full LangGraph execution traces




# 7. Debugging Notes

During development, an evaluation failure occurred:

UnicodeEncodeError: 'ascii' codec can't encode character '\u201d'

Cause

The API key environment variable contained a “smart quote” character:

``` export OPENAI_API_KEY=”sk-123” ```

Fix

Replace with standard ASCII quotes:

``` export OPENAI_API_KEY="sk-123" ```


This kind of real-world environment/configuration issue is something LangSmith helps surface quickly.

# 8. Key Concepts Demonstrated

* Building a structured LangGraph workflow

* Using LangSmith datasets for evaluation

* Running an evaluation through the UI and SDK

* Inspecting traces for debugging

* Handling model, state, and configuration errors