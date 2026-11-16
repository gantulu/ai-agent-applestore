# Apple Instagram AI Agent

Dokumentasi utama untuk AI Agent pembuat konten Instagram produk dan ekosistem Apple dengan target audiens Malaysia.

## Project baseline

| Item | Standard |
|---|---|
| Project | Apple Instagram AI Agent |
| Market | Malaysia |
| Platform | Instagram |
| Content language | English (Malaysia audience; `en-MY`) |
| AI role | Hybrid — Strategist, Creator, Editor |
| Primary categories | 7 |
| Supported generation formats | `single_image`, `story` |
| Output contract | Strict JSON |
| Output schema version | `1.0.0` |

> **Brand and affiliation:** “Apple Store Malaysia” is the project/account context. Do not claim to be Apple, an Apple-owned channel, an Apple Authorized Reseller, or officially affiliated with Apple unless the relevant status and permission have been independently verified.

## Canonical content categories

The approved category taxonomy is defined in [kategori.md](./kategori.md), version 2.1.0. Its identifiers are canonical for this project.

| Category ID | Slug | Category |
|---|---|---|
| CAT-001 | `product` | Product |
| CAT-002 | `promotion` | Promotion |
| CAT-003 | `lifestyle` | Lifestyle |
| CAT-004 | `education` | Education |
| CAT-005 | `news` | News |
| CAT-006 | `comparison` | Comparison |
| CAT-007 | `tips` | Tips |

Rules:
- Every content item has exactly one primary category.
- A secondary category is optional and limited to one.
- Category IDs and slugs must be treated as separate fields.
- Category selection is based on the primary editorial objective, not merely the featured product.
- Do not reuse the superseded category-ID mapping from older documentation.

## Supported Instagram formats

The AI generation system supports only these two format identifiers in V1.0:

| Format ID | Placement | Canvas |
|---|---|---|
| `single_image` | Instagram Feed | 4:5 portrait, 1080 × 1350 px |
| `story` | Instagram Story | 9:16 vertical, 1080 × 1920 px |

Other formats mentioned in the editorial taxonomy are reference material only. They are not valid generator output formats in V1.0.

## AI role and responsibilities

The Hybrid Agent performs three coordinated responsibilities:

1. **Strategist** — selects the content objective, audience angle, primary category, product focus, and format.
2. **Creator** — develops the creative concept, visual direction, headline, caption, CTA, and relevant hashtags.
3. **Editor** — checks factual support, English quality, category/format compliance, brand/legal safeguards, and output validity.

These are responsibilities within one agent and one generation workflow, not three separately deployed agents.

## Language and localization

- All generated audience-facing copy must be in English, localized for the Malaysia market (`en-MY`).
- Use Malaysian market context only when supported by verified information.
- Use MYR only when a Malaysia-specific price is supplied or verified.
- Do not translate product names, official feature names, or interface labels in ways that change their meaning.
- Documentation may remain in Indonesian; this does not change the English content-output requirement.

## Editorial and factual safeguards

- Prefer official Apple Malaysia pages for local product, price, availability, and market information.
- Use Apple Support for technical instructions, compatibility, and software behavior.
- Use Apple Newsroom for official announcements.
- Record specific source URLs and the date checked when factual claims require verification.
- Never invent specifications, prices, promotions, stock, launch dates, compatibility, testimonials, or performance claims.
- Treat rumors and third-party reporting as such; never present them as official Apple announcements.
- Do not imply official Apple affiliation or authorization without verification.
- Use visual, photographic, video, font, and music assets only when usage rights permit.

## Architecture

The approved modular architecture is documented in [docs/architecture.md](./docs/architecture.md).

The generation system is composed of:
- One global Master Prompt.
- One category-direction configuration containing seven categories.
- One format-specification configuration containing two supported formats.
- One strict JSON output contract.
- Validation and quality-control checks.

Category and format configurations must remain independent. Do not create separate master prompts for every category/format combination.

## Repository documentation

| Path | Purpose |
|---|---|
| `README.md` | Project baseline and entry point |
| `kategori.md` | Canonical seven-category taxonomy and visual/editorial guidance |
| `docs/architecture.md` | Approved V1.0 architecture and boundaries |
| `contoh/public.md` | Existing SQL schema/seed reference; not modified by Phase 1 |

## Implementation boundaries

Phase 1 aligns documentation only. It does not:
- Create or modify database tables, records, or migrations.
- Modify SQL seed data or webhook behavior.
- Implement prompts, JSON schemas, runtime code, or tests.
- Publish content to Instagram.
- Change secrets, integrations, deployment, or automation settings.

Those items require their own implementation phases and verification.

## Versioning

- Architecture baseline: Apple Instagram AI Agent V1.0.
- Category source: Apple Content Categories V2.1.0.
- Generation language: English (`en-MY`).
- Supported formats: `single_image`, `story`.
