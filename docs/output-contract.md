# Output Contract V1.0.0

The output is one JSON object with exactly ten top-level keys in this order:

1. template_version
2. brand
3. request
4. product
5. creative
6. copywriting
7. format_specification
8. assets
9. compliance
10. quality_control

The executable contract is schemas/output.schema.json. All object properties are required; unknown scalar values use null where the schema permits it. Additional properties are rejected.

## Field groups

- **brand:** project context, market, platform, locale, and independent-affiliation disclaimer.
- **request:** topic, objective, audience, primary category, optional secondary category, and concise request summary.
- **product:** product/model/configuration and supplied evidence notes. Evidence notes are not proof of verification.
- **creative:** concept, content angle, key message, visual style, positive image prompt, and negative prompt.
- **copywriting:** headline, optional subheadline, body copy, caption, optional CTA, and hashtags.
- **format_specification:** format ID, placement, ratio, 2K generation canvas, export canvas, and safe-area guidance.
- **assets:** required/reference assets and usage-rights status.
- **compliance:** source verification status, affiliation and asset-rights checks, factual claims, warnings, and mandatory human review.
- **quality_control:** review status, schema validation state, runtime checks, and mandatory human approval.

## Runtime-enforced values

The application, not the model, enforces:
- the canonical category ID/slug/name mapping;
- requested format and exact generation/export dimensions;
- market, platform, locale, and affiliation disclaimer;
- schema validation status after successful validation;
- mandatory human approval;
- human-review status when facts or asset rights remain unverified.

review_ready means structural and automated checks passed; it does not mean fact-checked, approved, or safe to publish. Publication always requires human approval.
