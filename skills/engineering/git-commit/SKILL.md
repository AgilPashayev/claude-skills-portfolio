---
name: git-commit
description: Draft a conventional commit message from the current git diff. Use when asked to commit, write a commit message, or summarize staged changes.
---

# Git commit

## Steps

1. Run `git status` and `git diff` (include staged and unstaged).
2. If nothing changed, stop and say so.
3. Write one subject line, max 72 characters, in this shape:

   `type(scope): imperative summary`

   Allowed types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.
4. Add a body only when the why is not obvious from the subject.
5. Do not commit unless explicitly asked to commit.
6. Never amend a commit that has already been pushed.

## Examples

Input: added JWT login and a refresh cookie.

```
feat(auth): add JWT login with refresh cookies

Keep access tokens short-lived and store refresh tokens httpOnly.
```

Input: dates in reports were off by one in US timezones.

```
fix(reports): use UTC when formatting report dates
```
