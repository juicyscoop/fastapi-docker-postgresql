CREATE TABLE IF NOT EXISTS public.aapl_daily
(
    date date NOT NULL,
    open double precision NOT NULL,
    high double precision NOT NULL,
    low double precision NOT NULL,
    close double precision NOT NULL,
    volume double precision NOT NULL,
    CONSTRAINT aapl_daily_pkey PRIMARY KEY (date)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.aapl_daily
    OWNER to postgres;