"""The marketplace and plugin manifests must load, resolve, and agree."""

from __future__ import annotations

import json
import re

from conftest import load_marketplace, marketplace_path, plugin_dirs, repo_root

SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def test_marketplace_is_valid_json():
    json.loads(marketplace_path().read_text(encoding="utf-8"))


def test_marketplace_has_required_fields():
    data = load_marketplace()
    for field in ("name", "owner", "plugins"):
        assert field in data, f"marketplace.json is missing '{field}'"
    assert NAME.match(data["name"]), f"marketplace name {data['name']!r} must be kebab-case"
    assert isinstance(data["plugins"], list) and data["plugins"], "no plugins declared"


def test_marketplace_sources_resolve_to_a_plugin():
    for entry in load_marketplace()["plugins"]:
        source = repo_root() / entry["source"]
        assert source.is_dir(), f"{entry['name']}: source {entry['source']} is not a directory"
        manifest = source / ".claude-plugin" / "plugin.json"
        assert manifest.is_file(), f"{entry['name']}: no plugin.json at {entry['source']}"


def test_every_plugin_on_disk_is_listed_in_the_marketplace():
    listed = {e["name"] for e in load_marketplace()["plugins"]}
    on_disk = {d.name for d in plugin_dirs()}
    assert on_disk <= listed, f"plugins not listed in marketplace.json: {sorted(on_disk - listed)}"


def test_plugin_manifest_is_valid(plugin_dir):
    data = json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    for field in ("name", "description", "version"):
        assert field in data, f"{plugin_dir.name}: plugin.json is missing '{field}'"
    assert data["name"] == plugin_dir.name, (
        f"plugin.json name {data['name']!r} must match directory {plugin_dir.name!r}"
    )
    assert NAME.match(data["name"]), f"plugin name {data['name']!r} must be kebab-case"
    assert SEMVER.match(data["version"]), f"version {data['version']!r} is not semver"


def test_marketplace_and_plugin_descriptions_agree(plugin_dir):
    manifest = json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    entries = {e["name"]: e for e in load_marketplace()["plugins"]}
    entry = entries.get(plugin_dir.name)
    assert entry is not None, f"{plugin_dir.name} is not listed in marketplace.json"
    assert entry.get("description") == manifest["description"], (
        f"{plugin_dir.name}: marketplace.json and plugin.json descriptions have drifted"
    )
