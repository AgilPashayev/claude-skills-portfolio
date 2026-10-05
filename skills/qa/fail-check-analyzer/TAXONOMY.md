# Failure taxonomy

Load only when classifying a failed check.

## Categories

| Category | Signals |
| --- | --- |
| **Assertion / product** | Expected value wrong; UI state missing; API returns unexpected body/status |
| **Test bug** | Wrong selector, wrong wait, outdated fixture, brittle timing in a *stable* env |
| **Build / compile** | Type errors, missing imports, bundler failures before tests run |
| **Lint / static** | ESLint, formatting, typecheck as a gate |
| **Env / infra** | Missing secrets, wrong base URL, service down, Docker/network, quota |
| **Data** | Seed missing, unique constraint, stale DB, timezone/locale fixtures |
| **Dependency** | Package not installed, version mismatch, peer dependency conflict |
| **Auth / permission** | 401/403, expired token, role missing in CI user |
| **Flake candidate** | Passes on retry with no code change — switch to `flaky-test-analyzer` |

## First-error rule

In long logs, find the **first** non-noise error. Later `Error: ...` lines are often consequences.

Noise to skip when searching:

- retry wrappers
- browser console warnings unrelated to the assertion
- teardown failures after the real fail
