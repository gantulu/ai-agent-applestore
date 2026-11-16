import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class NativeAgentContractTests(unittest.TestCase):
    def setUp(self):
        self.input_schema = load_json("schemas/input.schema.json")
        self.output_schema = load_json("schemas/output.schema.json")
        self.output_validator = Draft202012Validator(self.output_schema)
        self.valid_output = load_json("tests/fixtures/valid-output.json")

    def assert_output_valid(self, instance):
        self.assertEqual(list(self.output_validator.iter_errors(instance)), [])

    def assert_output_invalid(self, instance):
        self.assertNotEqual(list(self.output_validator.iter_errors(instance)), [])

    def test_json_documents_parse(self):
        for path in (
            "config/category_direction.json",
            "config/format_specification.json",
            "config/database_category_mapping.json",
            "schemas/input.schema.json",
            "schemas/output.schema.json",
            "tests/fixtures/valid-output.json",
        ):
            with self.subTest(path=path):
                load_json(path)

    def test_schemas_are_valid_draft_2020_12(self):
        Draft202012Validator.check_schema(self.input_schema)
        Draft202012Validator.check_schema(self.output_schema)

    def test_seven_canonical_categories_and_legacy_mapping(self):
        categories = load_json("config/category_direction.json")["categories"]
        mapping = load_json("config/database_category_mapping.json")["mappings"]
        self.assertEqual(len(categories), 7)
        self.assertEqual(len({x["category_id"] for x in categories}), 7)
        self.assertEqual(len({x["category_slug"] for x in categories}), 7)
        self.assertEqual(
            {(x["category_id"], x["category_slug"]) for x in categories},
            {(x["canonical_id"], x["slug"]) for x in mapping},
        )

    def test_two_formats_use_authoritative_export_canvas(self):
        formats = load_json("config/format_specification.json")["allowed_formats"]
        self.assertEqual(set(formats), {"single_image", "story"})
        expected = {
            "single_image": {
                "generation": {"width_px": 2048, "height_px": 2560},
                "export": {"width_px": 1080, "height_px": 1350},
            },
            "story": {
                "generation": {"width_px": 1440, "height_px": 2560},
                "export": {"width_px": 1080, "height_px": 1920},
            },
        }
        for format_id, dimensions in expected.items():
            with self.subTest(format_id=format_id):
                self.assertEqual(
                    formats[format_id]["generation_canvas"],
                    {**dimensions["generation"], "profile_id": "portrait_2k_long_edge_2560"},
                )
                self.assertEqual(formats[format_id]["export_canvas"], dimensions["export"])
                self.assertEqual(formats[format_id]["canvas"], formats[format_id]["export_canvas"])

    def test_input_schema_accepts_minimum_valid_brief(self):
        validator = Draft202012Validator(self.input_schema, format_checker=FormatChecker())
        brief = {"topic": "iPhone camera features", "format": "single_image"}
        self.assertEqual(list(validator.iter_errors(brief)), [])

    def test_input_schema_rejects_invalid_source_and_asset_uris(self):
        validator = Draft202012Validator(self.input_schema, format_checker=FormatChecker())
        for field in ("source_urls", "asset_urls"):
            with self.subTest(field=field):
                brief = {"topic": "Camera features", "format": "single_image", field: ["http://[::1"]}
                self.assertNotEqual(list(validator.iter_errors(brief)), [])

    def test_output_fixture_validates_as_complete_instance(self):
        self.assertEqual(
            list(self.output_validator.iter_errors(self.valid_output)),
            [],
        )

    def test_output_contract_has_exactly_ten_top_level_keys(self):
        expected = [
            "template_version", "brand", "request", "product", "creative",
            "copywriting", "format_specification", "assets", "compliance",
            "quality_control",
        ]
        self.assertEqual(list(self.output_schema["properties"]), expected)
        self.assertEqual(list(self.valid_output), expected)
        self.assertFalse(self.output_schema["additionalProperties"])

    def test_rejects_category_id_slug_mismatch(self):
        output = copy.deepcopy(self.valid_output)
        output["request"]["primary_category"]["category_slug"] = "promotion"
        self.assert_output_invalid(output)

    def test_rejects_feed_export_dimension_mismatch(self):
        output = copy.deepcopy(self.valid_output)
        output["format_specification"]["export_canvas"]["height_px"] = 1920
        self.assert_output_invalid(output)

    def test_rejects_generation_dimension_mismatch(self):
        output = copy.deepcopy(self.valid_output)
        output["format_specification"]["generation_canvas"]["width_px"] = 1440
        self.assert_output_invalid(output)

    def test_rejects_unexpected_top_level_property(self):
        output = copy.deepcopy(self.valid_output)
        output["debug"] = True
        self.assert_output_invalid(output)

    def test_review_ready_requires_passed_schema_and_all_checks(self):
        output = copy.deepcopy(self.valid_output)
        output["quality_control"]["checks"]["factual_claims"] = False
        self.assert_output_invalid(output)

        output = copy.deepcopy(self.valid_output)
        output["quality_control"]["schema_validation"] = "pending"
        self.assert_output_invalid(output)

    def test_verified_source_status_requires_evidence(self):
        output = copy.deepcopy(self.valid_output)
        output["product"]["evidence"] = []
        self.assert_output_invalid(output)


if __name__ == "__main__":
    unittest.main()
