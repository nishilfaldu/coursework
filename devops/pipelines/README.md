# CI/CD Pipeline with GitHub Actions

[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)](https://docs.github.com/actions)
[![C++](https://img.shields.io/badge/C++-MSBuild-00599C?logo=cplusplus&logoColor=white)](https://learn.microsoft.com/cpp/build/msbuild-visual-cpp)
![Runner](https://img.shields.io/badge/runner-windows--latest-blue)

A software-architecture assignment whose real subject is the **build pipeline**,
not the program. A deliberately tiny C++ solution (a DLL, an executable, and a
unit-test project) is the vehicle; the deliverable is a multi-stage
**GitHub Actions** pipeline that builds, lints, tests, and ships it.

## The pipeline

Two workflows model the two events in a typical Git workflow:

**`push.yml` — on push to `master` (full delivery):**

```
        ┌─────────┐     ┌──────┐
        │  build  │     │ lint │
        └────┬────┘     └──┬───┘
             └──────┬──────┘
                    ▼
                 ┌──────┐
                 │ test │        (needs: build, lint)
                 └──┬───┘
                    ▼
              ┌────────────┐
              │ SaveBinary │     (needs: test)
              └────────────┘
   build the .sln with MSBuild → upload artifact →
   run VSTest on the test DLL → commit the built .exe back to the repo
```

**`pull.yml` — on pull request to `master` (gate before merge):**

```
   build  +  lint  ──►  test
```

Same `build → lint → test` gate, but **no deploy** — a PR only has to prove it
compiles and passes tests; nothing ships until it's merged.

### Concepts demonstrated

- **Job dependencies** via `needs:` to enforce stage ordering.
- **Artifact passing** between jobs (`upload-artifact` / `download-artifact`) so
  the built binary moves from `build` to `test` to deploy.
- **Event-driven triggers** — different pipelines for `push` vs `pull_request`.
- **Automated build + test** with MSBuild and VSTest on a Windows runner.
- **Continuous delivery** — the `SaveBinary` job commits the compiled executable
  back to the repository after tests pass.

## The (intentionally minimal) program

| Component | Purpose |
|-----------|---------|
| `Application/` | A DLL exporting `CoolClass::Calc(a, b)` — returns `2a` if `a == b`, else `a + b` |
| `PipeplinesExe/` | A console executable that links the DLL and calls `Calc` |
| `UnitTest1/` | MSVC unit tests asserting `Calc`'s behaviour |
| `Pipeplines.sln` | The Visual Studio solution tying them together |

## Notes

- The workflows target a **Windows runner** (MSBuild + VSTest), matching the
  Visual Studio C++ toolchain.
- In this archived collection the workflows live under the project folder for
  reference; GitHub only executes workflows from a repository's root
  `.github/workflows/`, so they don't run here.
- The Visual Studio project names keep the original "Pipeplines" spelling to
  avoid breaking the solution's internal references.
