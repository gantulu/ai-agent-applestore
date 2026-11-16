import unittest

from src.provider import _to_openai_schema


class ProviderSchemaTests(unittest.TestCase):
    def test_api_schema_removes_local_metadata_and_lowers_const(self):
        source = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "local-id",
            "title": "Local title",
            "type": "object",
            "properties": {
                "name": {"type": "string", "minLength": 1},
                "market": {"type": "string", "const": "MY"},
            },
            "required": ["name", "market"],
            "additionalProperties": False,
        }
        result = _to_openai_schema(source)
        self.assertNotIn("$schema", result)
        self.assertNotIn("$id", result)
        self.assertNotIn("title", result)
        self.assertNotIn("minLength", result["properties"]["name"])
        self.assertEqual(result["properties"]["market"]["enum"], ["MY"])
        self.assertNotIn("const", result["properties"]["market"])


if __name__ == "__main__":
    unittest.main()
