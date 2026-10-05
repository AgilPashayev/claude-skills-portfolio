---
name: skill-audit
description: Review a playbook folder for description quality, length, and clarity. Use when asked to review, lint, or improve a SKILL.md file or playbooks directory.
---

# Playbook audit

Use on any folder that contains `SKILL.md`.

## Steps

1. Read the frontmatter and body. Do not open extra files until `SKILL.md` points at them.
2. Score each item in the rubric as pass, warn, or fail.
3. If scripts exist, check they are meant to be **run**, not copied into a prompt.
4. Suggest a clearer `description` if triggers are missing.

## Rubric

| Check | Pass looks like |
| --- | --- |
| Name | lowercase, hyphens, matches folder, under 64 chars |
| Description | what **and** when, concrete trigger words |
| Length | main file under 500 lines; detail in linked files |
| Links | extra files linked from `SKILL.md`, not nested deeply |
| Paths | POSIX paths (`scripts/validate.py`) |
| Secrets | no tokens, keys, or private URLs |
| Review gate | analysis playbooks require human review before action |

## Output

```
Playbook: <name>
Verdict: ready | revise
Findings:
- [fail] ...
- [warn] ...
Rewrite (description):
  ...
```
