# Database Compatibility — Legacy SQL V1

## Observed legacy relationship

The SQL reference contoh/public.md defines:

- public.make_webhook_categories.category as the category primary key.
- public.make_webhook.category_id as a foreign key to make_webhook_categories.category.

Despite the category_id column name, the stored foreign-key value is a category slug, e.g. tips, not the canonical identifier CAT-007.

## Canonical mapping

| Canonical ID | Canonical slug | Legacy value |
|---|---|---|
| CAT-001 | product | product |
| CAT-002 | promotion | promotion |
| CAT-003 | lifestyle | lifestyle |
| CAT-004 | education | education |
| CAT-005 | news | news |
| CAT-006 | comparison | comparison |
| CAT-007 | tips | tips |

Machine-readable mapping: config/database_category_mapping.json.

## Why no direct insert is implemented

The current agent output is a prompt draft, not a rendered image. The legacy make_webhook table requires date and time and is intended to queue an image/caption for publishing. A generated prompt does not provide a valid image_url or an approved schedule.

The runtime therefore exposes build_legacy_webhook_preview() only. It:
- validates the canonical category ID/slug pair;
- maps it to the legacy slug value;
- reports missing queue fields;
- always sets write_performed: false.

No database connection, migration, seed update, or webhook call is made.

## Requirements for a future persistence phase

Before enabling writes, approve:
1. the image-generation/storage provider and the final image URL contract;
2. schedule date/time and timezone rules;
3. human approval state and who may queue content;
4. database credentials and least-privilege access;
5. idempotency and duplicate prevention;
6. migration strategy if the legacy category_id field is renamed or changed to a true canonical ID.

Do not change the existing foreign key or seed rows as part of prompt generation.
