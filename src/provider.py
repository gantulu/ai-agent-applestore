import json
import os
import urllib.error
import urllib.request
from typing import Any


class ProviderError(RuntimeError):
    pass


def _to_openai_schema(value: Any) -> Any:
    """Remove local JSON Schema metadata and lower const to enum for API compatibility."""
    if isinstance(value, list):
        return [_to_openai_schema(item) for item in value]
    if not isinstance(value, dict):
        return value
    result = {}
    for key, item in value.items():
        if key in ("$schema", "$id", "title", "minLength", "default"):
            continue
        if key == "const":
            result["enum"] = [item]
            continue
        result[key] = _to_openai_schema(item)
    return result


class OpenAIResponsesProvider:
    """Small standard-library client for the OpenAI Responses API."""

    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY", "").strip()
        self.model = os.getenv("OPENAI_MODEL", "gpt-6-luna").strip()
        self.base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        self.timeout = int(os.getenv("OPENAI_TIMEOUT_SECONDS", "90"))
        if not self.api_key:
            raise ProviderError("OPENAI_API_KEY is required. Add it as a GitHub Actions secret.")

    def generate(self, instructions: str, request: dict[str, Any], schema: dict[str, Any]) -> str:
        payload = {
            "model": self.model,
            "instructions": instructions,
            "input": json.dumps(request, ensure_ascii=False),
            "text": {
                "format": {
                    "type": "json_schema",
                    "name": "apple_instagram_prompt_output",
                    "strict": True,
                    "schema": _to_openai_schema(schema),
                }
            },
        }
        body = json.dumps(payload).encode("utf-8")
        http_request = urllib.request.Request(
            f"{self.base_url}/responses",
            data=body,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(http_request, timeout=self.timeout) as response:
                response_data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:1200]
            raise ProviderError(f"OpenAI API returned HTTP {exc.code}: {detail}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            raise ProviderError(f"Could not reach the OpenAI API: {exc}") from exc
        except json.JSONDecodeError as exc:
            raise ProviderError("OpenAI API returned an invalid JSON response.") from exc

        if response_data.get("status") not in (None, "completed"):
            raise ProviderError(f"OpenAI response did not complete: {response_data.get('status')}")
        output_text = response_data.get("output_text")
        if not output_text:
            fragments = []
            for item in response_data.get("output", []):
                if item.get("type") != "message":
                    continue
                for content in item.get("content", []):
                    if content.get("type") == "output_text":
                        fragments.append(content.get("text", ""))
                    elif content.get("type") == "refusal":
                        raise ProviderError("The model refused the generation request.")
            output_text = "".join(fragments)
        if not output_text:
            raise ProviderError("The API response did not contain structured output text.")
        return output_text
