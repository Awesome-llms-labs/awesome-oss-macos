# Glossary

Terms that come up when evaluating open-source macOS software.

- **Universal binary** — a macOS app bundle containing both Intel (`x86_64`) and Apple Silicon (`arm64`) code. Runs natively on both.
- **Apple Silicon native** — built for `arm64`; runs at full speed on M-series Macs.
- **Rosetta 2** — Apple's translation layer that runs Intel binaries on Apple Silicon Macs. Works transparently, with a small performance cost.
- **SIP (System Integrity Protection)** — macOS's lockdown of system files and processes. Some tools (notably yabai) require SIP to be partially disabled for full functionality.
- **Notarization** — Apple's automated malware scan for distributed apps. OSS apps distributed outside the App Store are usually notarized; unsigned builds trigger Gatekeeper warnings on first launch (right-click → Open to bypass).
- **Gatekeeper** — macOS's check that only trusted software runs. Unsigned or ad-hoc-signed OSS builds may be blocked until you explicitly allow them.
- **Homebrew cask** — a Homebrew package definition for GUI macOS apps (`brew install --cask …`).
- **Formula** — a Homebrew package definition for command-line tools.
- **Tiling window manager** — arranges windows in a non-overlapping grid automatically (i3-style), as opposed to macOS's default floating windows.
- **Menu bar app** — a utility that lives in the macOS menu bar (top-right), often without a Dock icon.
- **LaunchAgent / LaunchDaemon** — macOS's per-user / system-wide background service mechanism (the `launchd` equivalent of systemd units / cron jobs).
- **SPDX license identifier** — the standard short name for a license (e.g. `MIT`, `Apache-2.0`, `GPL-3.0-only`) used in the `license` field of `data/macos.json`.
- **Copyleft (GPL-family)** — licenses requiring derivative works to stay open-source under the same terms. Fine for personal use; matters if you redistribute.
- **Permissive (MIT/Apache/BSD)** — licenses allowing reuse in proprietary software with minimal conditions.
- **Verified ✅ / Unverified ⚠️** — this repo's flags. ✅ means the entry's facts were confirmed on the project's official GitHub repo page or official site; ⚠️ means something couldn't be confirmed and the entry says what.
