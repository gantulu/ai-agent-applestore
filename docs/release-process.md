# Release & Maintenance Process

## Purpose

This repository contains the version-controlled instructions, configuration, and JSON contracts for a ChatGPT-native Hybrid Agent. Releases update those project assets; they do not deploy an AI runtime.

## Source of truth

- GitHub default branch `main` is the canonical repository baseline.
- ChatGPT Project instructions and uploaded reference files are snapshots. They do not synchronize automatically with GitHub.
- GitHub Actions validates repository content only. It does not invoke ChatGPT, call an external model API, or generate images.

## Change workflow

1. Start from the latest `main`.
2. Create a focused branch for one change set.
3. Update the relevant prompt, category, configuration, schema, tests, or documentation.
4. Run the local validation command: `python3 -m pip install -r requirements.txt && python3 -m unittest discover -s tests -v`.
5. Open a pull request targeting `main`.
6. Confirm the `Validate AI Agent` required check passes and review the diff for scope, factual correctness, and accidental secrets.
7. Merge only after required repository rules are satisfied.

Direct pushes to `main` should be avoided once branch protection is active. Until then, use pull requests voluntarily.

## Release checklist

- [ ] Confirm the change matches the approved roadmap and architecture.
- [ ] Confirm no OpenAI API key, external model endpoint, or runtime dependency was introduced.
- [ ] Confirm no automatic Instagram publishing, scheduling, or database write was introduced.
- [ ] Validate JSON syntax, JSON Schemas, fixtures, and automated tests.
- [ ] Confirm README, setup guide, architecture, configuration, and output contract agree.
- [ ] Update document version and `Last Updated` metadata where applicable.
- [ ] Review source evidence, asset rights, and human-approval safeguards where content rules change.
- [ ] Merge the reviewed change to `main`.
- [ ] Record the resulting commit SHA and CI run.
- [ ] Refresh the corresponding ChatGPT Project instructions/reference files or retrieve the current canonical files through an explicitly connected GitHub integration.

## ChatGPT Project refresh

After a release, compare the changed repository paths with the Project's five mandatory reference files:

1. `kategori.md`
2. `config/category_direction.json`
3. `config/format_specification.json`
4. `schemas/input.schema.json`
5. `schemas/output.schema.json`

Also refresh Project instructions from `prompts/master_prompt.md` when it changes. The optional `docs/output-contract.md` is explanatory and does not replace the JSON Schema.

## Rollback and maintenance

- Revert a problematic change through a reviewed pull request; do not force-push shared history.
- Keep historical branches only when they are intentionally used for recovery or ongoing work.
- Review branch protection and required CI checks after repository permission or workflow changes.
- Do not delete branches solely because their pull requests were merged; verify their purpose and preserve any required recovery reference first.
- Treat the JSON Schemas and canonical configuration as the authority when prose documentation conflicts.

## Release boundary

A successful GitHub Actions run means repository validation passed. It does not prove that all 14 category/format scenarios work in ChatGPT. End-to-end validation and human approval remain part of P3.
