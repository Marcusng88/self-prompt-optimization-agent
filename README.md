# Self Prompt Optimization Agent

A LangGraph-based personal assistant that can improve its own behavior over time by maintaining two editable local prompt modules:

- `src/prompts/working_instruction_prompt.py`: the assistant operating manual
- `src/prompts/user_profile.py`: learned user preferences and context

The agent composes a system prompt from:

1. `src/meta_prompt.py`
2. `src/prompts/working_instruction_prompt.py`
3. `src/prompts/user_profile.py`

It also mounts tools from:

- MCP filesystem server (via `langchain-mcp-adapters`)
- Tavily web search (`langchain-tavily`)

The project is intended as an educational purpose for building self-improving agents with LangChain/LangGraph.

## Features

- Self-evolving prompt architecture with clear separation of concerns
- Prompt templates auto-copied on first run if local prompt files are missing
- File-based MCP tool integration for local prompt editing workflows
- Tavily search tool for web retrieval
- LangSmith-ready environment variable support
- LangGraph dev server support with exported `agent`

## Project Structure

```text
self-prompt-optimization-agent/
	langgraph.json
	pyproject.toml
	requirements.txt
	.env.example
	scripts/
		bootstrap.ps1
		bootstrap.sh
	src/
		agent.py
		meta_prompt.py
		config/
			model.py
			mcp.py
		prompts/
			__init__.py
			user_profile.py
			working_instruction_prompt.py
			templates/
				user_profile.py
				working_instruction_prompt.py
```

## Requirements

- Python 3.11+
- Node.js + `npx` (required for `@modelcontextprotocol/server-filesystem`)

## Environment Variables

Create a `.env` file from `.env.example` and set:

- `GOOGLE_API_KEY`: for Gemini models (if you use them)
- `LANGSMITH_API_KEY`: for LangSmith tracing/observability
- `TAVILY_API_KEY`: for Tavily search tool
- `MCP_FILESYSTEM_ROOT` (optional): override default MCP filesystem root

Default MCP root is `src/prompts`.

## Quick Start

### Windows (manual)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
# edit .env with your real keys
langgraph dev --allow-blocking
```

### macOS/Linux (manual)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env with your real keys
langgraph dev --allow-blocking
```

### Bootstrap Scripts

Windows:

```powershell
.\scripts\bootstrap.ps1
```

macOS/Linux:

```bash
./scripts/bootstrap.sh
```

The bootstrap scripts:

1. Create `.venv` if missing
2. Install dependencies from `requirements.txt`
3. Create `.env` from `.env.example` if missing
4. Copy prompt templates into `src/prompts` if missing

## How the Agent Works

### Runtime Assembly

In `src/agent.py`, the exported `agent` is created with:

- Model: `openai_model` from `src/config/model.py`
- Tools: `mcp_tools` + `TavilySearch`
- System prompt: concatenation of meta prompt + working instructions + user profile

`langgraph.json` points to this entry:

```json
{
	"graphs": {
		"agent": "./src/agent.py:agent"
	}
}
```

### Prompt Initialization Behavior

When `src/prompts/__init__.py` is imported, it ensures:

- `src/prompts/working_instruction_prompt.py` exists
- `src/prompts/user_profile.py` exists

If missing, each file is copied from `src/prompts/templates/`.

This lets you reset prompt state by deleting one or both local files and re-running.

## Customization

### Switch Model

Edit `src/config/model.py` to select your preferred model wiring. The repository currently defines both:

- OpenAI chat model
- Gemini chat model

### Change MCP Filesystem Scope

Set `MCP_FILESYSTEM_ROOT` in `.env` to any directory you want exposed to the MCP filesystem server.

### Evolve Prompt Behavior

Edit these two files to tune behavior over time:

- `src/prompts/working_instruction_prompt.py`
- `src/prompts/user_profile.py`

Keep prompts specific and testable to avoid bloated or contradictory instructions.

## Development Notes

- Primary graph config: `langgraph.json`
- Python packaging metadata: `pyproject.toml`
- Pinned runtime dependencies: `requirements.txt`
- Agent debug mode is currently enabled in `src/agent.py`

## Troubleshooting

- `npx` not found:
	Install Node.js and verify `npx --version` works.

- MCP tool startup issues:
	Confirm `@modelcontextprotocol/server-filesystem` can be launched through `npx` and that `MCP_FILESYSTEM_ROOT` is valid.

- Missing API key errors:
	Ensure `.env` is present and keys are populated.

- Prompt files not generated:
	Ensure `src/prompts/templates/` exists and import flow reaches `src/prompts/__init__.py`.

## License

This project is licensed under the terms in `LICENSE`.
