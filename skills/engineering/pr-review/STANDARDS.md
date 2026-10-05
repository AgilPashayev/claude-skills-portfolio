# Review standards

Loaded only when running the PR review playbook. Keep team-specific rules here so `SKILL.md` stays short.

## Security

- Reject SQL, shell, or HTML built from unsanitized user input.
- Reject new network listeners, auth bypasses, or disabled TLS checks.
- Flag `eval`, unbounded deserialization, and world-writable files.

## Tests

- New branches need a test or an explicit reason they cannot have one.
- Do not accept tests that only assert mocks.

## Style

- Match the repo. Do not restyle unrelated files.
- Prefer small functions that do one thing. Do not demand rewrites of working code.
