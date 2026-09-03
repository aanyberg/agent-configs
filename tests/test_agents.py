"""Agent frontmatter controls model, cost, and tool access — it must be explicit."""

from __future__ import annotations

import re
from collections import Counter

from conftest import agent_files, parse_frontmatter

NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

ALLOWED_KEYS = {
    "name", "description", "tools", "model", "effort",
    "maxTurns", "permissionMode", "color", "argument-hint",
}
REQUIRED_KEYS = {"name", "description", "tools", "model", "permissionMode"}

VALID_MODELS = {"opus", "sonnet", "haiku", "fable", "inherit"}
VALID_EFFORT = {"low", "medium", "high"}
VALID_PERMISSION_MODES = {"default", "plan", "acceptEdits", "bypassPermissions"}
VALID_TOOLS = {
    "AskUserQuestion", "Bash", "Edit", "Glob", "Grep", "NotebookEdit", "Read",
    "Skill", "SlashCommand", "Task", "TodoWrite", "WebFetch", "WebSearch", "Write",
}


def _tool_list(agent) -> list[str]:
    tools = agent.frontmatter.get("tools", [])
    if isinstance(tools, str):
        return [t.strip() for t in tools.split(",") if t.strip()]
    return [str(t) for t in tools]


def test_agent_has_required_frontmatter(agent):
    missing = REQUIRED_KEYS - set(agent.frontmatter)
    assert not missing, (
        f"{agent.rel}: frontmatter is missing {sorted(missing)}; without these the agent "
        f"inherits the caller's model and full tool access"
    )


def test_agent_has_no_unknown_frontmatter_keys(agent):
    unknown = set(agent.frontmatter) - ALLOWED_KEYS
    assert not unknown, f"{agent.rel}: unrecognised frontmatter key(s) {sorted(unknown)}"


def test_agent_name_matches_filename(agent):
    expected = agent.path.stem
    assert agent.frontmatter.get("name") == expected, (
        f"{agent.rel}: name {agent.frontmatter.get('name')!r} must match filename {expected!r}"
    )


def test_agent_name_is_kebab_case(agent):
    name = str(agent.frontmatter.get("name", ""))
    assert NAME.match(name), (
        f"{agent.rel}: name {name!r} must be lowercase kebab-case — it is the address "
        f"callers type, so spaces and capitals make it awkward to invoke"
    )


def test_agent_description_is_non_empty(agent):
    assert str(agent.frontmatter.get("description", "")).strip(), f"{agent.rel}: empty description"


def test_agent_model_is_valid(agent):
    model = agent.frontmatter.get("model")
    assert model in VALID_MODELS, f"{agent.rel}: model {model!r} not in {sorted(VALID_MODELS)}"


def test_agent_effort_is_valid(agent):
    effort = agent.frontmatter.get("effort")
    if effort is not None:
        assert effort in VALID_EFFORT, f"{agent.rel}: effort {effort!r} not in {sorted(VALID_EFFORT)}"


def test_agent_permission_mode_is_valid(agent):
    mode = agent.frontmatter.get("permissionMode")
    assert mode in VALID_PERMISSION_MODES, (
        f"{agent.rel}: permissionMode {mode!r} not in {sorted(VALID_PERMISSION_MODES)}"
    )


def test_agent_tools_are_real_tools(agent):
    unknown = [t for t in _tool_list(agent) if t not in VALID_TOOLS and not t.startswith("mcp__")]
    assert not unknown, f"{agent.rel}: unknown tool name(s) {unknown}"


def test_agent_max_turns_is_a_positive_int(agent):
    turns = agent.frontmatter.get("maxTurns")
    if turns is not None:
        assert isinstance(turns, int) and 0 < turns <= 100, (
            f"{agent.rel}: maxTurns {turns!r} must be an int in 1..100"
        )


def test_read_only_agents_cannot_write(agent):
    """An agent in plan mode must not be handed edit tools."""
    if agent.frontmatter.get("permissionMode") != "plan":
        return
    writers = {"Edit", "Write", "NotebookEdit"} & set(_tool_list(agent))
    assert not writers, f"{agent.rel}: permissionMode 'plan' but declares {sorted(writers)}"


def test_agent_names_are_unique():
    names = [parse_frontmatter(p).frontmatter.get("name") for p in agent_files()]
    duplicates = [n for n, count in Counter(names).items() if count > 1]
    assert not duplicates, f"duplicate agent names: {duplicates}"
