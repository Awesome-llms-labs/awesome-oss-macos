# Licenses Explained

Every entry in this list carries a `license` field and an `oss_verified` boolean. This page explains what the license values mean and why some apps are marked `unverified`.

## The licenses you'll see

| License | Type | What it means for you |
|---|---|---|
| MIT | Permissive | Do anything — use, modify, sell. Keep the copyright notice. |
| Apache-2.0 | Permissive | Like MIT, plus an explicit patent grant. |
| BSD-2-Clause / BSD-3-Clause | Permissive | Like MIT with slightly different wording. |
| ISC | Permissive | Functionally equivalent to MIT (common for terminal tools like tmux, Starship). |
| Unlicense / public domain | Permissive | No restrictions at all (Karabiner-Elements, yt-dlp). |
| GPL-2.0 / GPL-3.0 | Copyleft | Free to use and modify; if you distribute a modified copy you must share the source under the same license. |
| AGPL-3.0 | Copyleft (network) | Like GPL, plus: running a modified copy as a network service counts as distribution. Matters for self-hosters, not for desktop use. |
| LGPL-2.1 / LGPL-3.0 | Weak copyleft | Libraries: you can link from proprietary code; changes to the library itself stay open. |
| MPL-2.0 | File-level copyleft | Changes to existing files stay open; new files you add can be under any license (Firefox, Thunderbird, Zen). |
| EUPL-1.2 | Copyleft | EU public license, copyleft like GPL and explicitly GPL-compatible (eza). |
| Vim license | Permissive-ish | Charityware: you may use and copy it, and are encouraged to donate to a charity (Vim, MacVim). |
| CC-BY-4.0 | Content license | Applies to documentation/content rather than code (tldr pages). Listed for completeness where a project has no separate code license. |
| unverified | Unknown | The repo's license could not be confirmed on its official GitHub page (missing, custom, or ambiguous). Treat the app as "source visible, terms unclear" until you read its LICENSE file. |

## Why `oss_verified` exists

`oss_verified: true` means the license above was read on the project's official GitHub repository (via its license metadata or LICENSE file) — not copied from a third-party list. `false` means we could not confirm it: the repo may have no license file, a custom non-SPDX license GitHub can't classify, or conflicting claims. **Never treat an unverified license as permission** — open the repo's LICENSE file first.

## Licenses that look open but aren't

Excluded from this list because they fail the Open Source Definition:

- **Server Side Public License (SSPL)** — e.g. some database-adjacent tools. Discriminates against SaaS use; not OSI-approved.
- **Business Source License (BSL)** — source is visible but commercial use is restricted until a change date (HashiCorp tools after 2023).
- **Custom "community" / "fair" licenses** — MiniMax-style community licenses and similar look permissive but add use restrictions.
- **"Free for personal use"** — freeware, not open source. No source, no freedoms.

## A note on GPL apps in the Mac App Store

Apple's App Store terms conflict with GPL distribution, which is why most GPL macOS apps (IINA, KeePassXC, GIMP) distribute via GitHub releases or their own sites rather than the App Store. Download from `repo_url` or the official homepage — never a repackaged copy.
