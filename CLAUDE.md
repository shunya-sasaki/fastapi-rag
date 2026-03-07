# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

FastAPI-based RAG (Retrieval-Augmented Generation) API server. This is the application code for the API layer; infrastructure (ChromaDB, PostgreSQL) is managed by the parent `docker-rag` repo via Docker Compose.

## Architecture

- **Package**: `ragapi` — src-layout under `src/ragapi/`
- **Modules**:
  - `app/` — FastAPI application (currently scaffolded)
  - `models/` — Data models with pydantic BaseModel
  - `db/` — Database layer with sqlmodel
  - `utils/` — Shared utilities: `CustomLogger` (colored rotating file logger), `GitVersion` (git-based versioning/release), `FormatConverter` (string format conversion)

## Dependencies & Tooling

- **Python**: >=3.11
- **Package manager**: [uv](https://github.com/astral-sh/uv)
- **Build system**: Hatchling with `uv-dynamic-versioning` (version derived from git tags)
- **Core deps**: `fastapi[all]`, `sqlmodel`

## Commands

```bash
# Install dependencies
uv sync

# Run dev server
uv run fastapi dev src/ragapi/app/main.py

# Run tests
uv run pytest

# Run a single test
uv run pytest tests/test_foo.py::test_bar -v

# Lint
uv run ruff check src/

# Format
uv run ruff format src/

# Build package (must be on main with a release commit)
uv build
```

## Code Style

Configured in `pyproject.toml`:

- **Ruff**: line-length 79, lint rules `D` (docstrings, Google convention), `E`, `F`, `C90`, `I` (isort)
- **isort**: force single-line imports, first-party package `ragapi`
- **Black**: line-length 79 (Ruff format is primary)
- **Docstrings**: Google style convention

## Versioning

Uses `uv-dynamic-versioning` — version is derived from git tags at build time. The `GitVersion` utility class handles release/tag workflows. Semantic versioning with `v`-prefixed tags (e.g., `v1.0.0`).

## APIs

### File upload

- **Endpoint**: `POST /api/upload`
- **Request**: multipart/form-data with file field `file`
- **Description**: Upload a file for processing
  Extract metadata (filename and page number) and save to database

### RAG Chat response

- **Endpoint**: `POST /api/rag`
- **Request**: JSON with `query` field (user input) and ref file index numbers and preset prompts
- **Description**: Generate a response based on the query and file context. Uses RAG

## Data models

- Data model is defined in the models directory
- Use pydantic BaseModel
- Use model_dict and set alias to use format_converter that is defined in utils
