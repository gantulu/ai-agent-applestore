# GitHub Actions Operations

## Workflows

### Validate AI Agent
Path: .github/workflows/validate.yml

Runs on pushes to main and feat/**, and pull requests targeting main. It parses configuration/schema JSON and runs the unit tests. It does not call the model API and does not need the OpenAI secret.

### Generate Instagram Image Prompt
Path: .github/workflows/generate-prompt.yml

Manual workflow_dispatch only. Inputs:
- topic (required)
- category (auto or one of seven canonical slugs)
- format (single_image or story)
- product name (optional)
- objective (optional)
- audience (optional)

The workflow generates outputs/prompt-output.json and uploads it as an artifact for 14 days. It creates a text prompt; it does not render an image or publish to Instagram.

GitHub only exposes the manual Run workflow action when the workflow file is present on the default branch. See [workflow_dispatch documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow).

## Required repository configuration

1. Open Settings → Secrets and variables → Actions.
2. Add secret OPENAI_API_KEY with an API key belonging to the intended OpenAI Platform project.
3. Optionally add variable OPENAI_MODEL; default is gpt-6-luna. Choose a model enabled for the API project.
4. No API key should be stored in repository files, workflow inputs, or artifacts.

Optional environment variables:
- OPENAI_BASE_URL — defaults to https://api.openai.com/v1.
- OPENAI_TIMEOUT_SECONDS — defaults to 90.

## Security

- Workflows declare contents: read; they do not need repository write permissions.
- Actions are pinned to full commit SHAs.
- Checkout uses persist-credentials: false.
- Secrets are passed through environment variables and are never printed.
- CI on pull requests does not access the model secret.

GitHub references:
- [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Triggering workflows](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow)
- [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)

## Troubleshooting

- **Missing OPENAI_API_KEY:** add the repository secret and rerun.
- **Model unavailable:** set OPENAI_MODEL to a model enabled for the API project.
- **Schema error:** inspect the failed job log; update the contract and tests together.
- **No artifact:** generation must complete and write the JSON file before upload.
