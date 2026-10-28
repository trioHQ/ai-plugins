---
name: reviewing-card-spend
description: Review Trio corporate card purchases, current invoice totals and invoice exports for an entity.
---

# Reviewing card spend in Trio

Use the Trio MCP tools. Every tool is read-only.

## Workflow

1. Call `list_entities` to get the `entity_id`. The card tools need it.
2. Find the cards with `list_cards`. Filter by `display_name`, `holder_name`, `holder_tax_number` or `card_last_digits` when the question names a card or a person.
3. For spend in a period, call `list_card_purchases` with `entity_id`, `from_datetime` and `to_datetime`. Filter by `card_id`, `status` or category when asked. Walk every page (`metadata.before` / `metadata.after`) before you total.
4. For the open invoice, call `get_current_card_invoice`. It returns the purchase total, the amount pending confirmation, the period and the status. Use `list_card_invoices` for invoice history.
5. For one purchase by its end-to-end ID, call `get_card_purchase_by_e2e` with the `id` and the purchase `timestamp`.
6. To export, call `export_card_invoice` with `entity_id` and the invoice `id` (optionally one `card_id`) and give the user the temporary link. Mention that the link expires.

## Rules

- Amounts come in cents. Divide by 100 and format as Brazilian reais, for example `R$ 50.000,00`.
- Purchase statuses: `authorized`, `approved`, `denied`, `confirmed`, `canceled`, `reversed`, `voided`. Separate denied and reversed purchases from confirmed spend when you total.
- Invoice statuses: `open`, `closed`, `paid`. The current invoice is the `open` one.
- Card numbers arrive masked, for example `5555 •••• •••• 4021`. Never try to reconstruct the missing digits.
- Issuing, blocking or topping up a card happens in the Trio App. If the user asks for it, give them the relevant card and holder details and direct them there.
