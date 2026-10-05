---
name: fail-check-analyzer
description: Analyze a failed CI check, test, lint, or build and produce a root-cause report with next actions. Use when a check fails, a test is red, CI is broken, or someone asks to analyze a failure, fail log, or failed pipeline.
---

# Fail check analyzer

Use when a check is **consistently failing** (same failure on retry). For intermittent passes, use `flaky-test-analyzer` instead.

If the failure shape is unclear, read [TAXONOMY.md](TAXONOMY.md).

## Inputs to gather

Collect only what is missing:

1. Failure signal: CI job name, test name, exit code, or screenshot
2. Log / stack trace (prefer the first failing assertion, not the whole run)
3. Recent change: PR, commit, or "unknown"
4. Environment: branch, browser/OS, staging vs CI, seed/data if relevant

## Analysis steps

1. **Classify** the failure using [TAXONOMY.md](TAXONOMY.md).
2. **Locate** the first real error (ignore cascade noise after it).
3. **Separate**:
   - product bug
   - test bug
   - environment / infra
   - data / fixture problem
4. **Map to change** if a PR or commit is available; say "unknown" if not.
5. **Propose** the smallest next action that would confirm the hypothesis.

## Output format

```markdown
## Fail check report

**Check:** <job or test name>
**Verdict:** product bug | test bug | env/infra | data | unclear
**Confidence:** high | medium | low

### What failed
<one sentence>

### Evidence
- <log line or assertion>
- <file:line if known>

### Likely root cause
<hypothesis>

### Not the cause (ruled out)
- ...

### Next actions
1. <fastest confirmation step>
2. <fix path if confirmed>
3. <owner: QA | Dev | DevOps>

### Human review (required)
**Status:** awaiting human review  
**Do not** merge, close the bug, skip the check, or change CI until a reviewer accepts this report.
```

## Human review (mandatory)

This playbook **drafts analysis only**. A person must review the report before any action.

- Present the report and stop. Do not apply fixes, reopen/close tickets, mute checks, or edit CI unless a reviewer explicitly asks after review.
- End every report with: `Human review required before acting on this analysis.`
- If a reviewer rejects the verdict, revise from their feedback.

## Rules

- Do not invent log lines. Quote only what was provided or found.
- Prefer one primary cause. List secondary causes only if evidence supports them.
- If logs are missing, say what to paste next — do not guess the stack.
- If the same check sometimes passes, stop and switch to flaky analysis.
