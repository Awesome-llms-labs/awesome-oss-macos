# macOS-Native vs. Electron (and Friends)

This list includes both native macOS apps and cross-platform ones. The `macos_native` flag in `data/oss-macos.json` tells you which is which. Here's what the distinction costs and buys you.

## Native macOS apps (`macos_native: true`)

Built with Swift/SwiftUI, Objective-C, or AppKit/UIKit directly against macOS frameworks.

**Upsides**
- Launch instantly and idle at tens of MB of RAM (Rectangle, Maccy, Stats, Ice).
- Follow platform conventions: native menus, trackpad gestures, menu-bar extras, Shortcuts actions, system appearance.
- Behave correctly with Spaces, Stage Manager, fullscreen, and accessibility APIs.

**Downsides**
- macOS-only by construction — no Linux/Windows version.
- Smaller contributor pools; a single maintainer's burnout can stall the app (check `status`).

## Electron / Tauri / cross-platform (`macos_native: false`)

One codebase (usually web tech) shipped on every desktop OS: VS Code, Signal, Element, Logseq, Joplin, OBS Studio, KeePassXC (Qt).

**Upsides**
- Feature parity across platforms; larger contributor communities; faster feature velocity.
- Your config and muscle memory transfer to Linux/Windows machines.

**Downsides**
- Heavier: an Electron app typically idles at 200–500 MB RAM vs. <50 MB for a comparable native app.
- Slightly off platform feel: custom title bars, non-native file dialogs, occasional gesture quirks.

## Terminal / CLI tools (`macos_native: false`)

Tools like ripgrep, fzf, tmux, and Homebrew itself aren't GUI apps at all — they're in the `terminal-system` category. "Native" doesn't apply; what matters is Apple Silicon support (universal or arm64 builds) and Homebrew availability, which nearly all of them have.

## Qt apps (a middle ground)

KeePassXC, VLC, qutebrowser, and Krita use Qt — native-compiled, lighter than Electron, but with their own widget styling. On macOS they feel 90% native and perform well.

## How to use the flag

- Building a lean menu-bar setup? Filter `macos_native: true` in `productivity` and `utilities`.
- Need the same tool on your Linux server? Prefer `macos_native: false` cross-platform entries.
- Neither is a quality judgment — IINA (native) and mpv (cross-platform) are both excellent players; pick by taste.
