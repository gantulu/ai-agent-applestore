# Apple Instagram AI Agent

AI Agent untuk menghasilkan image-generation prompts Instagram bagi projek kandungan produk dan ekosistem Apple dengan sasaran pasaran Malaysia.

## Project baseline

| Item | Standard |
|---|---|
| Agent | One Hybrid Agent: Strategist → Creator → Editor |
| Market / language | Malaysia / English (en-MY) |
| Canonical categories | 7, from kategori.md V2.1.0 |
| Instagram formats | single_image (Feed), story (Story) |
| Generation profile | Portrait 2K long edge 2560 px |
| Output contract | Strict JSON Schema, version 1.0.0 |
| Runtime | Python 3.11+ |
| Orchestration | GitHub Actions |
| Model API | OpenAI Responses API (configurable model) |
| Publication | Draft only; human approval required |

**Brand disclaimer:** This is an independent Apple-product content project. Do not claim Apple ownership, endorsement, or authorized-reseller status unless separately verified and expressly permitted.

## Canonical categories

The source of truth is [kategori.md](./kategori.md) V2.1.0.

| ID | Slug | Category |
|---|---|---|
| CAT-001 | product | Product |
| CAT-002 | promotion | Promotion |
| CAT-003 | lifestyle | Lifestyle |
| CAT-004 | education | Education |
| CAT-005 | news | News |
| CAT-006 | comparison | Comparison |
| CAT-007 | tips | Tips |

One primary category is mandatory; one secondary category is optional. Category is selected by editorial objective, not merely by the product shown.

## Formats and resolution

| Format | 2K generation canvas | Instagram export canvas | Ratio |
|---|---:|---:|---:|
| Feed / single_image | 2048 × 2560 | 1080 × 1350 | 4:5 |
| Story / story | 1440 × 2560 | 1080 × 1920 | 9:16 |

The 2K values define this project's portrait generation profile (2560 px long edge). They do not guarantee native output support from every image provider. This repository generates the text prompt and target dimensions; it does not generate or upscale image files.

## Quick start

Requirements: Python 3.11+ and an OpenAI API key.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

export OPENAI_API_KEY="your-api-key"
export OPENAI_MODEL="gpt-6-luna"  # optional; override to a model enabled for your API project

python3 -m src.main \
  --input inputs/request.example.json \
  --output outputs/prompt-output.json
```

The generated file is validated against schemas/output.schema.json. The runtime does not browse or independently verify facts, so factual claims are marked for human review.

## Generate from GitHub Actions

1. In GitHub, open Settings → Secrets and variables → Actions.
2. Add repository secret OPENAI_API_KEY.
3. Optionally add repository variable OPENAI_MODEL; default is gpt-6-luna.
4. Open Actions → Generate Instagram Image Prompt → Run workflow.
5. Enter the topic, category (or auto), format, and optional product details.
6. Download the instagram-prompt artifact. It contains prompt-output.json.

The manual workflow is available after .github/workflows/generate-prompt.yml is merged into the default branch. See [GitHub Actions guide](./docs/github-actions.md).

## Local validation

```bash
python3 -m pip install -r requirements.txt
python3 -m json.tool schemas/input.schema.json > /dev/null
python3 -m json.tool schemas/output.schema.json > /dev/null
python3 -m unittest discover -s tests -v
```

CI runs the same tests on pushes and pull requests. The tests do not call the paid model API.

## Repository map

| Path | Purpose |
|---|---|
| README.md | Project baseline and setup |
| kategori.md | Canonical seven-category taxonomy |
| prompts/master_prompt.md | Global Hybrid Agent instructions |
| config/category_direction.json | Seven modular category directions |
| config/format_specification.json | Feed/Story and 2K/export dimensions |
| schemas/input.schema.json | Generation request contract |
| schemas/output.schema.json | Strict ten-key output contract |
| src/ | Configuration, prompt assembly, provider, generator, validators |
| tests/ | Contract, configuration, generation, and mapping tests |
| .github/workflows/ | CI validation and manual prompt generation |
| docs/database-compatibility.md | Legacy SQL category mapping and write boundary |

## Safety and scope

- API keys are read only from environment variables / GitHub Secrets; never commit credentials.
- GitHub Actions uses read-only contents permission and actions pinned to full commit SHAs.
- The runtime does not auto-publish, schedule, or send Instagram content.
- The legacy SQL queue requires an actual image URL and schedule date/time. Prompt JSON alone is not a publishable queue record; no database write is performed.
- Product, price, compatibility, news, and promotion claims require source verification and human review.
- See [architecture](./docs/architecture.md), [output contract](./docs/output-contract.md), and [database compatibility](./docs/database-compatibility.md).
