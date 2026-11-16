import json
import unittest

from src.config_loader import load_project_config
from src.validator import ContractValidationError, validate
from tests.helpers import valid_output


class ContractTests(unittest.TestCase):
    def test_output_has_exactly_ten_top_level_keys(self):
        config = load_project_config()
        self.assertEqual(
            list(config["output_schema"]["properties"].keys()),
            ["template_version", "brand", "request", "product", "creative",
             "copywriting", "format_specification", "assets", "compliance", "quality_control"],
        )

    def test_example_request_matches_input_schema(self):
        config = load_project_config()
        with open("inputs/request.example.json", encoding="utf-8") as handle:
            request = json.load(handle)
        validate(request, config["input_schema"], "Input")

    def test_valid_output_matches_schema(self):
        config = load_project_config()
        validate(valid_output(), config["output_schema"], "Output")

    def test_unknown_output_field_is_rejected(self):
        config = load_project_config()
        output = valid_output()
        output["unapproved"] = True
        with self.assertRaises(ContractValidationError):
            validate(output, config["output_schema"], "Output")


if __name__ == "__main__":
    unittest.main()
