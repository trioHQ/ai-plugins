# Trio AI plugin

Official plugin published by [Trio](https://www.trio.com.br) — Trio's own GitHub organization is [`triohq`](https://github.com/triohq), which owns this repository. Publisher contact: developers@trio.com.br. Read balances, statements, Pix payments, receivables and corporate cards from your Trio corporate account, directly from your AI coding tool.

The plugin installs the [Trio MCP server](https://docs.trio.com.br/v2/mcp/what-is-trio-mcp) (`https://mcp.trio.com.br/mcp`) and six skills that teach your agent Trio's conventions: start from the entity, walk every page, amounts in cents, and never move money. Every tool is read-only. Agents read, analyze and explain. People approve in the [Trio App](https://app.trio.com.br).

## Installation

### Claude Code

```bash
claude plugin marketplace add triohq/ai-plugins
claude plugin install trio@trio
```

Then authenticate: run `/mcp` inside Claude Code, select `plugin:trio:trio`, and sign in to the Trio App in your browser.

Without the plugin, add the server directly:

```bash
claude mcp add --transport http -s user trio https://mcp.trio.com.br/mcp
claude mcp login trio
```

### Muse

```bash
muse plugins install <path-to-this-repo>
```

### Cursor

Install from the [Cursor Marketplace](https://cursor.com/marketplace), or add this repo manually in Cursor Settings > Plugins. The plugin installs the Trio skills and the MCP server. Open Settings > MCP and select **Sign in** next to `trio`.

Without the plugin, add `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "trio": {
      "url": "https://mcp.trio.com.br/mcp"
    }
  }
}
```

### Codex

```bash
codex plugin marketplace add triohq/ai-plugins
```

Then run `codex`, open `/plugins`, select **Trio**, and install. Or without the plugin:

```bash
codex mcp add trio --url https://mcp.trio.com.br/mcp
codex mcp login trio
```

### Gemini CLI

Install this repository as an extension from the [Gemini CLI extensions gallery](https://github.com/google-gemini/gemini-cli/blob/main/docs/extensions/index.md) listing for Trio, using the gallery's install flow in your terminal.

### Antigravity

Install the Trio plugin from the Antigravity plugin browser, or add this repository manually in Antigravity's plugin settings.

Then run `/mcp`, select `trio`, and choose **Authenticate**.

### Claude, ChatGPT, Gemini, Perplexity and other MCP clients

Add a custom connector with the server URL `https://mcp.trio.com.br/mcp` and let the client run the OAuth sign-in. Choose OAuth where the client asks for an authentication method. Do not paste a Trio API key. See [Connecting Trio MCP](https://docs.trio.com.br/v2/mcp/connecting) and [PUBLISHING.md](PUBLISHING.md) for the directory listings.

## How to develop

Clone this repository with your usual Git tooling, then point Claude Code at your local checkout:

```bash
claude --plugin-dir /path/to/ai-plugins
```

Then run `/mcp` and authenticate. Run the manifest tests with `python3 -m unittest discover -s tests`.

## Features

Trio MCP provides 17 read-only tools across these categories:

- **Entities and accounts** - Entities (CNPJs) and bank accounts with real-time balances
- **Statements** - Consolidated statement of one account over a period, with running balance
- **Payments (cash-out)** - Outgoing Pix, boleto, utility and tax payments, by period, identifier or payee
- **Receivables (cash-in)** - Incoming Pix, boletos paid and deposits, by period, identifier or payer
- **Pix keys** - Validate a Pix key in the Central Bank's directory before paying in the Trio App
- **Corporate cards** - Cards, purchases, open and past invoices, and CSV invoice export
- **Transfers** - Transfers between your own accounts

See [Supported tools](https://docs.trio.com.br/v2/mcp/tools) for every tool, its parameters and a sample prompt.

### Bundled skills

The plugin ships six task-specific skills your AI client loads on demand:

| Skill | What it does |
| - | - |
| `checking-balances` | Consolidated balance across entities and accounts |
| `analyzing-cash-flow` | Cash flow, daily position and period reports from the statement |
| `tracing-payments` | Trace a payment by identifier or payee, and compare a batch with payee history |
| `verifying-receivables` | Confirm whether a Pix or boleto arrived, and total what a payer sent |
| `reviewing-card-spend` | Card purchases, the open invoice, and CSV export |
| `validating-pix-keys` | Confirm a Pix key holder before the payment is created in the Trio App |

Skills activate automatically when their description matches your request, so you generally don't need to invoke them by name.

### Slash commands

- `/trio-balance [entity]` - Consolidated balances
- `/trio-cash-flow [period]` - Cash-flow summary for a period
- `/trio-trace-payment <id>` - Trace one outgoing payment

## Example usage

```
> What's the consolidated balance across our entities?
> Which payments over R$ 50 thousand went out this week?
> Did the Pix with end-to-end ID E1234… arrive?
> How much did we pay Vértice Engenharia in October?
> What came in and went out of the main account in October?
> Where was the marketing card used in the last 7 days?
> Export the current invoice of the marketing card.
> Who owns the Pix key finance@acme.com.br?
```

## Security

- Connect only to `https://mcp.trio.com.br/mcp`, and sign in only on `https://app.trio.com.br`.
- Sign in with OAuth, never with your password or an API key. The token carries the read-only `mcp:foundation` scope, is bound to one organization, and can be revoked.
- Read access still exposes balances, statements, counterparties and card data. Use clients you trust, avoid shared or public sessions, and disconnect clients you no longer use.
- Card numbers and CPFs arrive masked. CNPJs and amounts do not.

Full guidance: [Connecting Trio MCP - Security best practices](https://docs.trio.com.br/v2/mcp/connecting).

## Privacy

Trio's [Privacy Policy](https://www.trio.com.br/legal/politica-de-privacidade) covers the Trio MCP server (`https://mcp.trio.com.br/mcp`). The plugin itself collects nothing: it only declares the remote server and skills. After OAuth sign-in, the server reads your organization's balances, statements, payments, receivables and card data under the read-only `mcp:foundation` scope and returns it to the AI client you connected. No tool moves money.

## Publishing

This repo is structured so one source tree feeds every marketplace: Claude Code and Codex plugin marketplaces, the Cursor Marketplace, the Gemini extensions gallery, Antigravity and Grok, the official MCP Registry, and the MCP directories (Smithery, Glama, mcp.so, PulseMCP). See [PUBLISHING.md](PUBLISHING.md) for the per-marketplace checklist.

## Documentation

- [What is Trio MCP?](https://docs.trio.com.br/v2/mcp/what-is-trio-mcp)
- [Connecting Trio MCP](https://docs.trio.com.br/v2/mcp/connecting)
- [Supported tools](https://docs.trio.com.br/v2/mcp/tools)
- [Trio API documentation](https://docs.trio.com.br)

## License

MIT
