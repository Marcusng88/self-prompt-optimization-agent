from pathlib import Path
import shutil

_TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"

_PROMPT_FILES = [
    "working_instruction_prompt.py",
    "user_profile.py",
]


def _ensure_prompt_files() -> None:
    for filename in _PROMPT_FILES:
        target = Path(__file__).resolve().parent / filename
        if target.exists():
            continue
        source = _TEMPLATES_DIR / filename
        if source.exists():
            shutil.copyfile(source, target)


_ensure_prompt_files()
