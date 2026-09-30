# Glossary

Terms you'll meet in this list and in macOS open-source culture generally.

- **Cask** — a Homebrew package definition for a GUI macOS app (`brew install --cask rectangle`). Distinct from a *formula*, which builds CLI tools from source.
- **Formula** — a Homebrew package definition for command-line software.
- **Menu-bar app / menu extra** — an app that lives in the macOS menu bar (right side, near the clock) rather than the Dock: Stats, Ice, Maccy, Itsycal.
- **Tiling window manager** — automatically arranges windows in non-overlapping tiles: Yabai, Amethyst, AeroSpace. Contrast with *window snapping* (Rectangle, Loop), which moves windows on demand.
- **System extension / kernel extension (kext)** — privileged code that extends macOS: LuLu's firewall and Karabiner-Elements' keyboard handling use system extensions (modern) rather than deprecated kexts. Installing one requires approval in System Settings → Privacy & Security.
- **Notarization** — Apple's automated malware scan for distributed apps. OSS apps on GitHub Releases are usually signed *and* notarized; if macOS warns on first launch, right-click → Open once.
- **Universal binary** — a single app bundle containing both Intel (x86_64) and Apple Silicon (arm64) code. Prefer it over Intel-only builds (which run under Rosetta 2 translation).
- **App Store vs. GitHub Releases** — many OSS macOS apps skip the App Store (GPL conflicts, sandboxing limits) and ship `.dmg` files on GitHub Releases instead. That's normal, not suspicious — but always download from the official `repo_url`.
- **Copyleft** — a license (GPL, AGPL) requiring distributed modifications to stay open under the same license. See `licenses-explained.md`.
- **Permissive license** — a license (MIT, Apache-2.0, BSD, ISC) allowing nearly any use, including in proprietary software.
- **Source-available** — you can read the source, but the license restricts some uses. Not open source; excluded from this list.
- **OSI (Open Source Initiative)** — maintains the Open Source Definition. "OSS" in this list means meeting it.
- **SPDX identifier** — a short standard code for a license (`MIT`, `GPL-3.0-only`, `Apache-2.0`). The `license` field uses these.
- **SIP (System Integrity Protection)** — macOS protection for system files. Tools like Yabai need *partial* SIP disablement for advanced features — a real tradeoff; AeroSpace and Amethyst work without it.
- **XPC / Mach services** — macOS inter-process communication. Menu-bar utilities often split into an app plus a privileged helper.
- **Launch agent / launch daemon** — macOS background-task definitions (`~/Library/LaunchAgents`). Persistence monitors like BlockBlock and KnockKnock watch these locations.
- **Dotfiles** — plain-text config files (`.zshrc`, `.tmux.conf`) many terminal tools in this list are configured through.
