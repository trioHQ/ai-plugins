# Trio plugin for Claude Code

Official plugin published by [Trio](https://www.trio.com.br) — Trio's own GitHub organization is [`triohq`](https://github.com/triohq), which owns this repository. Publisher contact: developers@trio.com.br.

The plugin installs the read-only [Trio MCP server](https://docs.trio.com.br/v2/mcp/what-is-trio-mcp) (`https://mcp.trio.com.br/mcp`), six skills and three slash commands to read balances, statements, Pix payments, receivables and corporate cards from your Trio corporate account. Agents read, analyze and explain. People approve in the [Trio App](https://app.trio.com.br).

## Installation

```bash
claude plugin marketplace add triohq/ai-plugins
claude plugin install trio@trio
```

Then run `/mcp` inside Claude Code, select `plugin:trio:trio`, and sign in to the Trio App in your browser.

## Skills

| Skill | What it does |
| - | - |
| `checking-balances` | Consolidated balance across entities and accounts |
| `analyzing-cash-flow` | Cash flow, daily position and period reports from the statement |
| `tracing-payments` | Trace a payment by identifier or payee, and compare a batch with payee history |
| `verifying-receivables` | Confirm whether a Pix or boleto arrived, and total what a payer sent |
| `reviewing-card-spend` | Card purchases, the open invoice, and CSV export |
| `validating-pix-keys` | Confirm a Pix key holder before the payment is created in the Trio App |

## Slash commands

- `/trio-balance [entity]` - Consolidated balances
- `/trio-cash-flow [period]` - Cash-flow summary for a period
- `/trio-trace-payment <id>` - Trace one outgoing payment

## Security

- Connect only to `https://mcp.trio.com.br/mcp`, and sign in only on `https://app.trio.com.br`.
- Sign in with OAuth, never with your password or an API key. The token carries the read-only `mcp:foundation` scope, is bound to one organization, and can be revoked.
- Card numbers and CPFs arrive masked. CNPJs and amounts do not.

## Privacy

Trio's [Privacy Policy](https://www.trio.com.br/legal/politica-de-privacidade) covers the Trio MCP server (`https://mcp.trio.com.br/mcp`). The plugin itself collects nothing: it only declares the remote server, skills and commands. After OAuth sign-in, the server reads your organization's balances, statements, payments, receivables and card data under the read-only `mcp:foundation` scope and returns it to Claude. No tool moves money.

## License

MIT
