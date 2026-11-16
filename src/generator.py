import json
from typing import Any

from src.config_loader import load_project_config
from src.prompt_builder import build_instructions
from src.provider import OpenAIResponsesProvider
from src.validator import validate


AFFILIATION = (
    "Independent Apple-product content project. This account is not represented as Apple-owned, "
    "Apple-operated, endorsed, or Apple-authorized unless separately verified and expressly permitted."
)


def _category_record(value: dict[str, Any], categories: dict[str, Any]) -> dict[str, str]:
    for item in categories["categories"]:
        if value.get("category_id") == item["category_id"] or value.get("category_slug") == item["category_slug"]:
            return {
                "category_id": item["category_id"],
                "category_slug": item["category_slug"],
                "category_name": item["category_name"],
            }
    raise ValueError("Model returned a category outside the canonical seven-category taxonomy.")


def _apply_runtime_guards(output: dict[str, Any], request: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    categories = config["categories"]
    formats = config["formats"]["allowed_formats"]
    requested_category = request.get("category", "auto")
    primary = _category_record(output["request"]["primary_category"], categories)
    if requested_category not in (None, "", "auto"):
        expected = _category_record(
            {"category_id": requested_category, "category_slug": requested_category}, categories
        )
        if primary["category_slug"] != expected["category_slug"]:
            raise ValueError("Model category does not match the explicitly requested category.")
    output["request"]["primary_category"] = primary

    secondary = output["request"].get("secondary_category")
    if secondary is not None:
        secondary = _category_record(secondary, categories)
        if secondary["category_slug"] == primary["category_slug"]:
            raise ValueError("Primary and secondary categories must be different.")
        output["request"]["secondary_category"] = secondary

    selected_format = formats[request["format"]]
    expected_generation = selected_format["generation_canvas"]
    expected_export = selected_format["canvas"]
    output["format_specification"] = {
        "format_id": selected_format["format_id"],
        "placement": selected_format["placement"],
        "aspect_ratio": selected_format["aspect_ratio"],
        "generation_canvas": expected_generation,
        "export_canvas": {
            "width_px": expected_export["width_px"],
            "height_px": expected_export["height_px"],
        },
        "safe_area": selected_format["layout_guidance"]["safe_area"],
    }

    output["template_version"] = "1.0.0"
    output["brand"] = {
        "project_name": "Apple Instagram Content Project",
        "market": "MY",
        "platform": "instagram",
        "content_locale": "en-MY",
        "affiliation_statement": AFFILIATION,
    }
    output["request"].update({
        "topic": request["topic"],
        "objective": request.get("objective", "awareness"),
        "audience": request.get("audience", "Apple users and prospective buyers in Malaysia"),
    })
    output["product"]["product_name"] = request.get("product_name") or output["product"].get("product_name")
    for field in ("model", "generation", "configuration"):
        source_field = {"model": "product_model", "generation": "product_generation", "configuration": "product_configuration"}[field]
        if request.get(source_field):
            output["product"][field] = request[source_field]

    output["product"]["evidence"] = [
        {"claim": fact, "source_url": None, "checked_at": None}
        for fact in request.get("supplied_facts", [])
    ]
    output["assets"]["reference_assets"] = request.get("asset_urls", [])
    rights_pending = bool(request.get("asset_urls"))
    output["assets"]["usage_rights_status"] = "pending" if rights_pending else "not_required"
    output["compliance"]["brand_affiliation_checked"] = True
    output["compliance"]["human_review_required"] = True
    output["compliance"]["asset_rights_status"] = "pending" if rights_pending else "not_required"

    claims = output["compliance"].get("factual_claims", [])
    has_claims = bool(claims or request.get("product_name") or request.get("supplied_facts") or request.get("source_urls"))
    output["compliance"]["source_verification_status"] = "unverified" if has_claims else "not_required"
    warnings = list(output["compliance"].get("warnings", []))
    if has_claims:
        warnings.append("Factual claims and supplied sources have not been independently verified by this runtime.")
    if rights_pending:
        warnings.append("Reference asset usage rights require human confirmation.")
    warnings.append("Human approval is mandatory before any publication.")
    output["compliance"]["warnings"] = list(dict.fromkeys(warnings))

    checks = {
        "category_format": primary["category_slug"] in {item["category_slug"] for item in categories["categories"]},
        "locale": output["brand"]["content_locale"] == "en-MY",
        "generation_dimensions": (
            output["format_specification"]["generation_canvas"]["width_px"] == expected_generation["width_px"]
            and output["format_specification"]["generation_canvas"]["height_px"] == expected_generation["height_px"]
        ),
        "factual_claims": not has_claims,
        "brand_safety": output["brand"]["affiliation_statement"] == AFFILIATION,
        "asset_rights": not rights_pending,
    }
    output["quality_control"]["checks"] = checks
    output["quality_control"]["schema_validation"] = "pending"
    output["quality_control"]["human_approval_required"] = True
    output["quality_control"]["status"] = "needs_human_review" if not all(checks.values()) else "review_ready"
    return output


def generate(request: dict[str, Any], provider: Any | None = None) -> dict[str, Any]:
    config = load_project_config()
    validate(request, config["input_schema"], "Input")
    instructions = build_instructions(config, request)
    provider = provider or OpenAIResponsesProvider()
    raw = provider.generate(instructions, request, config["output_schema"])
    try:
        output = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Model output was not valid JSON: {exc}") from exc
    if not isinstance(output, dict):
        raise ValueError("Model output must be a single JSON object.")
    output = _apply_runtime_guards(output, request, config)
    validate(output, config["output_schema"], "Output")
    output["quality_control"]["schema_validation"] = "passed"
    validate(output, config["output_schema"], "Final output")
    return output
