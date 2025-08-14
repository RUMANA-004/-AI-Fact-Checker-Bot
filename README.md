# AI Fact-Checker Bot 

## Overview

The AI Fact-Checker Bot verifies claims using web search and structured reasoning. It is built with Python, Streamlit, and optionally LangGraph for Retrieval-Augmented Generation (RAG).

## Features

* **Streamlit Web UI** for interactive claim checking
* **5-step fact-checking chain**

  1. Initial Response
  2. Assumption Extraction
  3. Verification Loop
  4. Evidence Gathering
  5. Final Synthesis
* **Web Search Integration** (DuckDuckGo or fallback)
* **CLI Mode** for quick checks
* Optional **RAG pipeline** with LangGraph

## Installation

1. Clone this repository:

```bash
git clone <repo-url>
cd <repo-folder>
```

2. Create and activate a Python environment:

```bash
conda create -n factbot python=3.10
conda activate factbot
```

3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the CLI

```bash
python src/cli.py
```

## Running the Streamlit App

```bash
streamlit run src/ui/streamlit_app.py
```

Then open the displayed URL in your browser.

## Example Claims to Test

* The capital of France is Paris
* Mount Everest is the tallest mountain in the world
* NASA landed a rover on Mars in 2021
* Climate change is caused by human activities

## RAG Application 

For advanced fact-checking using your own documents:

```bash
python src/rag/rag_graph.py
```

Add knowledge files in `src/rag/knowledge/` before running.

## License

MIT
