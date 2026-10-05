---
name: release-notes
description: Turn git commits or a changelog fragment into user-facing release notes. Use when asked for a changelog, release notes, or a version summary.
---

# Release notes

When a version range is given, run:

```bash
python scripts/collect_commits.py v1.0.0 HEAD
```

If Python is unavailable, run `git log --oneline <from>..<to>` instead.

## Steps

1. Collect commits for the range (default: last tag to `HEAD`).
2. Drop merge commits and noise (`chore`, `wip`, formatting-only).
3. Group remaining work into **Added**, **Fixed**, **Changed**.
4. Write for the product audience, not the git history. No ticket IDs unless requested.
5. Keep the whole notes file under one screen when possible.
6. Have a person review the draft before publishing.

## Template

```markdown
## vX.Y.Z — YYYY-MM-DD

### Added
- ...

### Fixed
- ...

### Changed
- ...
```
