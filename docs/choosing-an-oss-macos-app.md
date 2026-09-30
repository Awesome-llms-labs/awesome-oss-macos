# Choosing an OSS macOS App

How to pick the right open-source app for your Mac without regretting it later.

## 1. Start with what kind of app it is

| App type | What to prefer | Examples in this list |
|---|---|---|
| Window managers / menu-bar tools | Native Swift/ObjC — they sip memory and respect macOS conventions | Rectangle, AltTab, Maccy, Stats, Ice |
| Note-taking / knowledge | AGPL apps are fully open but the license restricts commercial SaaS forks — fine for personal use | Logseq, Joplin, Trilium, SiYuan |
| Terminals / CLI tools | Cross-platform is fine; pick for features, not nativeness | Ghostty, WezTerm, Alacritty, Kitty |
| Media players / editors | Native players (IINA) feel best; cross-platform editors (Kdenlive, Shotcut) are full-featured | IINA, VLC, mpv, HandBrake |
| Security tools | Open source matters most here — you want the firewall you trust to be auditable | LuLu, Santa, KeePassXC, WireGuard |
| Browsers | Forks of Firefox/Chromium with the telemetry stripped | Ungoogled Chromium, Zen, Firefox |

## 2. Check the license before you depend on it

- **MIT / Apache-2.0 / BSD / ISC / Unlicense** — do anything with it, including at work.
- **GPL-2.0 / GPL-3.0** — fine to use; if you *modify and distribute* it, share your changes under the same license.
- **AGPL-3.0** — same as GPL, plus the "network use is distribution" clause: if you run a modified copy as a service, you must share the source.
- **EUPL-1.2** (eza) — copyleft like GPL, officially compatible with GPL.
- **MPL-2.0** (Firefox family) — file-level copyleft: changes to existing files stay open, new files can be proprietary.
- **Custom / source-available** — not open source by the OSI definition. This list excludes them; see `licenses-explained.md`.

## 3. Check the project's pulse

Every entry carries a `status`: `active` (commits in the last ~2 years), `maintenance` (alive but quiet), `archived` (read-only). For a tool you'll depend on daily (password manager, window manager), prefer `active`. For a stable single-purpose utility (ScrollReverser, qlmarkdown), `maintenance` is fine — some tools are simply *done*.

## 4. Native vs. Electron

Native macOS apps launch faster, use less RAM, and follow platform conventions (menu bar, trackpad gestures, Shortcuts). Electron apps (VS Code, Signal, Element, Logseq) trade that for cross-platform consistency. Neither is "wrong" — the `macos_native` flag in the data file tells you which you're getting. See `macos-native-vs-electron.md`.

## 5. Distribution: GitHub releases vs. Homebrew

Most apps here ship `.dmg` files on GitHub Releases and many are also `brew install --cask`able. Homebrew casks make updates painless (`brew upgrade --cask`), but always verify the cask points at the official release — that's what `repo_url` is for.

## 6. Watch for the proprietary lookalikes

Several beloved "Mac apps" are proprietary freeware or freemium — they are **not** in this list: Raycast, Alfred, Bartender, Magnet, CleanShot X, Shottr, 1Password, Obsidian, Notion, Warp, Arc, Vivaldi, Little Snitch, BetterTouchTool, AppCleaner, OnyX. Each has an OSS alternative listed here (e.g. Rectangle instead of Magnet, Maccy instead of Paste, LuLu instead of Little Snitch). See the README's "Notable exclusions" section.
