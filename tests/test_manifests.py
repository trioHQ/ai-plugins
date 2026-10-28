"""Every manifest must parse, and every path a manifest names must exist.

Manifests hand paths to clients that only check schema at install time.
Moving a file without updating a manifest is silent until a session starts.
"""

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MCP_URL = "https://mcp.trio.com.br/mcp"

JSON_FILES = [
    ".muse-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".cursor-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".antigravity-plugin/plugin.json",
    ".agents/plugins/marketplace.json",
    "gemini-extension.json",
    "server.json",
    "mcp.json",
    ".mcp.json",
    "mcp_config.json",
]


def load(relative):
    return json.loads((REPO_ROOT / relative).read_text(encoding="utf-8"))


class TestManifests(unittest.TestCase):
    def test_json_files_parse(self):
        for relative in JSON_FILES:
            with self.subTest(file=relative):
                self.assertIsInstance(load(relative), dict)

    def test_mcp_url_is_consistent(self):
        for relative in JSON_FILES:
            with self.subTest(file=relative):
                text = (REPO_ROOT / relative).read_text(encoding="utf-8")
                if "mcp.trio.com.br" in text:
                    self.assertIn(MCP_URL, text)

    def test_versions_are_in_sync(self):
        versions = {
            load(".claude-plugin/plugin.json")["version"],
            load(".claude-plugin/marketplace.json")["plugins"][0]["version"],
            load(".muse-plugin/plugin.json")["version"],
            load(".cursor-plugin/plugin.json")["version"],
            load(".codex-plugin/plugin.json")["version"],
            load("gemini-extension.json")["version"],
            load("server.json")["version"],
        }
        self.assertEqual(len(versions), 1, f"versions drifted: {versions}")

    def test_muse_capability_paths_exist(self):
        manifest = load(".muse-plugin/plugin.json")
        capabilities = manifest["capabilities"]
        for skill in capabilities["skills"]:
            path = REPO_ROOT / skill["path"]
            self.assertTrue(path.is_file(), f"missing skill file: {skill['path']}")
        for command in capabilities["commands"]:
            path = REPO_ROOT / command["path"]
            self.assertTrue(path.is_file(), f"missing command file: {command['path']}")
        server_ids = [server["id"] for server in capabilities["mcpServers"]]
        self.assertEqual(server_ids, ["trio"])

    def test_skill_frontmatter_matches_directory(self):
        for skill_dir in sorted((REPO_ROOT / "skills").iterdir()):
            skill_file = skill_dir / "SKILL.md"
            with self.subTest(skill=skill_dir.name):
                self.assertTrue(skill_file.is_file())
                text = skill_file.read_text(encoding="utf-8")
                self.assertTrue(text.startswith("---\n"))
                self.assertIn(f"name: {skill_dir.name}", text)
                self.assertIn("description:", text)

    def test_referenced_assets_exist(self):
        for manifest in (".cursor-plugin/plugin.json", ".codex-plugin/plugin.json"):
            data = load(manifest)
            logo = data.get("logo") or data.get("interface", {}).get("logo")
            with self.subTest(file=manifest):
                self.assertTrue((REPO_ROOT / logo).is_file(), f"missing logo: {logo}")
                self.assertTrue((REPO_ROOT / data["skills"].rstrip("/")).is_dir())
                mcp_file = data["mcpServers"].lstrip("./")
                self.assertTrue((REPO_ROOT / mcp_file).is_file())

    def test_codex_meets_openai_submission_minimum(self):
        # Limits from developers.openai.com/plugins/deploy/submission (Codex format).
        data = load(".codex-plugin/plugin.json")
        interface = data["interface"]
        self.assertLessEqual(len(data["name"]), 64)
        self.assertLessEqual(len(interface["displayName"]), 30)
        self.assertLessEqual(len(interface["shortDescription"]), 30)
        self.assertLessEqual(len(interface["longDescription"]), 4000)
        self.assertLessEqual(len(interface["developerName"]), 80)
        self.assertTrue(interface["capabilities"])
        for url_field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
            self.assertTrue(interface[url_field].startswith("https://"), url_field)
        self.assertLessEqual(len(interface["defaultPrompt"]), 3)
        for prompt in interface["defaultPrompt"]:
            self.assertLessEqual(len(prompt), 128)
        self.assertEqual(data["mcpServers"], "./.mcp.json")
        for icon_field in ("logo", "composerIcon"):
            self.assertTrue((REPO_ROOT / interface[icon_field]).is_file(), icon_field)
        mcp = load(".mcp.json")["mcpServers"]["trio"]
        self.assertEqual(mcp["extensions"]["com.openai"]["auth"]["type"], "oauth")
        review = data["extensions"]["com.openai"]["review"]["test_cases"]
        self.assertEqual(len(review["positive"]), 5)
        self.assertEqual(len(review["negative"]), 3)

    def test_gemini_commands_exist_for_claude_commands(self):
        for md_file in sorted((REPO_ROOT / "commands").glob("*.md")):
            with self.subTest(command=md_file.stem):
                self.assertTrue((REPO_ROOT / "commands" / f"{md_file.stem}.toml").is_file())


if __name__ == "__main__":
    unittest.main()
