---
name: tracing-payments
description: Trace outgoing Trio payments by external ID, Pix end-to-end ID or payee tax number, and total what a payee received.
---

# Tracing payments in Trio

Use the Trio MCP tools. Every tool is read-only.

## Choose the tool

- One payment by `external_id` or Pix `end_to_end_id`: `search_payment_documents`. It returns every stage of the document and the payee.
- Everything sent to one CPF or CNPJ in a period: `list_payment_documents_by_tax_number`, with `from_datetime`, `to_datetime` and `tax_number`.
- A filtered period listing, for example payments over a threshold or with one status: `list_payment_documents`, across every account or one `bank_account_id`.

Do not list a whole period and scan it when the user gave you an identifier or a tax number. Search instead.

## Workflow

1. Call `list_entities` first when you need an entity or account filter.
2. Run the chosen tool. For listings, walk every page (`metadata.before` / `metadata.after`) before you total or conclude.
3. Report each document's status and stages in order. Explain the current stage in plain language: `settled` and `failed` are final; `created`, `confirmed` and `onhold` are not.
4. When comparing a batch against a supplier's history before approval, total what each payee usually receives in a comparable period and point out the outliers. The approval itself happens in the Trio App, never here.

## Rules

- Amounts come in cents. Divide by 100 and format as Brazilian reais, for example `R$ 50.000,00`.
- Dates and times are ISO 8601. State the exact period you used.
- CPFs arrive masked. Never try to reconstruct the missing digits. CNPJs are returned in full.
- If a search finds nothing, say so and name the identifier and period you searched. Do not widen the search silently.
