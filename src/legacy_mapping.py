import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def build_legacy_webhook_preview(output: dict[str, Any], image_url: str | None = None,
                                 scheduled_date: str | None = None,
                                 scheduled_time: str | None = None) -> dict[str, Any]:
    mapping_path = ROOT / "config/database_category_mapping.json"
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    primary = output["request"]["primary_category"]
    match = next((item for item in mapping["mappings"] if item["canonical_id"] == primary["category_id"]), None)
    if match is None or match["slug"] != primary["category_slug"]:
        raise ValueError("Category ID/slug pair is not present in the approved legacy mapping.")
    missing = [
        name for name, value in (
            ("image_url", image_url), ("date", scheduled_date), ("time", scheduled_time)
        ) if not value
    ]
    return {
        "status": "not_insertable" if missing else "preview_only",
        "table": "public.make_webhook",
        "category_id_legacy_value": match["legacy_category_value"],
        "caption": output["copywriting"]["caption"],
        "image_url": image_url,
        "date": scheduled_date,
        "time": scheduled_time,
        "missing_required_fields": missing,
        "write_performed": False,
        "note": "This is a compatibility preview only. No database connection or write is performed.",
    }
