# Example review comments

## Critical

`src/api/users.ts`: the `/users/:id` handler interpolates `id` into a SQL string. Use a parameterized query so a caller cannot read or change other rows.

## Suggestion

`src/lib/dates.ts`: `new Date(string)` is timezone-dependent. Parse as UTC so report totals match across machines.

## Note

`README.md` still documents the old `/v1/login` path. Update it in a follow-up if this PR is already large.
