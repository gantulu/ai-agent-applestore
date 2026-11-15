# Apple Content Categories

Dokumentasi kategori dan metadata konten seputar produk, ekosistem, teknologi, dan layanan Apple.

## 1. Category Metadata

| Field | Description | Example |
|---|---|---|
| `id` | Identifier unik kategori | `CAT-001` |
| `slug` | Identifier URL kategori | `comparison` |
| `name` | Nama kategori | `Comparison` |
| `description` | Deskripsi kategori | Perbandingan produk Apple |
| `focus` | Fokus utama konten | Product Comparison |
| `content_type` | Jenis konten | Editorial |
| `keywords` | Kata kunci kategori | iPhone, MacBook, iPad |
| `status` | Status kategori | `active` |
| `sort_order` | Urutan kategori | `1` |

## 2. Category List

| ID | Slug | Category | Focus | Keywords | Status |
|---|---|---|---|---|---|
| CAT-001 | `comparison` | Comparison | Perbandingan produk Apple | iPhone, MacBook, iPad, Comparison | Active |
| CAT-002 | `education` | Education | Edukasi dan pengetahuan Apple | Apple Ecosystem, Technology, Guide | Active |
| CAT-003 | `lifestyle` | Lifestyle | Gaya hidup menggunakan produk Apple | Productivity, Creativity, Daily Life | Active |
| CAT-004 | `news` | News | Berita dan update terbaru Apple | Apple News, Updates, Events | Active |
| CAT-005 | `product` | Product | Pengenalan dan keunggulan produk | iPhone, Mac, iPad, Apple Watch | Active |
| CAT-006 | `promotion` | Promotion | Promo, diskon dan penawaran khusus | Discount, Deals, Offers | Active |
| CAT-007 | `tips` | Tips | Tips dan trik penggunaan produk Apple | Tutorial, How-to, Tricks | Active |

## 3. Category Details

### CAT-001 — Comparison

- **Focus:** Perbandingan produk Apple
- **Content Type:** Comparative Editorial
- **Keywords:** iPhone Comparison, MacBook Comparison, iPad Comparison
- **Examples:** iPhone vs iPhone, MacBook Air vs Pro

### CAT-002 — Education

- **Focus:** Edukasi dan pengetahuan Apple
- **Content Type:** Educational
- **Keywords:** Apple Ecosystem, Technology, Knowledge
- **Examples:** Mengenal iCloud, Apple Intelligence

### CAT-003 — Lifestyle

- **Focus:** Gaya hidup menggunakan produk Apple
- **Content Type:** Lifestyle Editorial
- **Keywords:** Productivity, Creativity, Daily Life
- **Examples:** Apple untuk produktivitas dan kreativitas

### CAT-004 — News

- **Focus:** Berita dan update terbaru Apple
- **Content Type:** News
- **Keywords:** Apple News, Updates, Events
- **Examples:** Peluncuran produk dan update iOS

### CAT-005 — Product

- **Focus:** Pengenalan dan keunggulan produk
- **Content Type:** Product Editorial
- **Keywords:** iPhone, Mac, iPad, Apple Watch, AirPods
- **Examples:** Product Review dan Product Features

### CAT-006 — Promotion

- **Focus:** Promo, diskon dan penawaran khusus
- **Content Type:** Promotional
- **Keywords:** Discount, Deals, Offers
- **Examples:** Special Deals dan Product Bundling

### CAT-007 — Tips

- **Focus:** Tips dan trik penggunaan produk Apple
- **Content Type:** Tutorial / How-to
- **Keywords:** Tips, Tricks, Tutorial, Guide
- **Examples:** Tips iPhone dan tutorial macOS

## 4. Metadata Standards

| Property | Format |
|---|---|
| ID | Unique String |
| Slug | Lowercase + kebab-case |
| Name | String |
| Description | Text |
| Focus | String |
| Content Type | String |
| Keywords | Array of Strings |
| Status | `active` / `inactive` |
| Sort Order | Integer |

## 5. Summary

- Total Categories: **7**
- Metadata: **9 fields**
- Default Status: `active`
- Category Identifier: `CAT-001` – `CAT-007`
- Slug Convention: Lowercase
