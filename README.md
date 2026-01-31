# self-prompt-optimization-agent

This agent is built on LangChain v1, observed via LangSmith, with integration of filesystem MCP servers using `langchain-mcp-adapters`. This project is for educational purposes to study how to build an agent that can self-evolve and learn over time.

## Quick start (Windows)
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
langgraph dev --allow-blocking
```

## Quick start (macOS/Linux)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
langgraph dev --allow-blocking
```

## One-command bootstrap
```bash
.\scripts\bootstrap.ps1
```

## Environment variables
Copy `.env.example` to `.env` and fill in your keys.

## Requirements
- Python 3.11+
- Node.js (for `npx` MCP filesystem server)

## Prompts (first-run initialization)
On first run, local prompt files are generated from templates in `src/prompts/templates/`.
If you want to reset your prompts, delete the local files and run the app (or `scripts/bootstrap.ps1`) again.

## MCP filesystem root
By default, the filesystem MCP server points to `src/prompts`. You can override this path with:
```
MCP_FILESYSTEM_ROOT=/path/to/your/prompts
```
