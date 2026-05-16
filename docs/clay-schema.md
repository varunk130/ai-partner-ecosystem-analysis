# Clay Enrichment Schema

`scripts/generate_clay_intel.py` expects rows in the shape below. Use this as the source of truth when configuring a Clay table or importing from another vendor.

## Required fields

| Field | Type | Example |
|---|---|---|
| `company_name` | string | `"Acme AI"` |
| `domain` | string (hostname) | `"acme.ai"` |

## Optional fields

| Field | Type | Default if missing | Notes |
|---|---|---|---|
| `hq_country` | string | `null` | ISO-3166 alpha-2 preferred (`"US"`) |
| `employee_count` | integer | `null` | Latest known headcount |
| `funding_total_usd` | integer | `null` | Cumulative disclosed funding |
| `last_funding_round` | string | `null` | e.g. `"Series B"` |
| `categories` | string[] | `[]` | Free-form tags |
| `linkedin_url` | string | `null` | Used for de-dup |
| `crunchbase_url` | string | `null` | Used for de-dup |

## Minimal example

```json
{
  "company_name": "Acme AI",
  "domain": "acme.ai",
  "hq_country": "US",
  "employee_count": 80,
  "funding_total_usd": 25000000,
  "last_funding_round": "Series A",
  "categories": ["LLM tooling", "Developer tools"]
}
```

## CSV input

The script also accepts CSV with the same column names. Multi-value fields (`categories`) should be pipe-delimited: `"LLM tooling|Developer tools"`.

## What the script does on bad rows

- Missing required field → row is skipped, logged to stderr.
- Unknown field → silently ignored.
- Empty optional field → treated as `null`, never as an empty string.
