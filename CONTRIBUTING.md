# Contributing

Thanks for helping keep this the most current directory of open-source macOS apps!

## Adding an entry

1. **Check it fits:** an **open-source** application or system tool that runs on macOS — native (Swift/SwiftUI, Objective-C), Electron/Tauri where macOS is first-class, or a terminal tool macOS users rely on. Excluded: iOS-only apps, proprietary freeware ("free but closed"), source-available-but-restricted licenses (SSPL, BSL, custom "community" licenses), and repos that no longer exist.
2. **Verify the license yourself.** Open the repo's LICENSE file (or the license badge on its GitHub page) and confirm the SPDX identifier. **Never invent a license.** If you can't confirm it, set `license` to `"unverified"` and `oss_verified` to `false`.
3. **Add to the right section** of `README.md` (categories: developer-tools, productivity, utilities, media, design, security-privacy, terminal-system, notes-knowledge, communication, browsers).
4. **One entry = one bullet.** Format:
   `- [Name](https://github.com/owner/repo) — ` one-line description.
   Mark license confidence honestly: `✅ MIT (verified)` only when you confirmed the license on the official repo; otherwise `⚠️ license unverified`.
5. **Add the matching record** to `data/oss-macos.json` with these exact fields:

| field | type | values |
|---|---|---|
| `name` | string | app name |
| `repo_url` | string | `https://github.com/owner/repo` |
| `homepage` | string | official `https://` site, or `""` |
| `description` | string | one sentence |
| `license` | string | SPDX id (e.g. `"MIT"`, `"GPL-3.0"`, `"Apache-2.0"`), or `"unverified"` |
| `category` | string | one of the 10 categories above |
| `macos_native` | bool | `true` for native Swift/ObjC/AppKit apps |
| `last_commit_verified` | bool | `true` only if you checked the repo's recent commit activity |
| `oss_verified` | bool | `true` only if you confirmed the license on the official repo |
| `source_url` | string | `https://` URL proving the license (repo page or LICENSE file), or `""` |
| `status` | string | `active` / `maintenance` / `archived` |

6. **Status changes:** if a project is archived, goes quiet for 2+ years, or changes license, update its README entry *and* its JSON record (`status`, and `license`/`oss_verified` if the license changed).

## Style rules

- Link the **official repo** (`https://github.com/owner/repo`), never a blog post, reseller, or repackaged download.
- Descriptions are one sentence, neutral, and macOS-relevant ("menu-bar calendar", " tiling window manager").
- Facts that can change (version numbers, feature lists) are omitted — link the repo instead of hard-coding details that rot.
- Proprietary lookalikes (Raycast, Alfred, Bartender, Magnet, 1Password, Obsidian, Warp, Arc, Little Snitch, …) do **not** get entries. Suggest the OSS alternative instead.
- Privacy-relevant facts (network access, telemetry) must be sourced.

## CI

Every PR runs:
- **Link check** (lychee) over all markdown files — no dead links.
- **Data validation** — `data/oss-macos.json` must parse, every record must have the required fields, `category`/`status` must be from the allowed sets, and verified entries must carry an `https://` `source_url`.
- **README sync check** — the README summary total and per-category counts must match the curated data file.

Run locally before pushing:

```bash
python3 scripts/validate_data.py
```
