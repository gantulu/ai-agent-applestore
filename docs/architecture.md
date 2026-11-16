# Apple Instagram AI Agent — Final Architecture V1.1

## 1. Status

**Architecture:** locked for V1.1 implementation.  
**Runtime:** Python 3.11+; one Hybrid Agent.  
**Orchestration:** GitHub Actions.  
**Model interface:** OpenAI Responses API through a provider adapter.  
**Output:** strict JSON contract V1.0.0.  
**Publication:** draft-only; human approval required.

## 2. Locked decisions

1. One Hybrid Agent performs three sequential responsibilities: Strategist → Creator → Editor. They are pipeline stages, not independently deployed agents.
2. kategori.md V2.1.0 remains the single source of truth for exactly seven categories.
3. The generator accepts exactly single_image and story.
4. Content language is English (en-MY); market is Malaysia (MY).
5. One global Master Prompt combines with one category direction and one format specification.
6. Output contains exactly ten top-level keys and is validated by JSON Schema.
7. Generation dimensions are distinct from Instagram export dimensions:
   - Feed: 2048 × 2560 generation; 1080 × 1350 export (4:5).
   - Story: 1440 × 2560 generation; 1080 × 1920 export (9:16).
8. The 2K profile is a project target (2560 px long edge), not a guarantee of native provider capability. Provider limitations must be explicit; this runtime does not upscale images.
9. GitHub Actions manual trigger generates a JSON prompt artifact; CI validates code/configuration.
10. No Instagram publishing, scheduling, or database writes are performed by the generator.

## 3. Component architecture

```text
GitHub Actions
  ├── validate.yml (push / pull_request)
  │     ├── JSON config parse
  │     └── unittest + JSON Schema validation
  └── generate-prompt.yml (workflow_dispatch)
        ├── validate request
        ├── load Master Prompt
        ├── load category direction (1 primary + optional secondary)
        ├── load format specification (1 format)
        ├── OpenAI Responses API adapter
        ├── runtime safeguards + JSON Schema validation
        └── upload prompt-output.json artifact

Python runtime
  ├── config_loader.py
  ├── prompt_builder.py
  ├── provider.py
  ├── generator.py
  ├── validator.py
  └── legacy_mapping.py (preview only; no DB writes)
```

## 4. Hybrid Agent stages

### Strategist
- Understand topic, audience, objective, and desired audience benefit.
- Select one canonical primary category and at most one secondary category.
- Choose the requested supported format.
- Identify facts and claims requiring verification.

### Creator
- Build the creative angle and visual concept.
- Apply category direction and format rules.
- Produce the image-generation prompt, negative prompt, headline, caption, CTA, and hashtags.
- Specify generation and export dimensions separately.

### Editor
- Check category/format allowlists and JSON structure.
- Enforce English (en-MY) and Malaysia context.
- Apply brand-affiliation and asset-rights safeguards.
- Flag unverified claims and require human review.

## 5. Runtime and provider boundary

- Provider implementation: src/provider.py.
- API: OpenAI Responses API with strict JSON Schema output.
- Model: OPENAI_MODEL environment variable; default gpt-6-luna.
- Credential: OPENAI_API_KEY environment variable / GitHub Actions secret.
- Optional settings: OPENAI_BASE_URL, OPENAI_TIMEOUT_SECONDS.
- The provider adapter is isolated so another provider can be added without changing the category taxonomy or output contract.
- The runtime does not use web search. Supplied claims and sources are not treated as independently verified.

## 6. Output contract

The ten top-level keys, in order:
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

Nested fields, types, enums, and nullability are defined in schemas/output.schema.json. Unknown facts use nullable fields or review warnings; the model must not fabricate values to satisfy the schema.

## 7. Database compatibility boundary

The existing SQL reference stores category slugs in make_webhook_categories.category. The make_webhook.category_id foreign key points to that slug column despite its name. config/database_category_mapping.json maps canonical CAT-NNN IDs to those legacy slugs.

A generated prompt does not include a rendered image URL or a publication schedule. The legacy make_webhook row requires date and time, and the queue's purpose is image publication. Therefore the implementation provides a preview mapper only and performs no insert/update. A future DB writer requires an approved image-generation/storage step, schedule input, credentials, and explicit write scope.

## 8. Security and operational controls

- Workflows use least-privilege contents: read.
- Third-party actions are pinned to full commit SHAs.
- API keys are never stored in source files, input JSON, logs, or artifacts.
- Generation artifacts are retained for 14 days.
- CI never calls the paid model API.
- No pull_request_target, automatic publishing, or write-enabled workflow token is used.

## 9. Phase completion

| Phase | Deliverable | Status |
|---|---|---|
| 1 — Documentation alignment | Canonical taxonomy and architecture baseline | Complete |
| 2 — Prompt architecture | Master Prompt + 7 category directions + 2 formats | Complete; PR #2 merged |
| 3 — JSON contract | Input/output schemas and contract documentation | Implemented; automated tests |
| 4 — Generation runtime | Config loader, prompt assembler, Responses API adapter, JSON writer | Implemented |
| 5 — Quality assurance | Category/format/schema/generation/mapping tests and CI | Implemented; CI verification required |
| 6 — Database compatibility | Canonical ID → legacy slug mapping; safe preview adapter | Complete for prompt-generation scope; live DB writes intentionally excluded |

## 10. Non-goals

- Image rendering, image upscaling, or asset storage.
- Instagram Graph API, publishing, or scheduling.
- Automatic source research or independent fact verification.
- Live database persistence.
- Separate autonomous agents or a web dashboard.
