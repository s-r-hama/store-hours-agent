🏪 Store Hours Agent — LangGraph + LangSmith Evaluation

This project implements a simple store-hours question-answering agent using LangGraph and evaluates it using LangSmith.

It demonstrates the full workflow of:

Building a multi-step LLM workflow with LangGraph

Creating and evaluating datasets inside LangSmith

Running experiments in both the UI and SDK

Debugging and improving LLM applications using traces and evaluations

This repository was created as part of a technical exercise showcasing practical knowledge of LangChain tooling.


📦 Features

Extracts store names from natural-language questions

Looks up store hours from structured JSON data

Generates a natural response such as “TKMaxx is open from 09:00 to 18:00”

Uses LangGraph to orchestrate the agent workflow

Uses LangSmith to evaluate performance

Includes a programmatic evaluation using langsmith.evaluate()


🧱 Architecture Overview

The application is built using LangGraph, which defines a small state machine with three nodes:

[extract_store] → [lookup_hours] → [answer] → END

1. extract_store

Uses an LLM (gpt-4o-mini) to extract the store name from the user’s question.

2. lookup_hours

Finds store hours from the JSON file in data/stores.json.

3. answer

Returns the final natural-language response.

All nodes operate on a shared StoreState.

This demonstrates the key LangGraph concepts:

Stateful workflow

Deterministic edges

LLM tool nodes

Node-by-node traceability inside LangSmith

📁 Repository Structure
store-hours-agent/
│
├── graph.py               # LangGraph workflow
├── evaluate.py            # LangSmith SDK evaluation
├── data/
│   └── stores.json        # Store hours data
└── README.md              # Documentation

🧪 Dataset & Evaluation

A dataset was created in the LangSmith UI:

question	expected
What time does TK Maxx open?	09:00
When does Tesco close?	22:00
What time does Primark open?	10:00

Then an evaluation was run using:

✔ LangSmith UI

Experiment type: Custom Code
Runner function invoked the LangGraph app.
Evaluator: Exact Match comparing output against expected.

✔ LangSmith SDK (evaluate.py)

Used:

from langsmith import evaluate


This triggered a full experiment and produced a link to LangSmith with:

per-example results

traces

scoring

pass/fail summary

▶️ Running the Agent Locally

You can run the workflow directly:

python3 graph.py


Example output:

Tkmaxx is open from 09:00 to 18:00.

▶️ Running the LangSmith Evaluation
1. Add your environment variables:
export OPENAI_API_KEY="your-openai-key"
export LANGSMITH_API_KEY="your-langsmith-key"
export LANGSMITH_PROJECT="store-hours-eval"


Be careful of “smart quotes” — use regular ASCII quotes only.

2. Run the evaluation:
python3 evaluate.py


You will receive a link to the LangSmith experiment, where you can view:

Inputs

Outputs

Expected values

Scoring results

Full LangGraph traces for each run



🐞 Debugging Journey (What I Learned)

During development, the evaluation initially failed with:

UnicodeEncodeError: 'ascii' codec can't encode character '\u201d'

Root cause

The OPENAI_API_KEY environment variable contained a smart quote (from macOS autocorrect).

Fix

Replace with a plain quote:

export OPENAI_API_KEY="sk-xxxxx"


This was a good real-world example of:

Debugging LangSmith trace errors

Understanding LangGraph node failures

Identifying encoding issues in API headers



🚀 Future Enhancements

Add fuzzy matching for store names

Add multiple branches for different question types

Integrate a vector database for store metadata

Add more sophisticated evaluators (LLM-as-a-judge)

Support multi-store operations (“Compare Tesco and TkMaxx hours”)