---
name: skill-audit
description: Audit an Agent Skill folder for description quality, progressive disclosure, and token cost. Use when the user asks to review, lint, or improve a SKILL.md file or skills directory.
---

# Skill audit

Use this on any folder that contains `SKILL.md`.

## Steps

1. Read the skill's frontmatter and body. Do not load extra files until `SKILL.md` points at them.
2. Score each item in the rubric below as pass, warn, or fail.
3. If the skill includes scripts, open them and check they are meant to be **run**, not pasted into context.
4. Suggest a rewritten `description` if the current one is missing triggers.

## Rubric

| Check | Pass looks like |
| --- | --- |
| Name | lowercase, hyphens, matches folder, under 64 chars |
| Description | third person, what **and** when, concrete trigger words |
| Length | `SKILL.md` under 500 lines; details live in linked files |
| Disclosure | extra files linked from `SKILL.md`, not nested three levels deep |
| Freedom | fragile steps use scripts or exact commands; judgment stays in prose |
| Paths | POSIX paths (`scripts/validate.py`), not Windows backslashes |
| Secrets | no tokens, keys, or private URLs |

## Output

Return a short report:

```
Skill: <name>
Verdict: ship | revise
Findings:
- [fail] ...
- [warn] ...
Rewrite (description):
  ...
```
