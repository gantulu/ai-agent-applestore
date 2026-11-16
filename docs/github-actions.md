# GitHub Actions — Validation Only

GitHub Actions validates repository files. It does **not** run the AI Agent, call ChatGPT, generate image prompts, or render images.

## Workflow

Path: `.github/workflows/validate.yml`

Triggers: pushes to `main` or `feat/**`, and pull requests targeting `main`.

Checks:
- JSON syntax for category, format, legacy mapping, and schemas.
- JSON Schema meta-validation and representative input/output contract tests.
- Seven canonical categories and their mapping.
- Two allowed formats and 2K/export dimensions.

Permissions are read-only (`contents: read`). No API secret or model credential is required.

## Generate content

Open the ChatGPT Project **Apple Instagram AI Agent** and submit a brief. ChatGPT executes the Hybrid Agent natively in the conversation.

Do not use GitHub Actions for generation. The former `generate-prompt.yml` workflow is removed.

## Repository configuration

No `OPENAI_API_KEY` secret or `OPENAI_MODEL` variable is required. Do not create either for this project.
