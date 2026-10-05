# Common flake patterns

Load when ranking intermittent test causes.

| Pattern | Typical signals | Stabilization |
| --- | --- | --- |
| **Timing / race** | Fails under load; fixed sleep; animation; async render | Wait for role/text/network idle; avoid arbitrary timeout bumps alone |
| **Selector brittleness** | Works until CSS/class rename; duplicate matches | Prefer role + name; unique test ids; assert visible state |
| **Order dependence** | Fails only when run with suite; passes in isolation | Reset state; no reliance on previous test |
| **Shared data** | Unique email collisions; parallel workers | Per-test fixtures; worker-scoped data; cleanup |
| **Network / third party** | External API timeouts; CDN; email provider | Mock in unit/integration; contract tests for real calls |
| **Clock / timezone** | Fails near midnight; DST; `Date.now()` | Fake timers; fixed clock; UTC fixtures |
| **Resource limits** | Only on small CI runners; OOM; CPU throttle | Reduce parallelism; lighter fixtures; raise resources if justified |
| **Browser-only** | One browser/engine; headless vs headed | Engine-specific waits; feature detection; quarantine that browser briefly |
| **Retry masking** | Passes only because CI retries 3× | Fix root cause; treat retry pass as still a flake |

## Ranking heuristic

Score higher when:

- Failure rate changes with CI load or parallelism
- Diff between pass and fail logs shows timing/order, not assertion content
- Test already contains `sleep`, `waitForTimeout`, or unconditional retry

Score lower (likely hard fail) when:

- Same assertion fails every time after a specific commit
- Missing env var or wrong URL in all red runs
