---
name: pr-review
description: Review a pull request or local diff for correctness, security, and maintainability. Use when the user asks for a code review, PR review, or feedback on a branch.
---

# PR review

Read [STANDARDS.md](STANDARDS.md) before commenting. Read [examples.md](examples.md) only if the review style is unclear.

## Steps

1. Identify the change set (`git diff main...HEAD` or the files the user named).
2. Walk the checklist below. Skip items that do not apply.
3. Group findings by severity. Do not pad the review with style nits if there are correctness bugs.
4. End with a merge recommendation: **approve**, **request changes**, or **comment**.

## Checklist

- [ ] Behavior matches the stated intent
- [ ] Edge cases and error paths are handled
- [ ] No secrets, tokens, or credentials in the diff
- [ ] Input is validated at trust boundaries
- [ ] Tests cover the new behavior, or a gap is called out
- [ ] Names and structure match the surrounding code

## Finding format

- **Critical**: must fix before merge
- **Suggestion**: worth changing, not blocking
- **Note**: optional, for learning

Each finding: file path, what is wrong, why it matters, a concrete fix.
