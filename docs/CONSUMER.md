# Consuming this repo as a plugin

This repo publishes a Claude Code plugin marketplace (`lahnvik`) with one plugin, `conventions`, containing all skills and agents from [`plugins/conventions`](../plugins/conventions). Consumer repos load it directly — no copying or symlinking into `~/.claude`.

## `.claude/settings.json`

Add the marketplace and enable the plugin in the consumer repo's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "lahnvik": {
      "source": {
        "source": "github",
        "repo": "aanyberg/agent-configs"
      }
    }
  },
  "enabledPlugins": {
    "conventions@lahnvik": true
  }
}
```

`aanyberg/agent-configs` is private, so the consumer's Claude Code session (local or cloud) needs read access to it under the account/org the session runs as.

## `CLAUDE.md` header

Every consumer repo's `CLAUDE.md` should start with:

```markdown
Backlog lives in GitHub Issues. Read .planning/policy.yml before any action that creates items, branches, or PRs.
```

## Local setup (one-time, per machine)

```bash
claude plugin marketplace add aanyberg/agent-configs
claude plugin install conventions@lahnvik
```

If the consumer repo already commits the `.claude/settings.json` above, `claude plugin marketplace add` runs automatically when the repo is trusted, and `claude plugin install` is the only manual step.

## Fallback

If a session's environment can't reach `aanyberg/agent-configs` on GitHub (e.g. a cloud sandbox without private-repo proxy access), the marketplace won't load. There is currently no sync script in this repo for that case — see the note in the root [README.md](../README.md) before scripting a workaround.
