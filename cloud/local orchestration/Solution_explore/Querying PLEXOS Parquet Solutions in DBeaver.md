# Querying PLEXOS Parquet Solutions in DBeaver (Community Edition) with DuckDB

This guide walks you from a fresh DBeaver install to running queries like:

```
Parent | Collection | Child | Category | Property | Band | Datetime | Value | Units
```

It uses **DBeaver Community** + **DuckDB**. No Pro license required.

---

## What you’ll end up with

- A persistent **DuckDB database file** (so your setup persists between sessions).
- A set of **views** that read your PLEXOS Parquet files in place.
- A single, human-readable **`v_facts`** view that exposes the data in the “PLEXOS way” (phase, period type, parent/child, property, band, timestamp, value, units).
- A few tiny helper queries to explore and sanity-check.

---

## Prerequisites (5 minutes)

1. **Install DBeaver Community** (standard installer).

2. **Have a PLEXOS Parquet Solution Folder**
   Unzip or copy the solution so that the folder contains subfolders like:

   ```
   attribute/
   attributedata/
   class/
   object/
   period/
   fullkeyinfo/
   data/            (contains parquet files in subfolders)
   ```

   (Other subfolders like `category/`, `phase/`, etc. are fine too.)

3. **Create a working folder** (no hard-coded paths)

   - Windows: `C:\Users\<you>\Documents\dbeaver_plexos\`
   - macOS: `/Users/<you>/Documents/dbeaver_plexos/`
   - Linux: `/home/<you>/Documents/dbeaver_plexos/`

> You’ll point DBeaver to save your DuckDB file _inside_ this folder.
> You will also paste your **solution root path** in one line of SQL (marked below).

---

## Step 1 — Create a DuckDB connection (persistent file)

1. Open **DBeaver**.
2. **Database → New Database Connection**.
3. Search for **DuckDB** and select it.

   - If prompted to download the driver, click **Download**.

4. In **Path / Database file**, choose:

   - Windows: `C:\Users\<you>\Documents\dbeaver_plexos\plexos.duckdb`
   - macOS/Linux: `~/Documents/dbeaver_plexos/plexos.duckdb` (use the **Browse** button to avoid typos)

5. Click **Finish**.
   You should now see the new connection in the **Database Navigator**.

---

## Step 2 — Open an SQL Editor on the DuckDB connection

- Right-click your new **DuckDB** connection → **SQL Editor → New SQL Script**.

We’re going to paste **one script** that:

- creates a schema,
- points views at your Parquet files,
- builds a single “facts” view for easy querying.

---

## Step 3 — Paste this entire script (edit only ONE line)

**Find the line that says “EDIT THIS LINE ONLY” and insert your solution folder path** (the folder that contains `data/`, `fullkeyinfo/`, `period/`, etc.).

Then run the script. In DBeaver you can run everything with **Alt+X (Execute Script)** or select all and **Ctrl/Cmd+Enter**.

```sql
-- =========================================================
-- PLEXOS Parquet setup for DBeaver (Community) + DuckDB
-- One-time registration: views + a single "facts" view
-- =========================================================

-- Use a dedicated schema
CREATE SCHEMA IF NOT EXISTS plexos;
SET schema 'plexos';

-- ---------------------------------------------------------
-- 0) Tell DuckDB where your solution folder is (ROOT macro)
--    EDIT THIS LINE ONLY: put the absolute path to the solution root
--    Examples:
--      Windows: 'C:/Users/yourname/Documents/PLEXOS_Solution'
--      macOS  : '/Users/yourname/Documents/PLEXOS_Solution'
--      Linux  : '/home/yourname/Documents/PLEXOS_Solution'
--    Use forward slashes even on Windows to avoid escaping.
-- ---------------------------------------------------------
CREATE OR REPLACE MACRO ROOT() AS 'C:/Users/yourname/Documents/PLEXOS_Solution';

-- Quick sanity check (optional):
-- SELECT ROOT();

-- ---------------------------------------------------------
-- 1) Register core views that read Parquet in place
--    (You can rerun this script safely; it uses OR REPLACE.)
-- ---------------------------------------------------------

-- Dictionaries / metadata (create the ones your solution has)
CREATE OR REPLACE VIEW attribute       AS SELECT * FROM read_parquet(ROOT() || '/attribute/Attribute.parquet');
CREATE OR REPLACE VIEW attributedata   AS SELECT * FROM read_parquet(ROOT() || '/attributedata/AttributeData.parquet');
CREATE OR REPLACE VIEW "class"         AS SELECT * FROM read_parquet(ROOT() || '/class/Class.parquet');
CREATE OR REPLACE VIEW object          AS SELECT * FROM read_parquet(ROOT() || '/object/Object.parquet');
CREATE OR REPLACE VIEW unit            AS SELECT * FROM read_parquet(ROOT() || '/unit/Unit.parquet')            -- if present
                                         UNION ALL SELECT * FROM (SELECT * FROM read_parquet(ROOT() || '/unit/*.parquet')) WHERE 1=0;
CREATE OR REPLACE VIEW period          AS SELECT * FROM read_parquet(ROOT() || '/period/Period.parquet');
CREATE OR REPLACE VIEW aggregatedseries AS SELECT * FROM read_parquet(ROOT() || '/aggregatedseries/AggregatedSeries.parquet');
CREATE OR REPLACE VIEW fullkeyinfo     AS SELECT * FROM read_parquet(ROOT() || '/fullkeyinfo/FullKeyInfo.parquet');
CREATE OR REPLACE VIEW membershipinfo  AS SELECT * FROM read_parquet(ROOT() || '/membershipinfo/MembershipInfo.parquet')
                                         UNION ALL SELECT * FROM (SELECT * FROM read_parquet(ROOT() || '/membershipinfo/*.parquet')) WHERE 1=0;

-- Time-series may be sharded by subfolders; read them all
CREATE OR REPLACE VIEW data AS
SELECT * FROM read_parquet(ROOT() || '/data/**');

-- ---------------------------------------------------------
-- 2) Single “facts” view in PLEXOS terms
--    (Properties are defined on memberships; fullkeyinfo names them.)
-- ---------------------------------------------------------
CREATE OR REPLACE VIEW v_facts AS
SELECT
  k."ParentObjectName"                                        AS parent_name,
  k."CollectionName"                                          AS collection_name,     -- e.g. System.Generators
  k."ChildObjectName"                                         AS child_name,
  COALESCE(k."ChildObjectCategoryName", k."ParentObjectCategoryName", '-') AS category_name,
  k."PropertyName"                                            AS property_name,       -- e.g. Generation, Load, Flow
  k."BandId"                                                  AS band_id,
  k."UnitValue"                                               AS units,               -- e.g. MW
  k."PhaseName"                                               AS phase_name,          -- ST, MT, LT, PASA
  k."PeriodTypeName"                                          AS period_type_name,    -- Interval, Monthly, etc.
  k."TimesliceName"                                           AS timeslice_name,
  k."ModelName"                                               AS model_name,
  k."SampleName"                                              AS sample_name,

  p."StartDate"                                               AS datetime,
  p."EndDate"                                                 AS period_end,

  d."Value"                                                   AS value,

  -- technical keys (handy for debugging)
  d."SeriesId"                                                AS series_id,
  d."PeriodId"                                                AS period_id,
  d."dataFileId"                                              AS data_file_id
FROM data d
LEFT JOIN fullkeyinfo k
       ON d."SeriesId"   = k."SeriesId"
      AND d."dataFileId" = k."DataFileId"     -- keeps mapping precise across files
LEFT JOIN period p
       ON d."PeriodId"   = p."PeriodId";

-- ---------------------------------------------------------
-- 3) Quick look (optional)
-- ---------------------------------------------------------
-- SELECT * FROM v_facts LIMIT 20;

-- ---------------------------------------------------------
-- 4) Handy exploration helpers (optional)
-- ---------------------------------------------------------
CREATE OR REPLACE VIEW v_list_properties AS
SELECT DISTINCT property_name FROM v_facts WHERE property_name IS NOT NULL ORDER BY 1;

CREATE OR REPLACE VIEW v_list_collections AS
SELECT DISTINCT collection_name FROM v_facts WHERE collection_name IS NOT NULL ORDER BY 1;

-- Time range (for sensible date filters)
CREATE OR REPLACE VIEW v_time_span AS
SELECT MIN(datetime) AS min_datetime, MAX(datetime) AS max_datetime FROM v_facts;
```

### What to expect

- After you run it, you’ll see the **`plexos`** schema in the left tree with the new views, including **`v_facts`**.
- `v_facts` is your go-to table for querying.

---

## Step 4 — Sanity checks (2 minutes)

Paste and run these **read-only** checks to get your bearings:

```sql
-- 1) Do I have readable rows?
SELECT * FROM plexos.v_facts LIMIT 20;

-- 2) What properties (metrics) exist?
SELECT * FROM plexos.v_list_properties LIMIT 100;

-- 3) What collections exist?
SELECT * FROM plexos.v_list_collections LIMIT 100;

-- 4) Time coverage
SELECT * FROM plexos.v_time_span;
```

---

## Step 5 — Practical query examples

> Adjust filters to your solution (use the lists above to pick valid values).
> If a filter is too strict, comment it out and re-run.

### A) Generator output for one day (ST, hourly/interval)

```sql
SELECT
  parent_name   AS "Parent",
  collection_name AS "Collection",
  child_name    AS "Child",
  category_name AS "Category",
  property_name AS "Property",
  band_id       AS "Band",
  datetime      AS "Datetime",
  value         AS "Value",
  units         AS "Units"
FROM plexos.v_facts
WHERE property_name    = 'Generation'
  AND collection_name  = 'System.Generators'
  AND phase_name       = 'ST'           -- change if needed
  AND period_type_name = 'Interval'     -- or 'Monthly', etc.
  AND datetime >= TIMESTAMP '2023-05-07 00:00:00'
  AND datetime <  TIMESTAMP '2023-05-08 00:00:00'
  AND band_id = 1                        -- drop this line if bands not used
ORDER BY "Child", "Datetime";
```

### B) Total system generation (sum across all generators, by timestamp)

```sql
SELECT
  datetime,
  SUM(value) AS total_generation_mw
FROM plexos.v_facts
WHERE property_name    = 'Generation'
  AND collection_name  = 'System.Generators'
  AND phase_name       = 'ST'
  AND period_type_name = 'Interval'
GROUP BY datetime
ORDER BY datetime;
```

### C) Top generators by average output (quick ranking)

```sql
SELECT
  child_name,
  AVG(value) AS avg_gen_mw
FROM plexos.v_facts
WHERE property_name   = 'Generation'
  AND collection_name = 'System.Generators'
  AND phase_name      = 'ST'
GROUP BY child_name
ORDER BY avg_gen_mw DESC
LIMIT 10;
```

### D) Filter by name pattern (LIKE supports wildcards)

```sql
SELECT *
FROM plexos.v_facts
WHERE property_name   = 'Flow'
  AND collection_name = 'System.Lines'
  AND child_name LIKE '%COI%'         -- contains "COI"
ORDER BY child_name, datetime
LIMIT 500;
```

---

## Exporting results (CSV/Excel) — optional

1. Run a query.
2. In the results grid, right-click → **Export Resultset**.
3. Choose **CSV** or **XLSX** and follow the wizard.
4. Consider exporting to your `Documents\dbeaver_plexos\` folder for consistency.

---

## Troubleshooting

| Symptom                     | Likely cause           | Fix                                                                                                          |
| --------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| `IO Error: No files found…` | `ROOT()` path is wrong | Edit the `CREATE MACRO ROOT()` line; ensure the folder contains `data/`, `period/`, `fullkeyinfo/`           |
| 0 rows returned             | Filters too strict     | Remove `band_id` line; try a different `phase_name`/`period_type_name`; check `v_time_span` for actual dates |
| “DuckDB / driver not found” | Driver not downloaded  | Reopen connection dialog → **Edit Driver Settings** → **Download/Update**                                    |
| “Catalog/Schema ambiguity”  | Wrong schema           | Run `SET schema 'plexos';` at the top of your editor tab                                                     |

---

## FAQ

**Q: Can I reuse this for another solution?**
Yes. Duplicate your DuckDB connection _or_ reuse it:

- Run the script again, but **change the one `ROOT()` line** to the new solution folder.
- All views will repoint automatically (`CREATE OR REPLACE`).

**Q: Can I avoid editing paths each time?**
The script isolates your path to **one line** (the macro). That’s the simplest, cross-platform way in DuckDB/DBeaver.

**Q: Where do results “live”?**
We don’t copy data — we read Parquet in place. Your DuckDB file just stores the **view definitions**.
