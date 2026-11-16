# ChatGPT Project Setup — Apple Instagram AI Agent

## Setup

Create a ChatGPT Project named **Apple Instagram AI Agent**.

## Project instructions

Copy the complete contents of `prompts/master_prompt.md` into Project instructions.

## Required reference files

Upload these **five mandatory files** as Project sources:

1. `kategori.md`
2. `config/category_direction.json`
3. `config/format_specification.json`
4. `schemas/input.schema.json`
5. `schemas/output.schema.json`

## Optional reference file

- `docs/output-contract.md` — optional explanatory documentation; it does not replace the authoritative JSON Schema.

## Keep files current

Project sources are uploaded snapshots, not an automatic GitHub mirror. When repository files change, re-upload/replace the corresponding Project sources or retrieve current files using an explicitly connected GitHub app/connector. If current canonical files are unavailable, ChatGPT must not guess their contents.

## Conversation starter

```text
Create an Instagram image prompt.
Topic:
Category: auto
Format: single_image
Objective:
Audience: Apple users in Malaysia
Product details:
Verified source URLs:
```

## Boundaries

- Run all model reasoning inside ChatGPT.
- No OpenAI API key or API call.
- GitHub Actions is for validation only.
- Prompt JSON is not a rendered image.
- Human review is required before publication.
