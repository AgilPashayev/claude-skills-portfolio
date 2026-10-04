# Agent Skills portfolio

Interview-ready examples of **Claude / Cursor Agent Skills**: reusable `SKILL.md` playbooks that load only when a task matches.

**Live site:** [agilpashayev.github.io/claude-skills-portfolio](https://agilpashayev.github.io/claude-skills-portfolio)

Built by [Agil Pashayev](https://github.com/AgilPashayev) to walk through in hiring conversations: what skills are, how progressive disclosure works, and how I would write them on a team.

## Why this exists

Hiring loops often ask how you would give an agent durable, cheap context. Skills are the answer I use:

- **Not a prompt** — they persist across chats.
- **Not MCP** — they are procedures, not tool connections.
- **Not a subagent** — they specialize the current agent instead of spawning another one.

Each example in `skills/` is small enough to read on a screen share.

## Skills in this repo

| Skill | What it shows |
| --- | --- |
| [`git-commit`](skills/git-commit/SKILL.md) | Short skill, strong description, conventional-commit template |
| [`pr-review`](skills/pr-review/SKILL.md) | Progressive disclosure (`STANDARDS.md`, `examples.md`) |
| [`skill-audit`](skills/skill-audit/SKILL.md) | Quality bar I would apply to other people's skills |
| [`release-notes`](skills/release-notes/SKILL.md) | Script the agent runs so source code stays out of context |

Interview talking points live in [`INTERVIEW.md`](INTERVIEW.md).

## Install (Cursor or Claude Code)

Copy a skill folder into one of these locations:

```text
.cursor/skills/<name>/SKILL.md     this project
.claude/skills/<name>/SKILL.md     this project (Claude Code + Cursor)
~/.cursor/skills/<name>/SKILL.md   all local projects
~/.claude/skills/<name>/SKILL.md   all local projects
```

Then either:

- Ask the agent to do the matching task, or
- Type `/git-commit`, `/pr-review`, `/skill-audit`, or `/release-notes` in Agent chat.

## Anatomy of a skill

```text
pr-review/
  SKILL.md        name + description + steps (always the entry)
  STANDARDS.md    loaded only when SKILL.md says to read it
  examples.md     loaded only if the review tone is unclear
```

Frontmatter that actually matters:

```yaml
---
name: git-commit
description: Draft a conventional commit message from the current git diff. Use when the user asks to commit, write a commit message, or summarize staged changes.
---
```

The description is the trigger. If it is vague, the skill never loads.

## Design rules I follow

1. Description includes **what** and **when**, in third person.
2. Keep `SKILL.md` under 500 lines; park detail in linked files.
3. Fragile, repetitive work goes in scripts. The agent runs them and reads stdout.
4. Use POSIX paths in instructions (`scripts/collect_commits.py`).
5. No secrets in skill files.

## Site

The GitHub Pages site is static HTML in this repository (`index.html`). Enable **Pages** on the `main` branch, folder `/ (root)`.

## License

MIT. Skills are examples, not production runbooks for a specific company.
