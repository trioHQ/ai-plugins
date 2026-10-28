---
name: validating-pix-keys
description: Validate a Pix key in the Central Bank directory and confirm the holder before a payment is created in the Trio App.
---

# Validating Pix keys with Trio

Use the Trio MCP tools. Every tool is read-only.

## Workflow

1. Call `list_entities` to get the `entity_id`. `check_pix_key` needs it.
2. Call `check_pix_key` with the `entity_id` and the `key`. A key can be a CPF, CNPJ, email, phone number or random key.
3. Report the holder's name, institution and account type exactly as returned, and compare them with who the user expects to pay. Flag any mismatch before the user proceeds.

## Rules

- `check_pix_key` validates only. It does not create a payment and does not reserve the key.
- The payment itself is created and approved in the Trio App, under the organization's approval rules. Never claim you made or scheduled a payment.
- If the key is not found, say so and repeat the key you checked so the user can spot a typo. Do not guess a corrected key.
- A matching key proves the account exists and names its holder. It does not prove the payment is legitimate. If the amount or the payee looks unusual for this payer, say so.
