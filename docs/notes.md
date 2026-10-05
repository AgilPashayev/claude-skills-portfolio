# Walkthrough notes

Short reminders for presenting this repo. Use your own words.

## Opening

These are the checklists I actually use for CI failures and flakes. The folders under `skills/qa/` are the core; `skills/engineering/` is supporting day-to-day work.

## Points to hit

1. **Hard fail vs flake** — always red → `fail-check-analyzer`; intermittent → `flaky-test-analyzer`.
2. **Human review** — analysis only. No merge, quarantine, or CI mute without a person signing off.
3. **First real error** — ignore cascade noise after the first failure.
4. **Flakes** — rank race / data / order; do not “fix” with a longer blind sleep.
5. **Structure** — short entry file, extra detail in linked docs, scripts only when useful.

## Demo path (5 minutes)

1. Open `skills/qa/fail-check-analyzer/SKILL.md` and `TAXONOMY.md`.
2. Open `skills/qa/flaky-test-analyzer/SKILL.md` and `FLAKE_PATTERNS.md`.
3. Show the human-review block at the end of each report template.
4. Optionally show `skills/engineering/pr-review/` as a non-QA example of the same folder pattern.

## Questions that come up

**Why folders instead of a wiki page?**  
Easier to version with the repo, review in PRs, and keep next to the code.

**What if the report is wrong?**  
That is why human review is required. The playbook drafts; a person decides.

**How do you keep them from growing forever?**  
Main file stays short. Detail moves to linked files. Drop steps that nobody follows.
