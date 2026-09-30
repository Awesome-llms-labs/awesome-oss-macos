# Choosing an open-source macOS app

A short decision guide — the questions to ask before you install anything.

## 1. What does "open source" actually cover?

Not all "open" is equal:

- **Full source, OSI-approved license** (MIT, Apache-2.0, GPL, BSD, MPL) — you can read it, build it, fork it. This list's default.
- **Source-available, not OSI** (e.g. custom "personal use only" licenses) — you can read it, but not necessarily fork or redistribute it. Such projects are excluded from this list or flagged explicitly.
- **Open core** — the engine is OSS, the Mac app you download is proprietary. The proprietary part is out of scope here.
- **"Free" ≠ open source.** Plenty of excellent Mac freeware (Raycast, Alfred, Shottr, AppCleaner, Bartender) keeps its source closed. They are deliberately not in this list.

Check the `license` field on every entry — it was read from the project's LICENSE file, not assumed.

## 2. Match the tool to the job

- **Window management:** macOS's built-in tiling (Sonoma+) covers basics. Reach for Rectangle/Spectacle-style snapping for keyboard shortcuts, Amethyst/AeroSpace/yabai for real tiling. yabai needs SIP partially disabled — decide if that's acceptable for you.
- **Terminal:** iTerm2 is the veteran (GPL-2.0); Alacritty/Kitty/Ghostty/WezTerm are GPU-accelerated and config-file driven — pick your config language (TOML, YAML, Lua…) before you pick the emulator.
- **Package management:** Homebrew is the default answer; MacPorts is the older, more BSD-flavored alternative. Both are fine; don't run both.
- **Security:** Objective-See's suite (LuLu firewall, KnockKnock, BlockBlock, …) is free and open — a solid baseline before paying for anything.
- **Media:** IINA is the "feels native" player (mpv engine); mpv itself for maximum scriptability; VLC for "plays literally everything".
- **Archiving:** Keka handles the formats macOS can't. Note its licensing history before assuming.

## 3. Check the Apple Silicon column

Most maintained projects now ship universal binaries or Apple Silicon-native builds. If the `apple_silicon` field is `null`, the build status was genuinely unknown — check the project's Releases page before installing on an M-series Mac; Intel-only builds still run under Rosetta 2, but native is better.

## 4. Maintenance matters more than stars

A ⭐ count is a popularity snapshot, not a health metric. Before adopting a tool, glance at the repo: recent commits? open issues getting replies? An archived repo with a great README is a liability for security-sensitive tools (firewalls, cleaners, anything with root access).

## 5. Prefer the official distribution channel

Download from the project's GitHub Releases or official site. Third-party "mac cracked apps" sites bundling OSS tools are a classic malware vector — the whole point of open source is that you don't need them.
