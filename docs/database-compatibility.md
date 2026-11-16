# Database Compatibility — Legacy SQL Reference

The SQL reference `contoh/public.md` defines `make_webhook_categories.category` as the category primary key and `make_webhook.category_id` as a foreign key to that slug column. Despite the column name, the stored value is a slug (for example `tips`), not `CAT-007`.

The canonical mapping is retained in `config/database_category_mapping.json`.

## ChatGPT-native boundary

The ChatGPT-native agent does not connect to this database, run SQL, create webhook records, or schedule posts. This mapping is reference documentation for a possible separately approved integration only.

A prompt draft is not a rendered image and does not provide a valid `image_url` or approved schedule. No database write is performed.

Any future persistence work requires separate approval for image storage, scheduling/timezone rules, authorization, credentials, idempotency, and migration strategy.
