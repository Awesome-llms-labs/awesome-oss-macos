# Contributing to Awesome OSS macOS

Thanks for helping keep this list honest and useful. A few rules before you open a PR:

## What belongs here

- **Genuinely open-source macOS apps or utilities** — source must be publicly available under a recognized open-source license (MIT, Apache-2.0, GPL, BSD, MPL, …).
- **macOS-first or with a real macOS build** — cross-platform tools count only if macOS is a first-class target (native build, not "runs under X11 maybe").
- **No proprietary software.** Raycast, Alfred, Bartender, CleanMyMac, iStat Menus, Shottr, AppCleaner, OrbStack, Warp, Arc — proprietary, out of scope. No "freemium with an OSS core that can't actually be built" either.
- **No abandonware with no source.** If the repo is gone or private, the entry goes to `docs/status-changes.md` instead.
- **No vaporware.** Announced-but-unshipped projects are excluded until a public repo exists.

## Entry requirements

Every entry in `data/macos.json` needs:

| Field | Rule |
|---|---|
| `name` | Exact project name |
| `description` | 1–2 sentences, neutral, no marketing fluff |
| `license` | The SPDX-style license **as stated in the repo's LICENSE file** — checked, not assumed |
| `category` | One of the categories in the CI validator |
| `github_url` | `https://github.com/owner/repo` |
| `stars` | Integer star count **as of the day you check it**, or `null` |
| `official_site` | Project homepage, or `null` |
| `apple_silicon` | `"universal binary"`, `"Apple Silicon native"`, `"Intel via Rosetta 2"`, or `null` if unknown — never guessed |
| `verified` | `true` **only** if you confirmed the project on its official GitHub repo page or official site. Otherwise `false` with… |
| `unverified_reason` | …a plain-English reason. "Could not confirm license on official source" beats a wrong license every time |

## How to submit

1. Add the entry to `data/macos.json` (keep alphabetical order within its category in `README.md`).
2. Add the matching bullet to `README.md` in the right category section.
3. If the entry replaces or retires an old one, note it in `docs/status-changes.md`.
4. Open a PR. CI runs lychee link checks and JSON validation — both must be green.

## Honesty policy

This repo's whole value is the ✅/⚠️ flags. If the official page is ambiguous, the entry says so. Unverified is a feature, not a failure.
