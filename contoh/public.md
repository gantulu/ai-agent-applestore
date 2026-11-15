create table public.make_calendar (
  date date not null,
  "Visual Effects" text null,
  "Mood" text null,
  "Color Palette" text null,
  "Lighting" text null,
  constraint make_calendar_pkey primary key (date)
) TABLESPACE pg_default;

create table public.make_webhook (
  id uuid not null default gen_random_uuid (),
  image_url text null,
  caption text null,
  date date not null,
  "time" time without time zone not null,
  category_id text null,
  constraint make_webhook_pkey primary key (id),
  constraint make_webhook_category_id_fkey foreign KEY (category_id) references make_webhook_categories (category) on update CASCADE on delete set null,
  constraint make_webhook_date_fkey foreign KEY (date) references make_calendar (date)
) TABLESPACE pg_default;

create index IF not exists idx_make_webhook_category_id on public.make_webhook using btree (category_id) TABLESPACE pg_default;

create table public.make_webhook_categories (
  category text not null,
  description text null,
  content_direction text null,
  ai_agent_focus text null,
  visual_direction text null,
  is_active boolean not null default true,
  created_at timestamp with time zone not null default now(),
  updated_at timestamp with time zone not null default now(),
  instruction text null,
  negative_prompt text null,
  constraint make_webhook_categories_pkey primary key (category)
) TABLESPACE pg_default;
