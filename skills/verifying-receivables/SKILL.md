---
name: verifying-receivables
description: Verify incoming Trio payments, confirm whether a Pix or boleto arrived, and total what a payer sent in a period.
---

# Verifying receivables in Trio

Use the Trio MCP tools. Every tool is read-only.

## Choose the tool

- One incoming payment by `external_id` or Pix `end_to_end_id`: `search_collecting_documents`. It returns every stage of the document and the payer.
- Everything received from one CPF or CNPJ in a period: `list_collecting_documents_by_tax_number`, with `from_datetime`, `to_datetime` and `tax_number`.
- A filtered period listing, for example Pix received this week: `list_collecting_documents`, across every account or one `bank_account_id`. Optional filters: `status`, `type`, `ref_type`, `tax_number`.

Do not list a whole period and scan it when the user gave you an identifier or a tax number. Search instead.

## Workflow

1. Call `list_entities` first when you need an entity or account filter.
2. Run the chosen tool. For listings, walk every page (`metadata.before` / `metadata.after`) before you total or conclude.
3. Answer arrival questions from the document status: `settled` means the money arrived. `created`, `confirmed` and `kyc` mean it has not settled yet. Say which one it is, with the amount and the payer.
4. Checking a spreadsheet against received payments: match on `external_id` first, then on amount and date, and flag every entry that does not match.

## Rules

- Amounts come in cents. Divide by 100 and format as Brazilian reais, for example `R$ 50.000,00`.
- Dates and times are ISO 8601. State the exact period you used.
- CPFs arrive masked. Never try to reconstruct the missing digits. CNPJs are returned in full.
- A missing document is not proof the payer never paid. Say what you searched, in which period, and suggest checking the identifier for typos.
