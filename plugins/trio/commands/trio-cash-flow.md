---
description: Summarize Trio cash flow for a period from the account statement
argument-hint: "[period, e.g. October 2026]"
---

Use the Trio MCP tools to summarize cash flow for: $ARGUMENTS

Follow the analyzing-cash-flow skill: find the account with `list_entities` and `list_bank_accounts`, read the whole period with `get_account_statement` page by page, then total inflows and outflows separately and give the net. Format amounts as Brazilian reais and state the exact period used.
