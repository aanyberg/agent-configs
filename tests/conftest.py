"""Shared loaders for the repository's structural validation suite.

Nothing here executes plugin logic; it only parses the files Claude Code
itself parses, so a failure means the plugin would load wrong.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Doc:
    """A markdown file with YAML frontmatter."""

    path: Path
    frontmatter: dict
    body: str

    @property
    def rel(self) -> str:
        return str(self.path.relative_to(REPO_ROOT))

    def __str__(self) -> str:  # keeps pytest ids readable
        return self.rel


def parse_frontmatter(path: Path) -> Doc:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} does not start with a YAML frontmatter block")
    _, raw, body = text.split("---\n", 2)
    data = yaml.safe_load(raw)
    if not isinstance(data, dict):
        raise ValueError(f"{path} frontmatter is not a mapping")
    return Doc(path=path, frontmatter=data, body=body)


def repo_root() -> Path:
    return REPO_ROOT


def marketplace_path() -> Path:
    return REPO_ROOT / ".claude-plugin" / "marketplace.json"


def load_marketplace() -> dict:
    return json.loads(marketplace_path().read_text(encoding="utf-8"))


def plugin_dirs() -> list[Path]:
    return sorted(p.parents[1] for p in REPO_ROOT.glob("plugins/*/.claude-plugin/plugin.json"))


def skill_files() -> list[Path]:
    return sorted(REPO_ROOT.glob("plugins/*/skills/*/SKILL.md"))


def agent_files() -> list[Path]:
    return sorted(REPO_ROOT.glob("plugins/*/agents/*.md"))


def markdown_files() -> list[Path]:
    return sorted(
        p
        for p in REPO_ROOT.rglob("*.md")
        if ".git" not in p.parts and "node_modules" not in p.parts
    )


def _ids(paths: list[Path]) -> list[str]:
    return [str(p.relative_to(REPO_ROOT)) for p in paths]


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    """Parametrise per-file tests so each file fails independently."""
    if "skill" in metafunc.fixturenames:
        paths = skill_files()
        metafunc.parametrize("skill", [parse_frontmatter(p) for p in paths], ids=_ids(paths))
    if "agent" in metafunc.fixturenames:
        paths = agent_files()
        metafunc.parametrize("agent", [parse_frontmatter(p) for p in paths], ids=_ids(paths))
    if "plugin_dir" in metafunc.fixturenames:
        paths = plugin_dirs()
        metafunc.parametrize("plugin_dir", paths, ids=_ids(paths))
    if "md_file" in metafunc.fixturenames:
        paths = markdown_files()
        metafunc.parametrize("md_file", paths, ids=_ids(paths))
