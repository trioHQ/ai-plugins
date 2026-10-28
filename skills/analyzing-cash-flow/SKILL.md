---
name: analyzing-cash-flow
description: Analyze Trio cash flow, daily position and period movements from the consolidated account statement.
---

# Analyzing cash flow in Trio

Use the Trio MCP tools. Every tool is read-only.

## Workflow

1. Call `list_entities`, then `list_bank_accounts` to find the account the question is about. If the question spans accounts, run the statement per account and combine the results.
2. Call `get_account_statement` with the account `id`, `from_datetime` and `to_datetime`. This is the first choice for cash flow, daily position and period reports: it returns every inflow and outflow with the running balance. Do not use the payment or receivable listings for cash flow.
3. Walk every page before you answer. Listings are paginated with `metadata.before` and `metadata.after` cursors. If you could not cover the whole period, say the answer is partial and name the covered range.
4. Total inflows and outflows separately, then give the net. Break the totals down by day or by counterparty only when the question asks for it.

## Rules

- Amounts come in cents. Divide by 100 and format as Brazilian reais, for example `R$ 50.000,00`.
- Dates and times are ISO 8601, for example `2026-10-01T00:00:00-03:00`. Default to the America/Sao_Paulo offset when the user gives plain dates, and state the exact period you used.
- `settled` and `failed` are final for payments and transfers. Do not count `failed` documents as movement; call out pending statuses (`created`, `confirmed`, `onhold`) separately.
- Reconciling against a spreadsheet: match on `external_id` first, then on amount and date, and flag every entry that does not match instead of forcing a match.
