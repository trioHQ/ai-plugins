# Publishing Trio MCP

One repo, every marketplace. This file is the checklist for publishing the official Trio MCP server and this plugin. The MCP endpoint is `https://mcp.trio.com.br/mcp` (streamable HTTP, OAuth 2.0 with dynamic client registration, PKCE S256, scope `mcp:foundation`, authorization server `https://app.trio.com.br`). It is read-only.

## Source of truth in this repo

| Marketplace | File(s) | How it is consumed |
| - | - | - |
| Claude Code plugins | `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` | `claude plugin marketplace add triohq/ai-plugins` |
| Muse plugins | `.muse-plugin/plugin.json` | `muse plugins install <repo>` |
| Cursor Marketplace | `.cursor-plugin/plugin.json`, `mcp.json`, `skills/` | Cursor Settings > Plugins, or the Cursor Marketplace listing |
| Codex plugins | `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `.mcp.json` | `codex plugin marketplace add triohq/ai-plugins` |
| Gemini CLI extensions | `gemini-extension.json`, `GEMINI.md`, `commands/*.toml` | `gemini extensions install https://github.com/triohq/ai-plugins` |
| Antigravity | `.antigravity-plugin/plugin.json`, `mcp_config.json` | `agy plugin install https://github.com/triohq/ai-plugins` |
| Official MCP Registry | `server.json` | `mcp-publisher publish` (see below) |
| Any other MCP client | `.mcp.json`, `mcp.json` | Copy the `trio` server entry into the client's MCP config |

Keep the version in every manifest in sync. Bump them together in one commit.

## 1. Official MCP Registry (modelcontextprotocol.io)

The registry is the upstream source most directories sync from. Publish it first.

```bash
# Install the publisher: https://github.com/modelcontextprotocol/registry
mcp-publisher login github   # proves control of the triohq GitHub org (io.github.triohq/*)
mcp-publisher publish        # reads ./server.json
mcp-publisher validate       # optional pre-check
```

`server.json` declares the remote `https://mcp.trio.com.br/mcp` as `streamable-http`. The name `io.github.triohq/trio` requires publishing from the `triohq` GitHub organization. To use `io.trio.com.br/trio` instead, verify the `trio.com.br` domain by DNS or HTTP as the registry documents, then change `name` in `server.json`.

## 2. Claude

- **Claude Code marketplace**: this repo is the marketplace. Users run `claude plugin marketplace add triohq/ai-plugins` and `claude plugin install trio@trio`. No separate submission.
- **Claude Connectors Directory** (claude.ai Settings > Connectors): submit the remote server at https://claude.ai/directory or through the Anthropic partner submission form. Provide the server URL, the OAuth authorization server `https://app.trio.com.br`, the `mcp:foundation` scope, the privacy policy and support links, and demo credentials for review. This listing is what makes Trio appear as a one-click connector in Claude.
- **Name/publisher similarity flags (expected)**: the scanner flags `trio` / `triohq` as resembling an existing brand because Trio is the brand. This is Trio's official plugin, not an impersonation — paste into the submission's reviewer notes: "Publisher `triohq` is the official GitHub organization of Trio (https://www.trio.com.br). This repo, the MCP endpoint `mcp.trio.com.br`, the OAuth server `app.trio.com.br` and author contact `developers@trio.com.br` are all under Trio's control. Plugin name `trio` names our own product." If the reviewer still requires separation, prove control from a `trio.com.br` page linking to `github.com/triohq/ai-plugins` rather than renaming the plugin.
- **Privacy**: `.claude-plugin/plugin.json` declares `privacyPolicyUrl` and the README has a Privacy section linking the same URL. Keep both in sync.
- **README install commands**: do not add shell commands that fetch and run remote code (for example an extensions/plugin install pointed straight at a GitHub URL) to the README; the directory scanner flags them as install-time risk. Use marketplace/gallery/UI install flows there and keep CLI-from-URL commands in this file only.

## 3. ChatGPT

Submit the MCP server as a ChatGPT app/connector through the OpenAI Apps SDK submission flow. The server is read-only, so declare read-only tool annotations and no write actions. Provide the same OAuth metadata: clients register dynamically at `https://app.trio.com.br/oauth/register`.

## 4. Cursor Marketplace

Submit at https://cursor.com/marketplace (publish flow). The `.cursor-plugin/plugin.json` manifest, `mcp.json` and `skills/` in this repo are the listing payload. Cursor also surfaces the plugin to Grok (desktop and mobile) from the same marketplace.

## 5. Codex

This repo is a Codex marketplace: `codex plugin marketplace add triohq/ai-plugins`. No separate submission. Keep `.agents/plugins/marketplace.json` pointing at the canonical repo URL.

## 6. Gemini CLI and Antigravity

Gemini CLI installs extensions straight from GitHub: `gemini extensions install https://github.com/triohq/ai-plugins`. For the Gemini extensions gallery, open a listing PR or issue in the `google-gemini/gemini-cli` extensions gallery with this repo URL. Antigravity installs from the same repo with `agy plugin install`.

## 7. MCP directories

Most directories ingest the official registry, so step 1 covers them over time. To appear sooner, submit the server URL and this repo directly:

- **Smithery** (smithery.ai): add a remote server by URL `https://mcp.trio.com.br/mcp`.
- **Glama** (glama.ai/mcp): submit the repo; Glama reads `server.json` and the README.
- **mcp.so**: submit the repo at mcp.so.
- **PulseMCP** (pulsemcp.com): submit the server; it also syncs the official registry.
- **Awesome MCP Servers** (github.com/punkpeye/awesome-mcp-servers): open a PR adding Trio under Finance.

## 8. VS Code and other clients

No listing needed. Users add the `.mcp.json` entry to their workspace or user MCP config and sign in with OAuth. Document the snippet from the README wherever Trio API docs mention MCP clients.

## Before each release

- [ ] `python3 -m unittest discover -s tests` passes (manifests parse, referenced paths exist, MCP URL is consistent everywhere).
- [ ] `muse skills validate` passes for every directory in `skills/`.
- [ ] `muse plugins validate .` passes.
- [ ] Version bumped in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.muse-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.codex-plugin/plugin.json`, `gemini-extension.json` and `server.json`.
- [ ] CHANGELOG.md entry added.
- [ ] After merging, re-publish `server.json` to the MCP Registry if the version or URL changed.
