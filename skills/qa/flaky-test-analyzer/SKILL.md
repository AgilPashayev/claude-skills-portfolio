---
name: flaky-test-analyzer
description: Diagnose intermittent or flaky tests by ranking likely flake causes and proposing stabilization fixes. Use when a test is flaky, intermittent, passes on retry, fails randomly, or someone asks to analyze flake rate or unstable CI.
---

# Flaky test analyzer

Use when the same test **sometimes passes and sometimes fails** with no intentional code change. For a hard fail every run, use `fail-check-analyzer` instead.

Read [FLAKE_PATTERNS.md](FLAKE_PATTERNS.md) when ranking causes.

## Inputs to gather

1. Test name and file path
2. Pass/fail pattern: "fails 1/10", "red only on CI", "only Firefox", etc.
3. One failing log and one passing log if available
4. Waits, sleeps, retries already in the test
5. Shared state: DB, cookies, localStorage, parallel workers

## Analysis steps

1. Confirm it is a flake (intermittent), not a new hard failure.
2. Rank causes using [FLAKE_PATTERNS.md](FLAKE_PATTERNS.md). Pick top 1–3.
3. Check for **shared mutable state** and **time/order dependence**.
4. Prefer fixes in this order:
   1. Wait on a condition (not a fixed sleep)
   2. Isolate data / workers
   3. Fix a product race if the flake exposes a real bug
   4. Quarantine only as a last temporary step
5. Suggest how to prove the fix (rerun count, CI job, seed).

## Output format

```markdown
## Flaky test report

**Test:** <name> (`path`)
**Pattern:** <e.g. fails ~20% on CI, green locally>
**Top causes (ranked):**
1. <cause> — why
2. <cause> — why

### Evidence
- failing run: ...
- passing run: ...

### Stabilization plan
1. <immediate fix>
2. <hardening>
3. <how to verify: N reruns / job name>

### Product risk?
yes/no — <if the flake may hide a real race>

### Quarantine?
only if: <reason> · remove by: <date or PR>

### Human review (required)
**Status:** awaiting human review  
**Do not** quarantine, delete, skip, or rewrite the test until a reviewer accepts this report.
```

## Human review (mandatory)

This playbook **drafts analysis only**. A person must review the report before any action.

- Present the report and stop. Do not quarantine tests, change retries, merge “fixes”, or edit CI unless a reviewer explicitly asks after review.
- End every report with: `Human review required before acting on this analysis.`
- If a reviewer rejects the ranked causes, revise from their feedback.

## Rules

- Do not recommend longer blind `sleep()` as the main fix.
- Call out when the flake is a **real race in the product**, not only a bad test.
- If there is no intermittency evidence, switch to `fail-check-analyzer`.
