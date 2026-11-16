import argparse
import json
from pathlib import Path

from src.generator import generate


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a validated Instagram image prompt JSON draft.")
    parser.add_argument("--input", default="inputs/request.example.json", help="Path to request JSON.")
    parser.add_argument("--output", default="outputs/latest.json", help="Path for generated JSON.")
    args = parser.parse_args()

    request = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = generate(request)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Validated prompt output written to {output_path}")
    print(f"Editorial status: {result['quality_control']['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
