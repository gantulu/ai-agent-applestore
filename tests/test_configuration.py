import unittest

from src.config_loader import load_project_config
from src.prompt_builder import build_instructions


class ConfigurationTests(unittest.TestCase):
    def test_seven_canonical_categories_are_unique_and_match_legacy_map(self):
        config = load_project_config()
        categories = config["categories"]["categories"]
        mappings = config["category_mapping"]["mappings"]
        self.assertEqual(len(categories), 7)
        self.assertEqual(len({item["category_id"] for item in categories}), 7)
        self.assertEqual(len({item["category_slug"] for item in categories}), 7)
        self.assertEqual(
            {(item["category_id"], item["category_slug"]) for item in categories},
            {(item["canonical_id"], item["slug"]) for item in mappings},
        )

    def test_two_formats_keep_2k_generation_separate_from_export(self):
        config = load_project_config()
        formats = config["formats"]["allowed_formats"]
        self.assertEqual(set(formats), {"single_image", "story"})
        self.assertEqual(formats["single_image"]["generation_canvas"], {
            "width_px": 2048, "height_px": 2560, "profile_id": "portrait_2k_long_edge_2560"
        })
        self.assertEqual(formats["single_image"]["canvas"], {"width_px": 1080, "height_px": 1350})
        self.assertEqual(formats["story"]["generation_canvas"], {
            "width_px": 1440, "height_px": 2560, "profile_id": "portrait_2k_long_edge_2560"
        })
        self.assertEqual(formats["story"]["canvas"], {"width_px": 1080, "height_px": 1920})

    def test_prompt_assembles_one_category_and_one_format(self):
        config = load_project_config()
        instructions = build_instructions(config, {"topic": "Focus modes", "category": "tips", "format": "story"})
        self.assertIn('"category_slug": "tips"', instructions)
        self.assertIn('"format_id": "story"', instructions)
        self.assertIn("2K generation canvas", instructions)

    def test_unsupported_category_is_rejected(self):
        config = load_project_config()
        with self.assertRaises(ValueError):
            build_instructions(config, {"topic": "x", "category": "reels", "format": "story"})


if __name__ == "__main__":
    unittest.main()
