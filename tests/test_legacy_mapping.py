import unittest

from src.legacy_mapping import build_legacy_webhook_preview
from tests.helpers import valid_output


class LegacyMappingTests(unittest.TestCase):
    def test_category_id_maps_to_legacy_slug_not_canonical_id(self):
        preview = build_legacy_webhook_preview(valid_output())
        self.assertEqual(preview["category_id_legacy_value"], "tips")
        self.assertNotEqual(preview["category_id_legacy_value"], "CAT-007")
        self.assertEqual(preview["status"], "not_insertable")
        self.assertFalse(preview["write_performed"])
        self.assertEqual(set(preview["missing_required_fields"]), {"image_url", "date", "time"})

    def test_complete_legacy_record_is_still_preview_only(self):
        preview = build_legacy_webhook_preview(
            valid_output(), image_url="https://example.test/image.png",
            scheduled_date="2026-11-20", scheduled_time="19:00:00"
        )
        self.assertEqual(preview["status"], "preview_only")
        self.assertFalse(preview["write_performed"])


if __name__ == "__main__":
    unittest.main()
