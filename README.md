# QA playbooks

Personal testing and engineering playbooks I keep next to the work. Each folder is a small, reusable procedure (`SKILL.md`) with optional notes and scripts.

Maintained by [Agil Pashayev](https://github.com/AgilPashayev).

**Site:** [agilpashayev.github.io/claude-skills-portfolio](https://agilpashayev.github.io/claude-skills-portfolio)

## Layout

```text
skills/
  qa/                 testing & CI triage
  engineering/        day-to-day engineering helpers
docs/
  notes.md            short talking points for walkthroughs
```

## QA

| Playbook | Purpose |
| --- | --- |
| [`fail-check-analyzer`](skills/qa/fail-check-analyzer/SKILL.md) | Root-cause a hard CI/test failure |
| [`flaky-test-analyzer`](skills/qa/flaky-test-analyzer/SKILL.md) | Diagnose intermittent tests |

Both stop after the report. **A person reviews before any fix, quarantine, or CI change.**

## Engineering

| Playbook | Purpose |
| --- | --- |
| [`git-commit`](skills/engineering/git-commit/SKILL.md) | Conventional commit message from the current diff |
| [`pr-review`](skills/engineering/pr-review/SKILL.md) | Structured review checklist + standards |
| [`release-notes`](skills/engineering/release-notes/SKILL.md) | User-facing notes from git history |
| [`skill-audit`](skills/engineering/skill-audit/SKILL.md) | Lint a playbook for clarity and size |

## How I use them

Copy a folder into the project (or your user skills directory), then run the matching workflow when the situation comes up:

```text
skills/qa/fail-check-analyzer  →  .cursor/skills/fail-check-analyzer
# or
skills/qa/fail-check-analyzer  →  .claude/skills/fail-check-analyzer
```

## Conventions

1. Every playbook starts with a clear `description` (what + when).
2. Keep the main file short; put detail in linked files.
3. Scripts are meant to be run; output matters, not pasting the source.
4. No secrets in these folders.
5. Analysis playbooks require human review before action.

## License

MIT.
