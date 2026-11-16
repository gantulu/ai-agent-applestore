# AI Agent Improvement Roadmap — V1.0

**Repository:** `gantulu/ai-agent-applestore`  
**Status:** Approved and locked  
**Baseline:** ChatGPT-native Hybrid Agent — Strategist → Creator → Editor  
**Execution order:** P1 → P2 → P3

This roadmap hardens the existing agent without introducing a backend runtime, external model API, automated Instagram publishing, scheduling, or database writes.

## P1 — Schema & CI hardening

**Goal:** make the output contract and automated validation reliable.

- [x] Add a representative complete output fixture.
- [x] Add negative tests for category mismatch, invalid dimensions, unexpected properties, and failed quality gates.
- [x] Validate authoritative `export_canvas` dimensions and retain the backward-compatible `canvas` equality check.
- [x] Enforce that `review_ready` requires `schema_validation=passed` and all quality checks to be true.
- [x] Enforce evidence presence when source verification is marked `verified`.
- [x] Enable JSON Schema URI format checking in tests.

**Acceptance:** valid fixture passes; invalid fixtures/mutations fail; CI runs all contract tests.

## P2 — Documentation & repository hygiene

**Goal:** keep project setup and repository operations consistent and maintainable.

- [ ] Clarify five mandatory Project reference files and one optional documentation file.
- [ ] Synchronise README, setup guide, schema, and configuration documentation.
- [ ] Correct category document update metadata.
- [ ] Audit historical branches; delete merged branches only after explicit approval.
- [ ] Verify `main` branch protection and required CI checks.
- [ ] Document release and maintenance procedures.

**Acceptance:** setup instructions are unambiguous, active configuration is clearly identified, and repository governance is verified.

## P3 — End-to-end testing & release readiness

**Goal:** verify the complete ChatGPT-native workflow before controlled pilot use.

### Category × format test matrix

Test all 14 combinations:

| Category | Feed / `single_image` | Story |
|---|---:|---:|
| Product | [ ] | [ ] |
| Promotion | [ ] | [ ] |
| Lifestyle | [ ] | [ ] |
| Education | [ ] | [ ] |
| News | [ ] | [ ] |
| Comparison | [ ] | [ ] |
| Tips | [ ] | [ ] |

### Agent role verification

- [ ] Strategist: objective, audience, category, product focus, and format.
- [ ] Creator: concept, visual direction, and copywriting.
- [ ] Editor: factual verification, locale, compliance, and output validation.

### Quality and pilot readiness

- [ ] Verify brand consistency and product accuracy.
- [ ] Verify source provenance for factual, news, and promotion claims.
- [ ] Verify English `en-MY` quality and format dimensions.
- [ ] Verify human review remains mandatory.
- [ ] Run real ChatGPT Project scenarios and record results.
- [ ] Resolve critical blockers and publish a release baseline.

**Acceptance:** all 14 scenarios are documented, role checks pass, and a controlled pilot report is approved.

## Delivery rules

1. Complete and verify one priority before starting the next.
2. Keep changes scoped to the approved priority.
3. Preserve the ChatGPT-native execution model.
4. Do not delete historical branches or change branch protection without explicit approval.
5. A successful CI run does not replace end-to-end testing in ChatGPT.
