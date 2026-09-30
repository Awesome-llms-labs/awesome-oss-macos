# Awesome OSS macOS [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of **80 open-source macOS applications** — native Mac apps plus cross-platform tools where macOS is first-class. Every entry links to its source repository, and every license was verified against the project's official license file or metadata on 2026-09-30.

- ✅ **80/80** licenses verified from official sources
- 🍎 **27** native macOS apps (AppKit/Swift/Objective-C)
- 📦 Machine-readable data in [`data/oss-macos.json`](data/oss-macos.json)

## Contents

- [🛠️ Developer Tools](#developer-tools) (8)
- [⚡ Productivity](#productivity) (7)
- [🧰 Utilities](#utilities) (9)
- [🎬 Media](#media) (10)
- [🎨 Design](#design) (8)
- [🔒 Security & Privacy](#security-privacy) (8)
- [💻 Terminal & System](#terminal-system) (12)
- [📝 Notes & Knowledge](#notes-knowledge) (6)
- [💬 Communication](#communication) (6)
- [🌐 Browsers](#browsers) (6)
- [Notable exclusions](#notable-exclusions)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## 🛠️ Developer Tools

Editors, package managers, database GUIs, and dev utilities.

- **[Homebrew](https://github.com/Homebrew/brew)** — The missing package manager for macOS. [`BSD-2-Clause`](https://github.com/Homebrew/brew) · [website](https://brew.sh)
- **[Visual Studio Code](https://github.com/microsoft/vscode)** — Free, extensible code editor with a huge extension marketplace. [`MIT`](https://github.com/microsoft/vscode) · [website](https://code.visualstudio.com)
- **[Zed](https://github.com/zed-industries/zed)** — Blazing-fast, GPU-accelerated code editor with built-in collaboration. [`GPL-3.0`](https://github.com/zed-industries/zed/blob/HEAD/LICENSE-GPL) · [website](https://zed.dev)
- **[Neovim](https://github.com/neovim/neovim)** — Hyperextensible Vim-based editor with Lua config and built-in LSP. [`Apache-2.0`](https://github.com/neovim/neovim/blob/HEAD/LICENSE.txt) · [website](https://neovim.io)
- **[GitUp](https://github.com/git-up/GitUp)** 🍎 — Native Mac Git client with a live, interactive repository graph. [`GPL-3.0`](https://github.com/git-up/GitUp) · [website](https://gitup.co)
- **[DBeaver](https://github.com/dbeaver/dbeaver)** — Universal database GUI for MySQL, Postgres, SQLite, and dozens more. [`Apache-2.0`](https://github.com/dbeaver/dbeaver) · [website](https://dbeaver.io)
- **[Sequel Ace](https://github.com/Sequel-Ace/Sequel-Ace)** 🍎 — Native Mac MySQL/MariaDB client, successor to Sequel Pro. [`MIT`](https://github.com/Sequel-Ace/Sequel-Ace/blob/HEAD/LICENSE) · [website](https://sequel-ace.com)
- **[CotEditor](https://github.com/coteditor/CotEditor)** 🍎 — Lightweight native Mac plain-text editor for code and prose. [`Apache-2.0`](https://github.com/coteditor/CotEditor/blob/HEAD/LICENSE) · [website](https://coteditor.com)

## ⚡ Productivity

Window management, clipboard managers, automation, and text expansion.

- **[Rectangle](https://github.com/rxhanson/Rectangle)** 🍎 — Move and resize windows with keyboard shortcuts and snap areas. [`MIT`](https://github.com/rxhanson/Rectangle/blob/HEAD/LICENSE) · [website](https://rectangleapp.com)
- **[AltTab](https://github.com/lwouis/alt-tab-macos)** 🍎 — Windows-style Alt-Tab switcher with live window thumbnails. [`GPL-3.0`](https://github.com/lwouis/alt-tab-macos) · [website](https://alt-tab.app)
- **[Loop](https://github.com/mrkai77/Loop)** 🍎 — Window management via a radial menu under your cursor. [`GPL-3.0`](https://github.com/mrkai77/Loop) · [website](https://github.com/mrkai77/Loop)
- **[Maccy](https://github.com/p0deje/Maccy)** 🍎 — Lightweight clipboard manager with search and keyboard-first paste. [`MIT`](https://github.com/p0deje/Maccy) · [website](https://maccy.app)
- **[Flycut](https://github.com/TermiT/Flycut)** 🍎 — Simple open-source clipboard manager for developers. [`MIT`](https://github.com/TermiT/Flycut) · [website](https://github.com/TermiT/Flycut)
- **[Espanso](https://github.com/espanso/espanso)** — Cross-platform text expander with snippets, forms, and scripting. [`GPL-3.0`](https://github.com/espanso/espanso) · [website](https://espanso.org)
- **[Hammerspoon](https://github.com/Hammerspoon/hammerspoon)** 🍎 — Automate macOS with Lua: window management, hotkeys, system scripting. [`MIT`](https://github.com/Hammerspoon/hammerspoon) · [website](https://www.hammerspoon.org)

## 🧰 Utilities

Menu-bar tools, system tweaks, input customization, and archivers.

- **[Stats](https://github.com/exelban/stats)** 🍎 — Menu-bar system monitor: CPU, memory, disks, network, sensors, battery. [`MIT`](https://github.com/exelban/stats/blob/HEAD/LICENSE) · [website](https://mac-stats.com)
- **[Hidden Bar](https://github.com/dwarvesf/hidden)** 🍎 — Hide menu-bar icons behind a toggleable separator. [`MIT`](https://github.com/dwarvesf/hidden) · [website](https://d.foundation/opensource)
- **[Ice](https://github.com/jordanbaird/Ice)** 🍎 *(maintenance)* — Powerful menu-bar manager: hide icons, reorder, multiple bars. [`GPL-3.0`](https://github.com/jordanbaird/Ice) · [website](https://icemenubar.app)
- **[MonitorControl](https://github.com/MonitorControl/MonitorControl)** 🍎 — Control external display brightness/volume with native OSD. [`MIT`](https://github.com/MonitorControl/MonitorControl) · [website](https://monitorcontrol.app)
- **[PeaZip](https://github.com/giorgiotani/PeaZip)** — Free archiver supporting 200+ formats, with encryption. [`LGPL-3.0`](https://github.com/giorgiotani/PeaZip) · [website](https://peazip.github.io)
- **[LinearMouse](https://github.com/linearmouse/linearmouse)** 🍎 — Per-device mouse/trackpad customization: scroll, speed, buttons. [`MIT`](https://github.com/linearmouse/linearmouse) · [website](https://linearmouse.app)
- **[Finicky](https://github.com/johnste/finicky)** 🍎 — Route URLs to different browsers based on rules you define. [`MIT`](https://github.com/johnste/finicky) · [website](https://github.com/johnste/finicky)
- **[KeyCastr](https://github.com/keycastr/keycastr)** 🍎 — Display keystrokes on screen — great for screencasts and demos. [`BSD-3-Clause`](https://github.com/keycastr/keycastr) · [website](https://github.com/keycastr/keycastr)
- **[Karabiner-Elements](https://github.com/pqrs-org/Karabiner-Elements)** 🍎 — Remap keys, build complex modifications, customize input devices. [`Unlicense`](https://github.com/pqrs-org/Karabiner-Elements) · [website](https://karabiner-elements.pqrs.org/)

## 🎬 Media

Players, editors, converters, and audio/video tooling.

- **[IINA](https://github.com/iina/iina)** 🍎 — Modern native Mac media player built on mpv. [`GPL-3.0`](https://github.com/iina/iina) · [website](https://iina.io)
- **[VLC](https://github.com/videolan/vlc)** — The ubiquitous plays-everything media player. [`GPL-2.0`](https://github.com/videolan/vlc) · [website](https://www.videolan.org/vlc)
- **[mpv](https://github.com/mpv-player/mpv)** — Minimal, scriptable, high-quality media player and library. [`GPL-2.0`](https://github.com/mpv-player/mpv/blob/HEAD/LICENSE.GPL) · [website](https://mpv.io)
- **[HandBrake](https://github.com/HandBrake/HandBrake)** — Convert video between formats, with presets for every device. [`GPL-2.0`](https://github.com/HandBrake/HandBrake/blob/HEAD/LICENSE) · [website](https://handbrake.fr)
- **[OBS Studio](https://github.com/obsproject/obs-studio)** — Free live-streaming and screen-recording studio. [`GPL-2.0`](https://github.com/obsproject/obs-studio) · [website](https://obsproject.com)
- **[Audacity](https://github.com/audacity/audacity)** — Multi-track audio recording and editing. [`GPL-3.0`](https://github.com/audacity/audacity/blob/HEAD/LICENSE.txt) · [website](https://www.audacityteam.org)
- **[LosslessCut](https://github.com/mifi/lossless-cut)** — Losslessly trim video/audio without re-encoding. [`GPL-2.0`](https://github.com/mifi/lossless-cut/blob/HEAD/LICENSE) · [website](https://losslesscut.app/)
- **[BlackHole](https://github.com/ExistentialAudio/BlackHole)** 🍎 — Virtual audio driver to route audio between apps. [`GPL-3.0`](https://github.com/ExistentialAudio/BlackHole/blob/HEAD/LICENSE) · [website](https://existential.audio/blackhole/)
- **[FFmpeg](https://github.com/FFmpeg/FFmpeg)** — Swiss-army knife of audio/video conversion and streaming (CLI). [`LGPL-2.1`](https://github.com/FFmpeg/FFmpeg/blob/HEAD/LICENSE.md) · [website](https://ffmpeg.org)
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — Download video and audio from hundreds of sites (CLI). [`Unlicense`](https://github.com/yt-dlp/yt-dlp) · [website](https://github.com/yt-dlp/yt-dlp)

## 🎨 Design

3D, image editing, CAD, photography, and diagramming.

- **[Blender](https://github.com/blender/blender)** — Full 3D creation suite: modeling, animation, rendering, VFX. [`GPL-2.0`](https://github.com/blender/blender/blob/HEAD/doc/license/GPL-license.txt) · [website](https://www.blender.org)
- **[GIMP](https://github.com/GNOME/gimp)** — GNU Image Manipulation Program — raster graphics editing. [`GPL-3.0`](https://github.com/GNOME/gimp/blob/HEAD/COPYING) · [website](https://www.gimp.org)
- **[LibreCAD](https://github.com/LibreCAD/LibreCAD)** — 2D CAD application for technical drawing. [`GPL-2.0`](https://github.com/LibreCAD/LibreCAD/blob/HEAD/LICENSE) · [website](https://librecad.org/)
- **[Krita](https://github.com/KDE/krita)** — Digital painting studio for illustrators and concept artists. [`GPL-3.0`](https://github.com/KDE/krita) · [website](https://krita.org)
- **[darktable](https://github.com/darktable-org/darktable)** — Photography workflow and RAW developer. [`GPL-3.0`](https://github.com/darktable-org/darktable) · [website](https://www.darktable.org)
- **[RawTherapee](https://github.com/RawTherapee/RawTherapee)** — Cross-platform RAW photo processor. [`GPL-3.0`](https://github.com/RawTherapee/RawTherapee) · [website](https://rawtherapee.com)
- **[draw.io Desktop](https://github.com/jgraph/drawio-desktop)** — Offline diagramming and whiteboarding app. [`GPL-3.0`](https://github.com/jgraph/drawio-desktop) · [website](https://www.diagrams.net)
- **[FreeCAD](https://github.com/FreeCAD/FreeCAD)** — Parametric 3D CAD modeler for product design and engineering. [`LGPL-2.1`](https://github.com/FreeCAD/FreeCAD) · [website](https://www.freecad.org)

## 🔒 Security & Privacy

Password managers, firewalls, and system integrity tools.

- **[Bitwarden](https://github.com/bitwarden/clients)** — Open-source password manager with end-to-end encryption. [`GPL-3.0`](https://github.com/bitwarden/clients/blob/HEAD/LICENSE.txt) · [website](https://bitwarden.com)
- **[KeePassXC](https://github.com/keepassxreboot/keepassxc)** — Offline password manager with strong encryption, no cloud needed. [`GPL-2.0-or-later`](https://github.com/keepassxreboot/keepassxc/blob/HEAD/COPYING) · [website](https://keepassxc.org)
- **[Santa](https://github.com/google/santa)** 🍎 *(maintenance)* — Google's binary allow/denylist system for macOS. [`Apache-2.0`](https://github.com/google/santa) · [website](https://santa.dev)
- **[LuLu](https://github.com/objective-see/LuLu)** 🍎 — Free macOS firewall alerting on unknown outgoing connections. [`GPL-3.0`](https://github.com/objective-see/LuLu) · [website](https://objective-see.org/products/lulu.html)
- **[KnockKnock](https://github.com/objective-see/KnockKnock)** 🍎 — See what persists on your Mac: launch items, extensions, plugins. [`GPL-3.0`](https://github.com/objective-see/KnockKnock) · [website](https://objective-see.org/products/knockknock.html)
- **[BlockBlock](https://github.com/objective-see/BlockBlock)** 🍎 — Monitor persistence locations and block malware persistence. [`GPL-3.0`](https://github.com/objective-see/BlockBlock) · [website](https://objective-see.org/products/blockblock.html)
- **[Wireshark](https://github.com/wireshark/wireshark)** — Network protocol analyzer for deep packet inspection. [`GPL-2.0`](https://github.com/wireshark/wireshark) · [website](https://www.wireshark.org)
- **[WireGuard](https://github.com/WireGuard/wireguard-apple)** 🍎 *(maintenance)* — Fast, modern VPN protocol with an official Apple-platform app. [`MIT`](https://github.com/WireGuard/wireguard-apple) · [website](https://www.wireguard.com)

## 💻 Terminal & System

Terminals, shells, tiling window managers, and CLI power tools.

- **[iTerm2](https://github.com/gnachman/iTerm2)** 🍎 — Feature-rich native Mac terminal with tmux integration and Python API. [`GPL-2.0`](https://github.com/gnachman/iTerm2) · [website](https://iterm2.com/)
- **[Alacritty](https://github.com/alacritty/alacritty)** — GPU-accelerated, minimal terminal emulator. [`Apache-2.0`](https://github.com/alacritty/alacritty) · [website](https://alacritty.org)
- **[Kitty](https://github.com/kovidgoyal/kitty)** — GPU-based terminal with graphics protocol, tabs, extensibility. [`GPL-3.0`](https://github.com/kovidgoyal/kitty) · [website](https://sw.kovidgoyal.net/kitty/)
- **[WezTerm](https://github.com/wezterm/wezterm)** — GPU-accelerated terminal with multiplexing built in. [`MIT`](https://github.com/wezterm/wezterm/blob/HEAD/LICENSE.md) · [website](https://wezterm.org)
- **[Ghostty](https://github.com/ghostty-org/ghostty)** — Fast native-feeling terminal focused on simplicity. [`MIT`](https://github.com/ghostty-org/ghostty) · [website](https://ghostty.org)
- **[Yabai](https://github.com/asmvik/yabai)** 🍎 — Tiling window manager for macOS — scriptable and fast. [`MIT`](https://github.com/asmvik/yabai) · [website](https://github.com/asmvik/yabai)
- **[Amethyst](https://github.com/ianyh/Amethyst)** 🍎 — Automatic tiling window manager with multiple layouts. [`MIT`](https://github.com/ianyh/Amethyst) · [website](https://ianyh.com/amethyst/)
- **[Starship](https://github.com/starship/starship)** — Minimal, fast, customizable shell prompt for any shell. [`ISC`](https://github.com/starship/starship) · [website](https://starship.rs)
- **[fzf](https://github.com/junegunn/fzf)** — Fuzzy finder for the command line: files, history, processes. [`MIT`](https://github.com/junegunn/fzf) · [website](https://junegunn.github.io/fzf/)
- **[ripgrep](https://github.com/BurntSushi/ripgrep)** — Blazing-fast recursive search — a modern grep. [`Unlicense`](https://github.com/BurntSushi/ripgrep) · [website](https://github.com/BurntSushi/ripgrep)
- **[lazygit](https://github.com/jesseduffield/lazygit)** — Terminal UI for Git with keyboard-driven workflows. [`MIT`](https://github.com/jesseduffield/lazygit) · [website](https://github.com/jesseduffield/lazygit)
- **[tmux](https://github.com/tmux/tmux)** — Terminal multiplexer: sessions, windows, panes that survive disconnects. [`ISC`](https://github.com/tmux/tmux) · [website](https://github.com/tmux/tmux)

## 📝 Notes & Knowledge

Note-taking, PKM, and outliners.

- **[Logseq](https://github.com/logseq/logseq)** — Privacy-first, local-first outliner and knowledge graph. [`AGPL-3.0`](https://github.com/logseq/logseq) · [website](https://logseq.com)
- **[Joplin](https://github.com/laurent22/joplin)** — Markdown notes with end-to-end encrypted sync across devices. [`AGPL-3.0`](https://github.com/laurent22/joplin/blob/HEAD/LICENSE) · [website](https://joplinapp.org)
- **[Standard Notes](https://github.com/standardnotes/app)** — Encrypted, long-lived notes app. [`AGPL-3.0`](https://github.com/standardnotes/app) · [website](https://standardnotes.com)
- **[Trilium Notes](https://github.com/TriliumNext/Trilium)** — Hierarchical notes with scripting and self-hosted sync. [`AGPL-3.0`](https://github.com/TriliumNext/Trilium) · [website](https://github.com/TriliumNext/Trilium)
- **[SiYuan](https://github.com/siyuan-note/siyuan)** — Local-first personal knowledge base with block editing. [`AGPL-3.0`](https://github.com/siyuan-note/siyuan) · [website](https://b3log.org/siyuan)
- **[AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)** — Open-source Notion alternative: notes, wikis, projects. [`AGPL-3.0`](https://github.com/AppFlowy-IO/AppFlowy) · [website](https://appflowy.com)

## 💬 Communication

Chat, email, and messaging clients.

- **[Element](https://github.com/element-hq/element-desktop)** *(maintenance)* — Matrix chat client with E2E encryption and bridging. [`AGPL-3.0`](https://github.com/element-hq/element-desktop) · [website](https://element.io)
- **[Signal](https://github.com/signalapp/Signal-Desktop)** — Private messenger with E2E encryption by default. [`AGPL-3.0`](https://github.com/signalapp/Signal-Desktop) · [website](https://signal.org/download)
- **[Telegram Desktop](https://github.com/telegramdesktop/tdesktop)** — Fast multi-device messenger with channels and bots. [`GPL-3.0`](https://github.com/telegramdesktop/tdesktop) · [website](https://desktop.telegram.org/)
- **[Zulip](https://github.com/zulip/zulip-desktop)** — Threaded team chat for organized async conversation. [`Apache-2.0`](https://github.com/zulip/zulip-desktop) · [website](https://zulip.com/apps)
- **[Mailspring](https://github.com/Foundry376/Mailspring)** — Fast, extensible email client with unified inbox. [`GPL-3.0`](https://github.com/Foundry376/Mailspring) · [website](https://getmailspring.com/)
- **[Session](https://github.com/oxen-io/session-desktop)** *(maintenance)* — Decentralized private messenger; onion routing, no phone number. [`GPL-3.0`](https://github.com/oxen-io/session-desktop) · [website](https://getsession.org)

## 🌐 Browsers

Web browsers for every philosophy.

- **[Firefox](https://github.com/mozilla-firefox/firefox)** — Mozilla's independent Gecko-based browser. [`MPL-2.0`](https://github.com/mozilla-firefox/firefox/blob/HEAD/LICENSE) · [website](https://www.firefox.com)
- **[Chromium](https://github.com/chromium/chromium)** — Open-source base of Chrome, without Google branding. [`BSD-3-Clause`](https://github.com/chromium/chromium) · [website](https://www.chromium.org/Home)
- **[Ungoogled Chromium](https://github.com/ungoogled-software/ungoogled-chromium)** — Chromium stripped of Google integration and tracking. [`BSD-3-Clause`](https://github.com/ungoogled-software/ungoogled-chromium) · [website](https://github.com/ungoogled-software/ungoogled-chromium)
- **[Brave](https://github.com/brave/brave-browser)** — Chromium-based browser with built-in ad blocking. [`MPL-2.0`](https://github.com/brave/brave-browser) · [website](https://brave.com)
- **[Zen Browser](https://github.com/zen-browser/desktop)** — Firefox-based browser with a modern, customizable UI. [`MPL-2.0`](https://github.com/zen-browser/desktop) · [website](https://zen-browser.app)
- **[qutebrowser](https://github.com/qutebrowser/qutebrowser)** — Keyboard-driven, Vim-like minimal browser. [`GPL-3.0`](https://github.com/qutebrowser/qutebrowser) · [website](https://www.qutebrowser.org/)

## Notable exclusions

Popular Mac apps deliberately left out because they are not open source, even though they are free or beloved:

- **Raycast, Alfred, Bartender, Magnet, CleanShot X, Shottr, BetterTouchTool, AppCleaner, OnyX** — proprietary freeware.
- **1Password, Obsidian, Notion, Warp, Arc, Vivaldi, Little Snitch** — proprietary.
- **Keka** — closed-source since 1.0, per its own README.
- **Mos** — license changed to CC BY-NC 4.0 (non-commercial, not open source).
- **Mac Mouse Fix** — custom license forbidding charging for derived programs (non-commercial).
- **Pearcleaner** — Apache-2.0 plus Commons Clause (source-available, not OSI open source).
- **Anytype** — Any Source Available License 1.0 (source-available, not OSI open source).
- **eqMac** — original project went proprietary (eqMac Pro); only stale forks remain.

## Documentation

- [Choosing an OSS macOS app](docs/choosing-an-oss-macos-app.md)
- [macOS native vs Electron](docs/macos-native-vs-electron.md)
- [Licenses explained](docs/licenses-explained.md)
- [Glossary](docs/glossary.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New entries must be open-source licensed, buildable/runnable on macOS, and verifiable via a public Git repository.

## License

This list is MIT licensed — see [LICENSE](LICENSE).
