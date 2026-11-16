import json
import unittest

from src.generator import generate
from tests.helpers import valid_output


class FakeProvider:
    def __init__(self, payload):
        self.payload = payload

    def generate(self, instructions, request, schema):
        self.instructions = instructions
        self.request = request
        self.schema = schema
        return json.dumps(self.payload)


class GenerationTests(unittest.TestCase):
    def test_runtime_enforces_requested_format_and_2k_canvas(self):
        request = {"topic": "Focus modes", "format": "story", "category": "tips"}
        provider = FakeProvider(valid_output())
        result = generate(request, provider=provider)
        self.assertEqual(result["format_specification"]["format_id"], "story")
        self.assertEqual(result["format_specification"]["generation_canvas"]["width_px"], 1440)
        self.assertEqual(result["format_specification"]["generation_canvas"]["height_px"], 2560)
        self.assertEqual(result["format_specification"]["export_canvas"], {"width_px": 1080, "height_px": 1920})
        self.assertEqual(result["quality_control"]["schema_validation"], "passed")
        self.assertEqual(result["quality_control"]["status"], "review_ready")

    def test_unverified_claims_force_human_review(self):
        request = {"topic": "Focus modes", "format": "single_image", "category": "tips",
                   "supplied_facts": ["A user-provided feature statement"]}
        result = generate(request, provider=FakeProvider(valid_output()))
        self.assertEqual(result["compliance"]["source_verification_status"], "unverified")
        self.assertFalse(result["quality_control"]["checks"]["factual_claims"])
        self.assertEqual(result["quality_control"]["status"], "needs_human_review")
        self.assertTrue(result["quality_control"]["human_approval_required"])

    def test_explicit_category_mismatch_is_rejected(self):
        request = {"topic": "Focus modes", "format": "single_image", "category": "product"}
        with self.assertRaises(ValueError):
            generate(request, provider=FakeProvider(valid_output()))


if __name__ == "__main__":
    unittest.main()
