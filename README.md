# Coursework

A curated home for projects I built during my computer science coursework,
collected here so each one stays documented, runnable, and easy to browse.

Rather than a dozen scattered, half-finished repositories, everything lives in
one place — **organized by theme, not by course number** — so a project is easy
to find whether you remember it as "that AES thing" or "the data-viz one." Each
project keeps its own README with context and run instructions.

## Index

| Theme | Project | What it is |
|-------|---------|------------|
| Security | [aes-encryption](security/aes-encryption) | AES round transformations and key schedule, implemented from scratch in Python |
| Security | [buffer-overflow-attack](security/buffer-overflow-attack) | Stack buffer overflow that pops a root shell on a Set-UID program (SEED Lab) |
| Security | [meltdown-attack](security/meltdown-attack) | Meltdown (CVE-2017-5754): leak kernel memory via a cache timing side channel (SEED Lab) |
| DevOps | [pipelines](devops/pipelines) | Multi-stage CI/CD pipeline (build → lint → test → deploy) with GitHub Actions |
| Algorithms | [algorithms](algorithms) | 99 data-structures & algorithms problems solved in Python, by difficulty |

*More projects are being cleaned up and added here over time.*

## How it's organized

```
coursework/
├── security/            # cryptography, exploitation, systems security
├── devops/              # CI/CD, build pipelines, automation
├── data-visualization/  # interactive data viz projects
├── systems/             # low-level / systems programming
├── algorithms/          # data structures and algorithms
├── web/                 # web apps and UIs
└── games/               # small games and fun builds
```

Folders appear as projects are added. Each project folder is self-contained:
clone the repo, open the project, follow its README.

## A note on these projects

These are learning projects from my degree — some polished, some scrappy, all
kept for reference. They're not my flagship work (see my pinned repositories for
that), but they document the range of things I've explored, from Galois-field
arithmetic to interactive data visualization.
