import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator, validate

ROOT = Path(__file__).resolve().parents[1]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class NativeAgentContractTests(unittest.TestCase):
    def test_json_documents_parse(self):
        for path in ("config/category_direction.json", "config/format_specification.json",
                     "config/database_category_mapping.json", "schemas/input.schema.json",
                     "schemas/output.schema.json"):
            with self.subTest(path=path):
                load_json(path)

    def test_schemas_are_valid_draft_2020_12(self):
        Draft202012Validator.check_schema(load_json("schemas/input.schema.json"))
        Draft202012Validator.check_schema(load_json("schemas/output.schema.json"))

    def test_seven_canonical_categories_and_legacy_mapping(self):
        categories = load_json("config/category_direction.json")["categories"]
        mapping = load_json("config/database_category_mapping.json")["mappings"]
        self.assertEqual(len(categories), 7)
        self.assertEqual(len({x["category_id"] for x in categories}), 7)
        self.assertEqual(len({x["category_slug"] for x in categories}), 7)
        self.assertEqual({(x["category_id"], x["category_slug"]) for x in categories},
                         {(x["canonical_id"], x["slug"]) for x in mapping})

    def test_two_formats_and_2k_export_dimensions(self):
        formats = load_json("config/format_specification.json")["allowed_formats"]
        self.assertEqual(set(formats), {"single_image", "story"})
        self.assertEqual(formats["single_image"]["generation_canvas"]["width_px"], 2048)
        self.assertEqual(formats["single_image"]["generation_canvas"]["height_px"], 2560)
        self.assertEqual(formats["single_image"]["canvas"], {"width_px": 1080, "height_px": 1350})
        self.assertEqual(formats["story"]["generation_canvas"]["width_px"], 1440)
        self.assertEqual(formats["story"]["generation_canvas"]["height_px"], 2560)
        self.assertEqual(formats["story"]["canvas"], {"width_px": 1080, "height_px": 1920})

    def test_input_schema_accepts_minimum_valid_brief(self):
        validate({"topic": "iPhone camera features", "format": "single_image"},
                 load_json("schemas/input.schema.json"))

    def test_output_contract_has_exactly_ten_top_level_keys(self):
        schema = load_json("schemas/output.schema.json")
        expected = ["template_version", "brand", "request", "product", "creative",
                    "copywriting", "format_specification", "assets", "compliance", "quality_control"]
        self.assertEqual(list(schema["properties"]), expected)
        self.assertFalse(schema["additionalProperties"])

if __name__ == "__main__":
    unittest.main()
