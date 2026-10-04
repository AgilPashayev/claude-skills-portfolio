# Agent Skills interview playbook

Use this before a screening or onsite. Speak in your own words. Do not memorize paragraphs.

## 30-second pitch

Agent Skills are folders of instructions, optional reference files, and scripts. The model keeps only each skill's name and description in context, then reads `SKILL.md` when the task matches. That gives repeatable workflows without stuffing the system prompt.

## What I built in this repo

| Skill | Pattern it demonstrates | Line to say |
| --- | --- | --- |
| `git-commit` | Tight template, no extra files | "Cheap skill. Description has trigger words: commit, message, staged." |
| `pr-review` | Progressive disclosure | "`STANDARDS.md` stays on disk until the review starts." |
| `skill-audit` | Meta workflow / quality bar | "I treat skills as product surface: lint the description, length, and paths." |
| `release-notes` | Executable helper | "The script returns commit lines. The model never needs the Python in context." |

## Expected questions

**What is a skill vs a prompt?**
A prompt is for this conversation. A skill is a reusable playbook that loads on demand across chats.

**Skill vs rule vs MCP vs subagent?**
- Rule: always-on preference, short.
- Skill: procedure, maybe scripts, loaded when relevant.
- MCP: tools and data connections.
- Subagent: a separate agent you delegate a job to.

**How does progressive disclosure work?**
1. Metadata (~name + description) is always visible.
2. Matching task → read `SKILL.md`.
3. Linked files and script *output* load only if needed.

**What makes a good description?**
Third person. What it does and when to use it. Concrete verbs the user might say.

Weak: "Helps with git."
Strong: "Draft a conventional commit message from the current git diff. Use when the user asks to commit or write a commit message."

**How would you ship skills on a team?**
Keep them in the repo under `.cursor/skills/` or `.claude/skills/`. Review `SKILL.md` like code. Version them with the project. Do not put secrets in skills.

**Failure modes you watch for?**
Vague descriptions that never trigger. Huge `SKILL.md` files that waste context. Windows paths. Nested references the model never opens. Skills that duplicate a one-line rule.

## Live demo (5 minutes)

1. Open this README and the `skills/` tree.
2. Show `pr-review/SKILL.md` linking to `STANDARDS.md`.
3. Show `release-notes/scripts/collect_commits.py` and explain "run, don't paste."
4. If Cursor is open: copy one skill into `.cursor/skills/` and invoke `/git-commit`.
5. Offer to rewrite a company's onboarding doc as a skill on the whiteboard.

## If they use a different stack

Same folder format works in Claude apps, Claude Code, the Claude API (with code execution), and Cursor. I can talk about the format, not one vendor.
