-- =========================================================
-- APPLE STORE CONTENT AUTOMATION
-- Schema and seed data
-- Execution order: tables -> categories -> calendar -> webhook
-- =========================================================

-- 1. CATEGORY MASTER
create table if not exists public.make_webhook_categories (
  category text not null,
  description text null,
  content_direction text null,
  ai_agent_focus text null,
  visual_direction text null,
  is_active boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  instruction text null,
  negative_prompt text null,
  constraint make_webhook_categories_pkey primary key (category)
);

-- 2. CONTENT CALENDAR
create table if not exists public.make_calendar (
  date date not null,
  "Visual Effects" text null,
  "Mood" text null,
  "Color Palette" text null,
  "Lighting" text null,
  constraint make_calendar_pkey primary key (date)
);

-- 3. WEBHOOK QUEUE
create table if not exists public.make_webhook (
  id uuid not null default gen_random_uuid(),
  image_url text null,
  caption text null,
  date date not null,
  "time" time without time zone not null,
  category_id text null,
  constraint make_webhook_pkey primary key (id),
  constraint make_webhook_category_id_fkey
    foreign key (category_id)
    references public.make_webhook_categories (category)
    on update cascade
    on delete set null,
  constraint make_webhook_date_fkey
    foreign key (date)
    references public.make_calendar (date)
);

-- 4. INDEXES
create index if not exists idx_make_webhook_category_id
  on public.make_webhook using btree (category_id);

create index if not exists idx_make_webhook_date
  on public.make_webhook using btree (date);

-- =========================================================
-- SEED DATA
-- =========================================================

-- 5. CATEGORY SEED
insert into public.make_webhook_categories (
  category,
  description,
  content_direction,
  ai_agent_focus,
  visual_direction,
  is_active,
  created_at,
  updated_at,
  instruction,
  negative_prompt
) values
(
  'comparison',
  'Kandungan perbandingan antara produk, model atau ciri Apple untuk membantu audiens memahami perbezaan dan memilih produk yang sesuai.',
  'Bandingkan dua atau lebih produk atau ciri berdasarkan spesifikasi dan kegunaan sebenar. Gunakan jadual atau poin ringkas, terangkan perbezaan utama, kesesuaian pengguna dan rumusan neutral. Elakkan dakwaan prestasi tanpa sumber.',
  'AI Comparison Agent: menyelidik spesifikasi rasmi, mengenal pasti perbezaan yang relevan, memadankan ciri dengan keperluan pengguna dan menghasilkan perbandingan yang adil serta mudah difahami.',
  'Visual perbandingan dua bahagian atau susun atur bersebelahan. Paparkan produk yang dibandingkan pada skala dan sudut yang konsisten, label ringkas untuk ciri utama dan ruang visual yang kemas. Kekalkan rupa produk yang tepat.',
  true,
  '2026-11-15 04:27:51.159869+00',
  '2026-11-15 04:34:38.264806+00',
  'Gunakan spesifikasi dan maklumat produk daripada sumber rasmi Apple atau sumber yang boleh disahkan. Nyatakan model dan generasi produk dengan tepat. Bandingkan ciri yang setara dalam format yang mudah difahami, jelaskan perbezaan sebenar serta siapa yang mungkin mendapat manfaat daripada setiap pilihan. Kekalkan nada objektif dan adil. Jika maklumat tidak tersedia atau tidak dapat disahkan, nyatakan batasan tersebut dan jangan membuat andaian. Tulis dalam Bahasa Melayu Malaysia yang semula jadi.',
  'Jangan reka atau mengubah spesifikasi, skor ujian, harga, keputusan benchmark atau dakwaan prestasi. Elakkan perbandingan yang tidak setara, maklumat lapuk tanpa konteks, dakwaan mutlak seperti terbaik untuk semua orang, bahasa berat sebelah, merendahkan jenama pesaing, ciri yang tidak wujud, label salah, teks kabur, produk terherot, reka bentuk model bercampur dan watermark.'
),
(
  'education',
  'Kandungan pendidikan yang menerangkan ciri, teknologi, fungsi dan ekosistem Apple dengan bahasa yang mudah difahami.',
  'Pilih satu topik atau ciri Apple bagi setiap hantaran. Terangkan maksudnya, cara ia berfungsi, manfaat praktikal dan contoh penggunaan. Susun maklumat daripada asas kepada langkah atau fakta penting.',
  'AI Education Agent: menyemak fakta teknikal, memudahkan konsep Apple, membina penerangan langkah demi langkah dan memastikan kandungan tepat untuk pengguna baharu serta sedia ada.',
  'Visual editorial pendidikan dengan hierarki maklumat jelas, close-up ciri atau antara muka yang relevan, anotasi minimal dan susun atur langkah demi langkah. Pastikan teks pada visual ringkas dan mudah dibaca.',
  true,
  '2026-11-15 04:27:51.159869+00',
  '2026-11-15 04:34:38.264806+00',
  'Terangkan satu konsep, ciri atau teknologi Apple bagi setiap kandungan. Mulakan dengan penerangan mudah, kemudian huraikan cara penggunaan dan manfaat praktikal. Pastikan nama ciri, langkah, tetapan, keserasian model dan versi sistem operasi adalah tepat serta disahkan. Gunakan istilah teknikal hanya apabila perlu dan terangkan maksudnya. Susun penerangan secara berperingkat supaya mudah diikuti oleh pengguna baharu. Tulis dalam Bahasa Melayu Malaysia yang jelas.',
  'Jangan berikan fakta teknikal yang tidak disahkan, langkah tetapan yang direka, nama menu yang salah, keserasian palsu atau fungsi yang tidak wujud. Elakkan penerangan mengelirukan, jargon tanpa penjelasan, arahan yang tidak lengkap, tangkapan antara muka palsu, teks kecil atau tidak boleh dibaca, ikon salah, susun atur berserabut dan watermark.'
),
(
  'lifestyle',
  'Kandungan yang menunjukkan bagaimana produk dan ekosistem Apple digunakan dalam rutin harian, kerja, pembelajaran, kreativiti dan hiburan.',
  'Bina cerita situasi harian yang relevan seperti bekerja, belajar, melancong, merakam kenangan atau berkarya. Tunjukkan bagaimana produk Apple menyokong aktiviti tersebut secara semula jadi, bukan sekadar menyenaraikan spesifikasi.',
  'AI Lifestyle Agent: menjana idea penceritaan, senario penggunaan dan manfaat berasaskan situasi sebenar dengan nada mesra, aspirasi dan dekat dengan kehidupan audiens Malaysia.',
  'Fotografi gaya hidup premium dan natural dalam suasana moden Malaysia. Produk digunakan secara realistik dalam aktiviti harian, dengan komposisi candid, ruang negatif dan suasana yang hangat.',
  true,
  '2026-11-15 04:27:51.159869+00',
  '2026-11-15 04:34:38.264806+00',
  'Bina naratif berdasarkan situasi harian yang munasabah dan relevan kepada audiens Malaysia seperti kerja, pembelajaran, perjalanan, kreativiti atau hiburan. Tunjukkan manfaat produk Apple melalui penggunaan sebenar dan bukannya dakwaan berlebihan. Pastikan senario, cara memegang peranti, aksesori dan interaksi kelihatan semula jadi. Kekalkan gaya premium, mesra dan aspirasi tanpa menjanjikan hasil yang tidak dapat dibuktikan. Tulis dalam Bahasa Melayu Malaysia.',
  'Elakkan situasi tidak realistik, penggunaan peranti yang salah, tangan atau jari cacat, anatomi tidak semula jadi, peranti terapung, perspektif mustahil, produk terherot, aksesori yang tidak serasi, logo atau butiran produk yang salah, gaya terlalu sarat, suasana palsu, dakwaan manfaat berlebihan dan watermark.'
),
(
  'news',
  'Kandungan berita dan kemas kini berkaitan Apple, produk, perisian, ciri baharu dan pengumuman rasmi berdasarkan sumber yang boleh dipercayai.',
  'Sampaikan satu berita atau kemas kini dengan tajuk jelas, ringkasan fakta, tarikh dan konteks. Utamakan pengumuman Apple atau sumber yang boleh disahkan. Bezakan fakta rasmi daripada khabar angin dan jangan bentangkan spekulasi sebagai fakta.',
  'AI News Agent: mengesan topik semasa, mengutamakan sumber rasmi dan boleh dipercayai, menyemak tarikh serta fakta, dan membezakan pengumuman rasmi daripada laporan atau spekulasi.',
  'Visual editorial berita yang bersih dan kontemporari. Gunakan imej produk atau elemen berkaitan berita yang tepat, tajuk pendek, tarikh atau konteks jika perlu, serta elakkan elemen sensasi.',
  true,
  '2026-11-15 04:27:51.159869+00',
  '2026-11-15 04:34:38.264806+00',
  'Sahkan berita melalui pengumuman Apple atau sumber yang boleh dipercayai sebelum menghasilkan kandungan. Semak tarikh penerbitan, tarikh kejadian, negara atau pasaran yang terlibat, nama produk dan butiran penting. Bezakan pengumuman rasmi, laporan media, khabar angin dan spekulasi dengan jelas. Jangan gunakan berita lama seolah-olah berita terkini. Jika fakta belum disahkan, jangan bentangkannya sebagai kepastian. Tulis ringkasan yang neutral dalam Bahasa Melayu Malaysia.',
  'Jangan cipta berita, tarikh, petikan, pengumuman, produk atau sumber. Jangan bentangkan khabar angin dan spekulasi sebagai fakta rasmi. Elakkan tajuk sensasi, maklumat lapuk yang dilabel terkini, konteks pasaran yang salah, imej produk yang tidak berkaitan, teks berita palsu, logo media rekaan dan watermark.'
),
(
  'product',
  'Kandungan pengenalan dan paparan produk Apple yang menonjolkan reka bentuk, ciri utama, manfaat dan pengalaman penggunaan.',
  'Fokus pada satu produk atau keluarga produk. Paparkan reka bentuk, ciri utama, manfaat kepada pengguna, pilihan atau keserasian yang relevan dan seruan tindakan yang sesuai. Sahkan spesifikasi menggunakan sumber rasmi Apple.',
  'AI Product Agent: mengesahkan nama model, spesifikasi dan ciri daripada sumber rasmi Apple, memilih manfaat utama dan menghasilkan penerangan produk yang jelas tanpa dakwaan tidak disahkan.',
  'Fotografi produk premium bergaya minimal dengan produk sebagai fokus utama, sudut yang menonjolkan reka bentuk, perincian material dan paparan ciri. Kekalkan warna, bentuk, port, kamera dan butiran model dengan tepat.',
  true,
  '2026-11-15 04:27:51.159869+00',
  '2026-11-15 04:34:38.264806+00',
  'Sahkan nama produk, model, generasi, warna, kapasiti, spesifikasi, ciri dan keserasian berdasarkan maklumat rasmi Apple. Fokus pada manfaat yang relevan kepada pengguna dan terangkan ciri tanpa melebih-lebihkan prestasi. Pastikan visual menggambarkan model produk yang betul dan tidak mengubah reka bentuk fizikalnya. Jangan mereka harga, stok, promosi atau jaminan. Gunakan Bahasa Melayu Malaysia yang menarik, tepat dan profesional.',
  'Jangan ubah atau mereka bentuk semula produk. Elakkan model, warna, saiz, kamera, port, butang, paparan, bahan atau aksesori yang tidak tepat. Jangan cipta spesifikasi, ciri, harga, stok, promosi atau jaminan. Elakkan produk pendua yang tidak diminta, perspektif cacat, pantulan tidak realistik, teks rawak, logo salah, produk tiruan dan watermark.'
),
(
  'promotion',
  'Kandungan kempen jualan, tawaran, diskaun dan promosi Apple Store Malaysia yang sah, tepat dan mempunyai tempoh serta terma yang jelas.',
  'Paparkan tawaran yang telah disahkan sahaja. Nyatakan produk yang terlibat, harga atau penjimatan jika disahkan, tempoh, kelayakan dan terma penting. Jangan cipta harga, stok, hadiah atau tarikh tamat promosi.',
  'AI Promotion Agent: menyusun maklumat kempen yang telah diluluskan, menyemak harga, tempoh dan terma, menonjolkan nilai tawaran serta mengelakkan sebarang maklumat promosi rekaan.',
  'Visual kempen komersial yang jelas dan menonjolkan tawaran yang telah disahkan. Susun produk, manfaat dan maklumat promosi dengan hierarki yang mudah diimbas; elakkan lencana, harga atau elemen tawaran yang tidak diberikan.',
  true,
  '2026-11-15 04:27:51.159869+00',
  '2026-11-15 04:34:38.264806+00',
  'Gunakan hanya butiran promosi yang diberikan atau telah disahkan: nama produk, harga, harga asal jika sah, jumlah penjimatan, tempoh, kelayakan, stok dan terma. Semak pengiraan harga serta diskaun sebelum diterbitkan. Paparkan syarat penting dengan jelas dan jangan mengelirukan pelanggan. Jika sesuatu butiran belum diberikan, jangan mereka atau menganggarkannya; tinggalkan butiran tersebut dan minta pengesahan. Gunakan seruan tindakan yang jelas dan Bahasa Melayu Malaysia.',
  'Jangan reka harga, diskaun, kod promosi, hadiah, stok, tarikh tamat, kelayakan atau terma. Elakkan harga asal palsu, pengiraan penjimatan salah, dakwaan tawaran terhad tanpa bukti, jaminan hasil, syarat tersembunyi dan seruan tindakan mengelirukan. Jangan tambah lencana jualan, teks, logo, produk atau elemen promosi yang tidak dibekalkan. Elakkan teks cacat dan watermark.'
),
(
  'tips',
  'Kandungan tip, panduan ringkas dan tutorial praktikal untuk membantu pengguna memanfaatkan produk, ciri dan aplikasi Apple.',
  'Berikan satu tip yang boleh terus dicuba. Gunakan langkah bernombor atau arahan ringkas, nyatakan model atau versi perisian jika berkaitan, dan terangkan hasil atau manfaat tip tersebut.',
  'AI Tips Agent: mengenal pasti tip yang berguna, mengesahkan keserasian model dan versi perisian, menyusun langkah yang tepat dan menghasilkan panduan ringkas yang mudah diikuti.',
  'Visual tutorial ringkas dengan close-up peranti atau tangkapan antara muka yang relevan, langkah bernombor, penunjuk minimal dan hasil yang jelas. Pastikan paparan antara muka sepadan dengan peranti dan versi perisian.',
  true,
  '2026-11-15 04:27:51.159869+00',
  '2026-11-15 04:34:38.264806+00',
  'Berikan satu tip praktikal yang boleh dilaksanakan oleh pengguna. Sahkan langkah, nama menu, tetapan, model yang disokong dan versi iOS, iPadOS, macOS atau watchOS yang berkaitan. Susun arahan mengikut turutan sebenar dan jangan melangkau langkah penting. Nyatakan jika fungsi bergantung pada model, wilayah, bahasa atau versi perisian. Pastikan tip selamat, tepat dan mudah diuji. Tulis dalam Bahasa Melayu Malaysia yang ringkas.',
  'Jangan reka fungsi, langkah, tetapan, nama menu atau pintasan. Elakkan arahan yang tidak serasi dengan model atau versi sistem operasi, langkah yang tidak lengkap, tip berisiko, maklumat lapuk dan hasil yang dijanjikan tanpa asas. Jangan paparkan antara muka, ikon, label atau tangkapan skrin yang tidak tepat. Elakkan teks kecil, langkah bercelaru dan watermark.'
);

-- 6. CALENDAR SEED
-- Generates all dates from 1 to 30 November 2026.
-- Visual direction is assigned by date range to avoid duplicate rows.
insert into public.make_calendar (
  date,
  "Visual Effects",
  "Mood",
  "Color Palette",
  "Lighting"
)
select
  calendar_date::date,
  case
    when extract(day from calendar_date) = 1 then
      'Clean reflections, subtle glass highlights, soft depth of field, refined product shadows'
    when extract(day from calendar_date) between 2 and 8 then
      'Minimal 3D depth, crisp edges, soft gradients, subtle motion-inspired light trails'
    when extract(day from calendar_date) between 9 and 15 then
      'Macro detail, floating composition, translucent layers, precise product highlights'
    when extract(day from calendar_date) between 16 and 22 then
      'Natural environmental depth, realistic reflections, gentle bokeh, cinematic transitions'
    when extract(day from calendar_date) between 23 and 29 then
      'Elegant festive accents, soft glow, layered composition, restrained sparkle effects'
    else
      'Sculpted light gradients, polished reflections, clean negative space, subtle depth'
  end,
  case
    when extract(day from calendar_date) = 1 then
      'Calm, premium, confident, minimalist'
    when extract(day from calendar_date) between 2 and 8 then
      'Modern, innovative, energetic, optimistic'
    when extract(day from calendar_date) between 9 and 15 then
      'Precise, intelligent, sophisticated, focused'
    when extract(day from calendar_date) between 16 and 22 then
      'Warm, human, inspiring, connected'
    when extract(day from calendar_date) between 23 and 29 then
      'Joyful, welcoming, celebratory, premium'
    else
      'Fresh, forward-looking, refined, aspirational'
  end,
  case
    when extract(day from calendar_date) = 1 then
      'Silver, graphite, soft white, cool grey'
    when extract(day from calendar_date) between 2 and 8 then
      'Midnight black, electric blue, ice white, silver'
    when extract(day from calendar_date) between 9 and 15 then
      'Titanium, deep navy, mist grey, clean white'
    when extract(day from calendar_date) between 16 and 22 then
      'Warm beige, natural wood, soft blue, off-white'
    when extract(day from calendar_date) between 23 and 29 then
      'Champagne, warm gold, deep burgundy, ivory'
    else
      'Space grey, pale lavender, cloud white, muted blue'
  end,
  case
    when extract(day from calendar_date) = 1 then
      'Soft diffused studio lighting, balanced highlights, gentle shadows'
    when extract(day from calendar_date) between 2 and 8 then
      'High-key studio lighting, cool rim light, controlled specular highlights'
    when extract(day from calendar_date) between 9 and 15 then
      'Directional softbox lighting, precise edge highlights, low-contrast shadows'
    when extract(day from calendar_date) between 16 and 22 then
      'Warm natural window light, soft ambient fill, realistic gentle shadows'
    when extract(day from calendar_date) between 23 and 29 then
      'Warm golden-hour glow, diffused highlights, soft cinematic shadows'
    else
      'Cool softbox lighting, subtle backlight, clean reflective highlights'
  end
from generate_series(
  date '2026-11-01',
  date '2026-11-30',
  interval '1 day'
) as calendar_date;

-- 7. WEBHOOK SEED
insert into public.make_webhook (
  id,
  image_url,
  caption,
  date,
  "time",
  category_id
) values (
  '77e4b463-e1c4-4065-a797-24cfbb597e73',
  'https://example.com/3.jpg',
  'Caption 3',
  '2026-11-15',
  '19:00:00',
  'education'
);
