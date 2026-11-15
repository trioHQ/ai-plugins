# Changelog

## 0.1.1 - 2026-11-15

- Move the Claude Code plugin to `plugins/trio` so the Claude Directory submission holds only Markdown, JSON and PNG files. The root marketplace now points at that folder.
- Claude's `.mcp.json` declares only `type` and `url`. Codex keeps its OpenAI auth extension in the root `.mcp.json`.
- Add a 512 px plugin icon for the Claude Directory listing.

## 0.1.0 - 2026-10-28

- Initial release of the official Trio plugin.
- Trio MCP server (`https://mcp.trio.com.br/mcp`, read-only, OAuth `mcp:foundation`) wired for Claude Code, Muse, Cursor, Codex, Gemini CLI and Antigravity.
- `server.json` for the official MCP Registry.
- Six skills: `checking-balances`, `analyzing-cash-flow`, `tracing-payments`, `verifying-receivables`, `reviewing-card-spend`, `validating-pix-keys`.
- Three slash commands: `/trio-balance`, `/trio-cash-flow`, `/trio-trace-payment`.
