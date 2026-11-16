# Apple Instagram AI Agent — Architecture V1.0

## 1. Status and purpose

**Status:** Approved architecture baseline  
**Scope:** Instagram content generation for an Apple-product-focused account/project targeting Malaysia.  
**Agent role:** Hybrid — Strategist + Creator + Editor.  
**Audience-facing content language:** English (`en-MY`).

This document describes the approved logical architecture. It is not a claim that the runtime, prompts, JSON schema, tests, or database integration have already been implemented.

## 2. Architecture principles

1. One global Master Prompt governs the agent.
2. Category direction and format specification are independent, reusable configurations.
3. Exactly one primary category is required for each generated content item.
4. A secondary category is optional and limited to one.
5. V1.0 generation supports exactly two formats: `single_image` and `story`.
6. Output is validated against one versioned strict JSON contract.
7. Fact verification, brand/legal safeguards, and editorial review are mandatory quality gates.
8. Generation and publication are separate. The agent creates drafts; it does not publish automatically.
9. Documentation language and generated content language are separate settings.

## 3. Logical architecture

```text
                 CONTENT REQUEST
                       |
                       v
              GLOBAL MASTER PROMPT
          Hybrid Role | Market | Language
                       |
             +---------+---------+
             |                   |
             v                   v
     CATEGORY DIRECTION   FORMAT SPECIFICATION
       7 categories          2 formats
             |                   |
             +---------+---------+
                       |
                       v
                GENERATION ENGINE
      Strategy -> Creative -> Copywriting -> Editing
                       |
                       v
                 OUTPUT CONTRACT
                  Strict JSON
                       |
                       v
                VALIDATION GATES
       Schema | Facts | Editorial | Brand/Legal
                       |
              +--------+--------+
              |                 |
              v                 v
          NEEDS REVIEW       REVIEW-READY
              |                 |
              +--------+--------+
                       |
                Human approval
                       |
                 (Future scope)
                 Publication
```

## 4. Hybrid agent responsibilities

### 4.1 Strategist

- Interpret the content request and intended business outcome.
- Identify target audience and audience need.
- Select one primary category and, only when justified, one secondary category.
- Define content objective, funnel stage, key message, and product focus.
- Select one supported output format.

### 4.2 Creator

- Develop a distinct content angle and creative concept.
- Apply the selected category's visual identity and creative direction.
- Produce English (Malaysia-localized) headline, supporting copy, caption, CTA, and relevant hashtags.
- Specify composition, visual hierarchy, image treatment, and format-specific guidance.
- Avoid inventing product details or campaign claims.

### 4.3 Editor

- Check product facts, model specificity, compatibility, dates, prices, and promotion terms.
- Check English grammar, clarity, tone, and Malaysian-market relevance.
- Confirm category and format values are allowed.
- Check brand affiliation, intellectual-property, asset-rights, and misleading-claim risks.
- Validate the final JSON structure and required fields.
- Return a review-needed result when verification is incomplete; do not silently mark it as passed.

These responsibilities are sequential stages in one agent workflow. They do not require separate agent deployments in V1.0.

## 5. Canonical category configuration

The source of truth is [../kategori.md](../kategori.md), version 2.1.0.

| ID | Slug | Category |
|---|---|---|
| CAT-001 | `product` | Product |
| CAT-002 | `promotion` | Promotion |
| CAT-003 | `lifestyle` | Lifestyle |
| CAT-004 | `education` | Education |
| CAT-005 | `news` | News |
| CAT-006 | `comparison` | Comparison |
| CAT-007 | `tips` | Tips |

Category ID and category slug are distinct values. The canonical taxonomy must not be inferred from the older README mapping or from database column names.

## 6. Supported format configuration

V1.0 generation allowlist:

| Format ID | Instagram placement | Dimensions |
|---|---|---|
| `single_image` | Feed | 1080 × 1350 px, 4:5 |
| `story` | Story | 1080 × 1920 px, 9:16 |

Carousel, Reels, infographic, UGC, and other formats may remain in editorial reference material, but are not valid generation outputs for this version.

## 7. Market and language configuration

| Setting | Value |
|---|---|
| Market | Malaysia |
| Content locale | `en-MY` |
| Platform | Instagram |
| Currency | MYR only for verified Malaysia-market prices |
| Documentation language | Indonesian is permitted |
| Audience-facing copy | English |

Localization must not introduce unverified assumptions about local availability, pricing, promotions, warranty, financing, or services.

## 8. Generation pipeline

1. **Request interpretation:** identify topic, product, audience, objective, and any supplied evidence.
2. **Strategy:** select category, funnel stage, message, and supported format.
3. **Configuration assembly:** combine the global instructions with exactly one category direction and one format specification.
4. **Creative development:** generate the visual concept and production guidance.
5. **Copywriting:** create English audience-facing text and CTA.
6. **Editorial review:** check factual claims, sources, language, and compliance.
7. **JSON serialization:** produce the versioned output contract.
8. **Validation:** reject malformed or disallowed output; flag incomplete verification for human review.

## 9. Output contract boundary

The approved output contract has ten required top-level keys:

- `template_version`
- `brand`
- `request`
- `product`
- `creative`
- `copywriting`
- `format_specification`
- `assets`
- `compliance`
- `quality_control`

The exact nested fields, data types, required/optional/nullability rules, and enums are defined in the separate schema implementation phase. This architecture document does not invent those details.

## 10. Data and database integration boundary

The existing SQL example at [../contoh/public.md](../contoh/public.md) is a reference and is not changed in Phase 1.

Audit observation requiring a later data-contract decision:
- `make_webhook_categories.category` stores category slugs such as `product` and `comparison`.
- `make_webhook.category_id` references that `category` column, so despite its name, the current foreign-key value is a slug, not the canonical `CAT-NNN` identifier.
- Do not change this relationship or migrate existing records as part of documentation alignment.
- Phase 6 must decide whether to rename the field, introduce a true category ID, or explicitly preserve the legacy slug reference with clear mapping and migration safeguards.

Calendar, webhook, idempotency, retries, and publication status remain outside Phase 1.

## 11. Brand, factual, and publication safeguards

- Do not claim that the account is Apple-owned, official, or authorized unless independently verified and permitted.
- Prefer Apple Malaysia for local-market information, Apple Support for technical details, and Apple Newsroom for official announcements.
- Distinguish official announcements from media reporting, rumors, and speculation.
- Never fabricate product specifications, compatibility, pricing, availability, discounts, stock, dates, or customer testimonials.
- Preserve accurate product appearance and interface details in visual direction.
- Use assets only where the required usage rights and permissions exist.
- Generated content remains a draft until human approval.

## 12. V1.0 scope exclusions

- Automatic Instagram publishing or scheduling.
- Instagram Graph API integration.
- Database schema changes or migrations.
- SQL seed changes.
- Webhook implementation or delivery changes.
- Prompt runtime implementation.
- JSON schema implementation.
- Asset generation/storage pipeline.
- Admin dashboard, analytics, and campaign management.
- Separate autonomous Strategist, Creator, and Editor agents.

## 13. Phase gates

| Phase | Deliverable | Acceptance gate |
|---|---|---|
| 1 — Documentation Alignment | README, category alignment, architecture | One canonical taxonomy and unambiguous generator constraints |
| 2 — Prompt Architecture | Master Prompt and modular configs | One prompt can combine all 7 × 2 configurations |
| 3 — JSON Contract | Versioned schema and contract docs | Required fields, types, and enums are explicit |
| 4 — Content Generation | 14 category/format test cases | All combinations generate conforming drafts |
| 5 — Quality Assurance | Validation tests and reports | Schema, editorial, factual, and compliance checks pass |
| 6 — Database Integration | Mapping and integration changes | Migration-safe persistence and webhook verification |

**Phase 1 completion does not authorize or imply completion of Phases 2–6.**
