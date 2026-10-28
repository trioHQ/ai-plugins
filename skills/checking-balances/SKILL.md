---
name: checking-balances
description: Answer questions about Trio account balances, consolidated across entities and bank accounts.
---

# Checking balances in Trio

Use the Trio MCP tools. Every tool is read-only.

## Workflow

1. Call `list_entities` first. It returns the organization's entities (CNPJs) and the `entity_id` most other tools need. With one entity, use it automatically. With several, and a question that spans the organization, cover all of them; ask which one only when the question names one entity ambiguously.
2. Call `list_bank_accounts`. Filter by `entity_id` when the question is about one entity. It returns each account's real-time available balance, currency and status.
3. Sum the available balances yourself for a consolidated total. Show the per-account breakdown next to the total, grouped by entity, so the reader can check the sum.

## Rules

- Amounts come in cents. Divide by 100 and format as Brazilian reais, for example `R$ 50.000,00`.
- Say the balance is the available balance at the time of the call. Balances are real-time; do not present them as end-of-day or historical.
- Flag accounts whose status is not `approved` instead of silently including or dropping them.
- For movements behind a balance, switch to the cash-flow skill (`get_account_statement`). Do not reconstruct a balance from document listings.
