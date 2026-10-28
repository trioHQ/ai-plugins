---
description: Show Trio balances, consolidated across entities and accounts
argument-hint: "[entity name or CNPJ]"
---

Use the Trio MCP tools to answer: what are the Trio balances? $ARGUMENTS

Follow the checking-balances skill: call `list_entities`, then `list_bank_accounts`, sum the available balances, and show the per-account breakdown grouped by entity. Format amounts as Brazilian reais.
