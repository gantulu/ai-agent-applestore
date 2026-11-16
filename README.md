# Apple Instagram AI Agent

A **ChatGPT-native Hybrid Agent** for creating Instagram image-generation prompts and structured content drafts for Apple-product content targeting Malaysia.

## Execution model

**The agent runs in ChatGPT. No OpenAI API key is required.**
- ChatGPT performs Strategist → Creator → Editor in the active conversation.
- GitHub stores the version-controlled Master Prompt, modular configuration, and JSON contracts.
- GitHub Actions validates repository files only; it does not execute AI generation.
- No external model API, API credential, or model endpoint is used.
- The primary deliverable is a strict-JSON image-generation prompt. Actual image rendering is optional and uses ChatGPT's native image-generation capability when explicitly requested.

## Recommended ChatGPT setup

Create a ChatGPT Project named **Apple Instagram AI Agent**.

1. Add the complete contents of `prompts/master_prompt.md` to Project instructions.
2. Upload these files as Project sources: `kategori.md`, `config/category_direction.json`, `config/format_specification.json`, `schemas/input.schema.json`, and `schemas/output.schema.json`.
3. Optionally upload `docs/output-contract.md`.
4. Start each task in the Project with the brief, product details, sources, and desired format.
5. When repository files change, refresh the Project sources or retrieve current files using an explicitly connected GitHub app/connector. Project files are not an automatic live mirror of GitHub.

Projects support instructions, reference files, and ongoing conversations: [OpenAI Projects documentation](https://help.openai.com/en/articles/10169521-projects-in-chatgpt). New custom GPT creation is unavailable on personal Free, Go, Plus, and Pro accounts according to current OpenAI documentation, so Projects are the recommended option: [GPT creation availability](https://help.openai.com/en/articles/8554397-create-a-gpt).

## Project baseline

| Item | Standard |
|---|---|
| Agent | One Hybrid Agent: Strategist → Creator → Editor |
| Execution | ChatGPT native Project/conversation |
| Market / language | Malaysia / English (en-MY) |
| Categories | 7 canonical categories from kategori.md V2.1.0 |
| Formats | single_image (Feed), story (Story) |
| Generation profile | Portrait 2K long edge 2560 px |
| Output contract | Strict JSON Schema 1.0.0 |
| GitHub Actions | Validation only |
| Model API / API key | Not used |
| Publication | Draft only; human approval required |

## Canonical categories

| ID | Slug | Category |
|---|---|---|
| CAT-001 | product | Product |
| CAT-002 | promotion | Promotion |
| CAT-003 | lifestyle | Lifestyle |
| CAT-004 | education | Education |
| CAT-005 | news | News |
| CAT-006 | comparison | Comparison |
| CAT-007 | tips | Tips |

One primary category is mandatory; one secondary category is optional. Select by editorial objective, not merely by the featured product.

## Formats and resolution

| Format | 2K generation canvas | Instagram export canvas | Ratio |
|---|---:|---:|---:|
| Feed / single_image | 2048 × 2560 | 1080 × 1350 | 4:5 |
| Story / story | 1440 × 2560 | 1080 × 1920 | 9:16 |

These are project target dimensions, not a guarantee that ChatGPT's native image tool renders at those exact pixel dimensions. Actual image output options govern rendered image size.

## Example request

```text
Create an Instagram image prompt.
Topic: iPhone camera features
Category: auto
Format: single_image
Objective: education
Audience: Apple users in Malaysia
Product details / verified sources: [provide details]
```

The agent selects a canonical category, combines the Master Prompt with the matching category and format rules, and returns the strict JSON contract. Current price, promotion, availability, compatibility, and news claims must be researched or flagged as unverified.

## Repository validation

GitHub Actions validates JSON configuration, JSON Schemas, and contract tests on pushes and pull requests. CI does not call ChatGPT and requires no AI API secret.

See [architecture](docs/architecture.md), [ChatGPT Project setup](docs/chatgpt-project-setup.md), [output contract](docs/output-contract.md), and [GitHub Actions](docs/github-actions.md).

## Safety

- No OPENAI_API_KEY, OpenAI API, Responses API, or external model endpoint.
- No AI inference or image generation in GitHub Actions.
- No automatic Instagram publishing, scheduling, or database writes.
- Factual claims and asset rights require verification and human review.
- Legacy SQL mapping is reference-only.
