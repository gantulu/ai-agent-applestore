# Apple Content Categories

Dokumentasi taxonomy untuk mengelompokkan konten seputar produk, ekosistem, teknologi, layanan, dan pengalaman menggunakan Apple.

Dokumen ini menjadi acuan konsisten dalam menentukan kategori, metadata, dan klasifikasi konten.

## 1. Overview

| Item | Value |
|---|---|
| Total categories | 7 |
| Metadata fields | 9 |
| Default status | `active` |
| Category ID format | `CAT-001` – `CAT-007` |
| Slug format | Lowercase kebab-case |

## 2. Category Metadata

Setiap kategori menggunakan sembilan field berikut.

| Field | Type | Required | Description | Example |
|---|---|---|---|---|
| `id` | String | Yes | Identifier unik kategori | `CAT-001` |
| `slug` | String | Yes | Identifier untuk URL | `comparison` |
| `name` | String | Yes | Nama kategori | `Comparison` |
| `description` | String | Yes | Penjelasan singkat kategori | Perbandingan produk Apple |
| `focus` | String | Yes | Fokus utama konten | Product comparison |
| `content_type` | String | Yes | Jenis atau format editorial | `comparative-editorial` |
| `keywords` | String[] | Yes | Kata kunci yang relevan | `["iPhone", "MacBook"]` |
| `status` | Enum | Yes | Status kategori | `active` |
| `sort_order` | Integer | Yes | Urutan tampilan kategori | `1` |

### Metadata example

Contoh representasi satu kategori:

```json
{
  "id": "CAT-001",
  "slug": "comparison",
  "name": "Comparison",
  "description": "Perbandingan produk Apple",
  "focus": "Product comparison",
  "content_type": "comparative-editorial",
  "keywords": ["iPhone", "MacBook", "iPad"],
  "status": "active",
  "sort_order": 1
}
```

## 3. Category List

| ID | Slug | Category | Focus | Content Type | Status |
|---|---|---|---|---|---|
| CAT-001 | `comparison` | Comparison | Perbandingan produk Apple | Comparative editorial | Active |
| CAT-002 | `education` | Education | Edukasi dan pengetahuan Apple | Educational | Active |
| CAT-003 | `lifestyle` | Lifestyle | Penggunaan Apple dalam kehidupan sehari-hari | Lifestyle editorial | Active |
| CAT-004 | `news` | News | Berita dan perkembangan terbaru Apple | News | Active |
| CAT-005 | `product` | Product | Informasi dan ulasan produk Apple | Product editorial | Active |
| CAT-006 | `promotion` | Promotion | Promo dan penawaran khusus | Promotional | Active |
| CAT-007 | `tips` | Tips | Panduan praktis penggunaan produk Apple | Tutorial / How-to | Active |

## 4. Category Details

### CAT-001 — Comparison

- **Description:** Perbandingan antara dua atau lebih produk, model, fitur, atau layanan Apple.
- **Focus:** Membantu pembaca memahami persamaan, perbedaan, dan trade-off.
- **Content type:** Comparative editorial.
- **Keywords:** iPhone comparison, MacBook comparison, iPad comparison.
- **Examples:** iPhone 16 vs iPhone 17; MacBook Air vs MacBook Pro.

### CAT-002 — Education

- **Description:** Konten edukasi yang menjelaskan konsep, teknologi, fitur, dan ekosistem Apple.
- **Focus:** Memberikan pemahaman dan pengetahuan yang bersifat informatif.
- **Content type:** Educational.
- **Keywords:** Apple ecosystem, technology, knowledge, explanation.
- **Examples:** Mengenal iCloud; memahami Apple Intelligence; cara kerja ekosistem Apple.

### CAT-003 — Lifestyle

- **Description:** Konten tentang pengalaman dan gaya hidup dengan menggunakan produk Apple.
- **Focus:** Produktivitas, kreativitas, pekerjaan, hiburan, dan aktivitas sehari-hari.
- **Content type:** Lifestyle editorial.
- **Keywords:** Productivity, creativity, daily life, work setup.
- **Examples:** Menggunakan iPad untuk bekerja; workflow kreator dengan Mac; Apple dalam aktivitas harian.

### CAT-004 — News

- **Description:** Informasi mengenai berita, pengumuman, acara, dan perkembangan terbaru Apple.
- **Focus:** Menyampaikan informasi aktual secara jelas dan berdasarkan sumber yang dapat diverifikasi.
- **Content type:** News.
- **Keywords:** Apple news, announcements, events, updates.
- **Examples:** Pengumuman produk baru; pembaruan iOS; informasi Apple Event.

### CAT-005 — Product

- **Description:** Konten yang membahas produk Apple secara spesifik.
- **Focus:** Pengenalan produk, spesifikasi, fitur, kelebihan, kekurangan, dan review.
- **Content type:** Product editorial.
- **Keywords:** iPhone, Mac, iPad, Apple Watch, AirPods, product review.
- **Examples:** Mengenal fitur iPhone; spesifikasi MacBook Air; review Apple Watch.

### CAT-006 — Promotion

- **Description:** Konten mengenai promosi, diskon, bundling, dan penawaran produk atau layanan Apple.
- **Focus:** Menyampaikan detail penawaran secara transparan.
- **Content type:** Promotional.
- **Keywords:** Promotion, discount, deals, offers, bundle.
- **Examples:** Promo pembelian iPhone; diskon aksesori; penawaran bundling.

### CAT-007 — Tips

- **Description:** Panduan praktis berupa langkah, trik, atau instruksi untuk menggunakan produk dan layanan Apple.
- **Focus:** Membantu pengguna menyelesaikan tugas atau menggunakan fitur secara lebih efektif.
- **Content type:** Tutorial / How-to.
- **Keywords:** Tips, tricks, tutorial, guide, how-to.
- **Examples:** Tips menghemat baterai iPhone; cara mengatur Focus Mode; shortcut macOS.

## 5. Content Classification Rules

Gunakan aturan berikut untuk menentukan kategori utama sebuah konten:

| Jika tujuan utama konten adalah... | Gunakan kategori |
|---|---|
| Membandingkan produk atau fitur | Comparison |
| Menjelaskan konsep atau teknologi | Education |
| Membahas pengalaman penggunaan dan gaya hidup | Lifestyle |
| Memberitakan pengumuman atau perkembangan terbaru | News |
| Mengulas atau memperkenalkan produk tertentu | Product |
| Menginformasikan penawaran atau diskon | Promotion |
| Memberikan langkah praktis atau tutorial | Tips |

### Classification guidelines

1. Tentukan kategori berdasarkan tujuan utama konten, bukan hanya produk atau kata kunci yang disebutkan.
2. Gunakan satu kategori sebagai kategori utama agar klasifikasi tetap konsisten.
3. Pilih kategori yang paling menggambarkan manfaat utama bagi pembaca.
4. Gunakan keywords untuk membantu pencarian dan pengelompokan, bukan sebagai pengganti kategori.
5. Jika sebuah konten tampak cocok untuk beberapa kategori, prioritaskan tujuan editorialnya.

### Distinction between similar categories

- **Education vs Tips:** Education menjelaskan pemahaman atau konsep; Tips memberikan langkah praktis untuk melakukan sesuatu.
- **Product vs Comparison:** Product membahas satu produk atau lini produk; Comparison membandingkan beberapa produk atau pilihan.
- **News vs Education:** News menyampaikan perkembangan aktual; Education menjelaskan topik secara konseptual dan tidak harus terkait berita terbaru.
- **Lifestyle vs Tips:** Lifestyle berfokus pada pengalaman atau pola penggunaan; Tips berfokus pada instruksi yang dapat diikuti.

## 6. Metadata Standards

| Property | Standard |
|---|---|
| `id` | String unik dan stabil; gunakan format `CAT-NNN` |
| `slug` | Lowercase kebab-case; unik dan tidak menggunakan spasi |
| `name` | Nama kategori yang ringkas dan mudah dikenali |
| `description` | Deskripsi singkat yang menjelaskan cakupan kategori |
| `focus` | Fokus editorial utama kategori |
| `content_type` | Label konsisten dalam format lowercase kebab-case |
| `keywords` | Array of strings; hindari duplikasi dan kata yang tidak relevan |
| `status` | Gunakan `active` atau `inactive` |
| `sort_order` | Integer positif untuk menentukan urutan tampilan |

### Naming conventions

- Jangan mengubah `id` kategori yang sudah digunakan sebagai referensi data.
- Gunakan slug yang konsisten dengan nama kategori dan pertahankan keunikannya.
- Gunakan istilah yang konsisten untuk `content_type`.
- Kategori nonaktif menggunakan status `inactive`; jangan menghapus kategori hanya untuk menyembunyikannya dari penggunaan aktif.
- Perubahan definisi kategori harus diperbarui di dokumen ini agar menjadi acuan bersama.

## 7. Summary

| Item | Total / Standard |
|---|---|
| Categories | **7** |
| Metadata fields | **9** |
| Default status | `active` |
| Category identifiers | `CAT-001` – `CAT-007` |
| Slug convention | Lowercase kebab-case |
| Primary classification | One primary category per content |

---

Dokumen ini merupakan baseline taxonomy kategori konten Apple. Perubahan jumlah kategori, identifier, atau struktur metadata sebaiknya dilakukan secara terkontrol agar konsistensi klasifikasi tetap terjaga.
