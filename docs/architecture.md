# Apple Instagram AI Agent — ChatGPT-Native Architecture V1.2

## 1. Architecture decision

The agent executes inside the user's ChatGPT conversation or Project. It uses the ChatGPT model and native capabilities. **No OpenAI API, Responses API, API key, or external model endpoint is used.**

GitHub is the version-controlled source of truth. ChatGPT is the execution environment. GitHub Actions performs repository validation only.

## 2. Components

| Layer | Responsibility |
|---|---|
| ChatGPT Project | Instructions, reference files, task conversations |
| Master Prompt | Global agent behavior and execution policy |
| Category config | Seven canonical editorial directions |
| Format config | Feed/Story rules and target dimensions |
| JSON Schemas | Input/output contracts |
| ChatGPT model | Strategist → Creator → Editor |
| Native ChatGPT tools | Web research and image generation when needed |
| GitHub | Version control and canonical configuration |
| GitHub Actions | JSON/config/schema tests only |

## 3. Hybrid pipeline

- **Strategist:** understand brief, audience and objective; choose one primary category, optional secondary category, and one supported format; identify claims needing verification.
- **Creator:** combine Master Prompt, selected category direction, and format specification; create concept, image prompt, negative prompt, headline, caption, CTA, and hashtags.
- **Editor:** check category/format, English en-MY, Malaysia context, brand/asset safeguards, factual claims, and ten-key JSON output contract.

These are sequential responsibilities of one ChatGPT-native agent, not separate deployed agents.

## 4. Configuration source of truth

- `kategori.md` V2.1.0
- `prompts/master_prompt.md`
- `config/category_direction.json`
- `config/format_specification.json`
- `schemas/input.schema.json`
- `schemas/output.schema.json`

ChatGPT must use current repository files available in the Project/chat. Project uploads are snapshots, not automatic GitHub synchronization; refresh them or retrieve current files using an explicitly connected GitHub app/connector.

## 5. Execution flow

1. User submits a brief in the ChatGPT Project.
2. ChatGPT uses Project instructions and reference files.
3. Strategist selects category and format.
4. Creator develops visual concept and copy.
5. Editor checks factual claims, safeguards, and output contract.
6. ChatGPT returns the JSON draft.
7. If explicitly requested, ChatGPT may render an image using its native image-generation capability.
8. Human reviews and separately handles publication.

No GitHub Actions workflow invokes a model or generates content.

## 6. Tool boundaries

- Web search only when current facts need research; cite sources.
- Native image generation is optional and distinct from prompt writing.
- No automatic publishing, scheduling, database persistence, or external API calls.
- Never claim prompt JSON is a rendered image.
- Never claim programmatic schema validation unless a validator actually ran.

## 7. Output contract

Exactly ten top-level keys: `template_version`, `brand`, `request`, `product`, `creative`, `copywriting`, `format_specification`, `assets`, `compliance`, `quality_control`. Nested fields and constraints are in `schemas/output.schema.json`.

## 8. GitHub Actions

Only `.github/workflows/validate.yml` remains. It validates JSON files, JSON Schema definitions, and contract tests. The former `generate-prompt.yml` is removed because generation is ChatGPT-native.

## 9. Database boundary

The legacy SQL mapping is retained as reference only. ChatGPT does not connect to the database, run SQL, create webhook records, or schedule posts.

## 10. Security and non-goals

No API key, external model credential, model inference in CI, automatic publishing, database writes, custom backend, or promise of automatic GitHub-to-Project synchronization.
