#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$ROOT_DIR/.venv"
TEMPLATES_DIR="$ROOT_DIR/src/prompts/templates"
PROMPTS_DIR="$ROOT_DIR/src/prompts"

if [ ! -d "$VENV_DIR" ]; then
  python -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

pip install -r "$ROOT_DIR/requirements.txt"

if [ ! -f "$ROOT_DIR/.env" ]; then
  cp "$ROOT_DIR/.env.example" "$ROOT_DIR/.env"
  echo "Created .env from .env.example. Please add your keys."
fi

if [ -d "$TEMPLATES_DIR" ]; then
  for template in "$TEMPLATES_DIR"/*.py; do
    [ -e "$template" ] || continue
    target="$PROMPTS_DIR/$(basename "$template")"
    if [ ! -f "$target" ]; then
      cp "$template" "$target"
    fi
  done
fi

echo "Run: langgraph dev --allow-blocking"
