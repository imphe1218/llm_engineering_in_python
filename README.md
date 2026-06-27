# LLM Engineering in Python

A uv-managed Python project for LLM engineering work — structured as a proper package (not notebooks), with the same core libraries as the companion `llm_engineering` course repo.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12.12 (see `.python-version`).

```powershell
uv sync
```

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

## Project layout

```
llm_engineering_in_python/
├── pyproject.toml
├── .python-version
├── src/
│   └── llm_engineering_in_python/
│       └── __init__.py
└── tests/
    └── test_main.py
```

## Usage

Run the CLI entry point:

```powershell
uv run llm-engineering-in-python
```

Run tests:

```powershell
uv run pytest
```

## Environment variables

Copy `.env.example` to `.env` and add your API keys as needed (OpenAI, Anthropic, etc.).

## Web stack

This project includes **FastAPI** and **Uvicorn** for building HTTP APIs, and **Gradio** for quick UIs — use them when you need a web interface without Jupyter.
