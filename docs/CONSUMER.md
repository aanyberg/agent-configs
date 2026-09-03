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

`aanyberg/agent-configs` is public, so no additional credentials are needed to reach it.

## `CLAUDE.md` header

Every consumer repo's `CLAUDE.md` should start with:

```markdown
Backlog lives in GitHub Issues. Read .planning/policy.yml before any action that creates items, branches, or PRs.
```

## `.planning/policy.yml` — you don't need to write this yourself

The header above tells the agent to read `.planning/policy.yml`, but a new consumer repo won't have one yet, and doesn't need to create it manually. The first time a policy-dependent skill (`backlog-management`, `task-workflow`, `git-conventions`) needs it and finds it missing, it generates `.planning/policy.yml` from [`plugins/conventions/policy.example.yml`](../plugins/conventions/policy.example.yml) — best-practice defaults, with `backlog.backend` auto-detected from your GitHub remote — and reports what it generated in that session's response. It never regenerates or overwrites the file again after that.

If you want to guarantee the GitHub Issues backend the header above promises (rather than relying on auto-detection), set `backlog.backend: github-issues` explicitly once the file exists. Every other value in it — commit types, branch format, versioning, autonomous limits — is a starting point, not a fixed rule; edit the file directly and it takes effect on the next run.

## Local setup (one-time, per machine)

```bash
claude plugin marketplace add aanyberg/agent-configs
claude plugin install conventions@lahnvik
```

If the consumer repo already commits the `.claude/settings.json` above, `claude plugin marketplace add` runs automatically when the repo is trusted, and `claude plugin install` is the only manual step.

## Fallback

If a session's environment can't reach `aanyberg/agent-configs` on GitHub (e.g. a cloud sandbox without private-repo proxy access), the marketplace won't load. There is currently no sync script in this repo for that case — see the note in the root [README.md](../README.md) before scripting a workaround.
