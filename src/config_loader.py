import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative_path: str) -> dict[str, Any]:
    path = ROOT / relative_path
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise ValueError(f"Required project file is missing: {relative_path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {relative_path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object in {relative_path}")
    return value


def load_project_config() -> dict[str, Any]:
    return {
        "master_prompt": (ROOT / "prompts/master_prompt.md").read_text(encoding="utf-8"),
        "categories": load_json("config/category_direction.json"),
        "formats": load_json("config/format_specification.json"),
        "category_mapping": load_json("config/database_category_mapping.json"),
        "input_schema": load_json("schemas/input.schema.json"),
        "output_schema": load_json("schemas/output.schema.json"),
    }
