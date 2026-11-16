# P2 Maintenance Automation V1

## Status

The initial implementation is intentionally read-only. It adds a manually triggered GitHub Actions audit at `.github/workflows/p2-maintenance-audit.yml`.

It does not delete branches, create archive tags, change branch protection, or create/update repository rulesets.

## Authentication and permission audit

The linked GitHub connection reports administrator permission for `gantulu` on this repository. This confirms the connected identity's repository role; it does not reveal the scopes of a separate fine-grained personal access token or the contents of Actions secrets.

The repository is public, the default branch is `main`, and the current Rulesets API read returned an empty list. The connected integration received HTTP 403 when reading classic branch protection, so the exact protection state must be verified with an appropriately authorized token.

## Fine-grained PAT requirements

Create a fine-grained PAT with:

- Resource owner: `gantulu`
- Repository access: only `ai-agent-applestore`
- Repository permission `Contents: write`: required to create archive refs and delete approved branch refs.
- Repository permission `Administration: write`: required to create/update repository rulesets and read their configuration.

Do not grant organization-wide access, account permissions, Actions write, or Workflows write for the planned API operations unless a separately reviewed feature proves they are necessary.

Store the token as the repository Actions secret `P2_MAINTENANCE_PAT`. Never commit or print the token, and never paste it into a chat message. The current read-only audit workflow does not consume this secret.

## Planned write workflow — gated, not yet enabled

### Branch archival and cleanup

1. Produce a read-only report for every non-default branch.
2. Review ahead/behind counts and changed file paths against `main`.
3. Identify commits and files not represented in `main`.
4. Create an archive tag for each branch explicitly approved for retirement, pointing to its reviewed head SHA.
5. Read each archive ref back and verify it points to the expected SHA.
6. Require an explicit allowlist of exact branch names and a confirmation phrase before deletion.
7. Refuse to delete `main`, unknown branches, branches not in the allowlist, or branches whose head SHA changed since review.
8. Delete only approved branch refs, then verify the branch is absent and archive tag remains.

### Main ruleset

1. Read existing rulesets and current protection state.
2. Confirm no conflicting ruleset exists.
3. Prepare a ruleset targeting only `refs/heads/main`.
4. Proposed rules: require pull request, zero required approvals, require the `Validate AI Agent` check, require branch up to date, block force pushes, and restrict deletions.
5. Show the exact proposed payload and require a separate explicit apply confirmation.
6. Create/update the ruleset only after approval, then read it back and verify every rule.

Do not enable deletion or ruleset writes as a side effect of an audit run.

## Workflow security controls

- Trigger: `workflow_dispatch` only.
- Default behavior: audit / dry-run.
- Explicit least-privilege `permissions` at workflow/job level.
- Use the PAT only in the write job and only as an environment secret.
- Do not expose secrets in command arguments, logs, artifacts, or summaries.
- Pin third-party actions to immutable commit SHAs.
- Use concurrency control to prevent overlapping maintenance runs.
- Validate repository name, default branch, exact branch allowlist, expected branch SHAs, and confirmation input.
- Separate branch cleanup and ruleset application into independent operations.
- Keep an auditable summary of planned and completed actions without logging credentials.

## Execution and acceptance

The initial read-only workflow must be run manually from GitHub Actions and its summary reviewed. The write-capable extension must not be enabled until the PAT secret is configured and its effective permissions are verified. Branch deletion and ruleset activation each require their own review and explicit approval.

The P2 work is complete only after branch cleanup and main protection are independently verified. P3 remains gated on P2 completion.
