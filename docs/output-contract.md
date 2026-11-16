# Output Contract V1.0.0

The ChatGPT-native agent returns one JSON object with exactly ten top-level keys in this order:

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

The machine-readable contract is schemas/output.schema.json. Object properties are required; unknown scalar values use null where permitted. Additional properties are rejected.

## Field groups

- **brand:** project context, market, platform, locale, affiliation disclaimer.
- **request:** topic, objective, audience, primary category, optional secondary category, summary.
- **product:** product/model/configuration and supplied evidence notes.
- **creative:** concept, content angle, key message, visual style, image prompt, negative prompt.
- **copywriting:** headline, subheadline, body copy, caption, CTA, hashtags.
- **format_specification:** format, placement, ratio, generation canvas, export canvas, safe area.
- **assets:** required/reference assets and usage-rights status.
- **compliance:** source verification, affiliation and asset-rights checks, factual claims, warnings, human review.
- **quality_control:** review status, schema validation state, checks, human approval.

## ChatGPT execution rules

ChatGPT follows the schema and fixed project values. Do not claim programmatic validation passed unless a JSON Schema validator was actually executed. Otherwise identify the output as checked by inspection, not machine-validated.

A review_ready value means only that the checks actually performed passed. It does not mean fact-checked, approved, or safe to publish. Human approval is always required before publication.
