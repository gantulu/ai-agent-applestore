from typing import Any

from jsonschema import Draft202012Validator


class ContractValidationError(ValueError):
    pass


def validate(instance: dict[str, Any], schema: dict[str, Any], label: str) -> None:
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.absolute_path))
    if errors:
        details = []
        for error in errors[:10]:
            path = ".".join(str(part) for part in error.absolute_path) or "$"
            details.append(f"{path}: {error.message}")
        raise ContractValidationError(f"{label} validation failed: " + "; ".join(details))
