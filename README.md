# Awesome OSS macOS [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated directory of **genuinely open-source macOS apps and utilities** — window managers, terminals, media tools, security utilities, dev tools and more — as of **September 2026**.

"Open source" here means the source is publicly available under a recognized open-source license (MIT, Apache-2.0, GPL, BSD, MPL, …). Proprietary freeware — however good — is deliberately out of scope: no Raycast, Alfred, Bartender, CleanMyMac, iStat Menus, Shottr, AppCleaner, OrbStack, Warp, or Arc.

**Verification confidence:** every entry is stamped ✅ **verified** (facts confirmed on the project's official GitHub repo page or official site) or ⚠️ **unverified** (something could not be confirmed — the entry says what). **Numbers are never guessed** — star counts are snapshots from the verification pass and Apple Silicon notes are omitted when unknown. Machine-readable records live in [`data/macos.json`](data/macos.json) with a `verified` boolean per entry. **93 of 93 entries verified** (0 flagged unverified with reasons) — all checks 2026-09-30.

## 2026 Highlights

- **Tiling on the Mac keeps maturing:** AeroSpace, yabai, Amethyst and Rectangle cover everything from i3-style tiling to simple keyboard snapping. Note yabai needs SIP partially disabled — decide if that trade-off is worth it for you.
- **Objective-See's free security suite** (LuLu firewall, KnockKnock, BlockBlock, RansomWhere, TaskExplorer) remains the open baseline for Mac security tooling.
- **Terminal choice is now about config language:** iTerm2 is the veteran; Alacritty, Kitty, Ghostty and WezTerm are GPU-accelerated and configured in files, not preference panes.
- **Homebrew is still the default package manager**; MacPorts is the older, more BSD-flavored alternative. Don't run both.
- **Apple Silicon-native builds are the norm** for maintained projects — entries note universal/ARM64 status where the project states it; Intel-only builds still run under Rosetta 2.

## Contents

- [Window managers & tiling](#window-managers-tiling)
- [Launchers](#launchers)
- [Clipboard managers](#clipboard-managers)
- [Screenshot & recording](#screenshot-recording)
- [Terminal emulators](#terminal-emulators)
- [Editors & IDEs](#editors-ides)
- [Developer tools](#developer-tools)
- [Package managers & automation](#package-managers-automation)
- [Media players](#media-players)
- [Video & image tools](#video-image-tools)
- [Audio tools](#audio-tools)
- [Streaming & capture](#streaming-capture)
- [System utilities](#system-utilities)
- [Menu bar tools](#menu-bar-tools)
- [Backup & sync](#backup-sync)
- [Security](#security)
- [Productivity](#productivity)
- [Accessibility](#accessibility)
- [Browsers](#browsers)
- [Miscellaneous](#miscellaneous)
- [Guides](#guides)
- [Related repositories](#related-repositories)
- [Contributing](#contributing)
- [License](#license)

---

## Window managers & tiling

- [AeroSpace](https://github.com/nikitabobko/AeroSpace) — ✅ verified. i3-like tiling window manager for macOS. License: `MIT`. ★ ~23.3k. [Official site](https://nikitabobko.github.io/AeroSpace/guide)
- [AltTab](https://github.com/lwouis/alt-tab-macos) — ✅ verified. Windows-style alt-tab window switcher for macOS. License: `GPL-3.0-only`. ★ ~16.3k. [Official site](https://alt-tab.app)
- [Amethyst](https://github.com/ianyh/Amethyst) — ✅ verified. Automatic tiling window manager for macOS in the spirit of xmonad. License: `MIT`. ★ ~16.3k. [Official site](https://ianyh.com/amethyst/)
- [Loop](https://github.com/MrKai77/Loop) — ✅ verified. Elegant window management via a radial menu under your cursor. License: `GPL-3.0-only`. ★ ~11.7k.
- [Rectangle](https://github.com/rxhanson/Rectangle) — ✅ verified. Move and resize windows on macOS with keyboard shortcuts and snap areas. License: `MIT`. ★ ~30k. [Official site](https://rectangleapp.com)
- [yabai](https://github.com/koekeishiya/yabai) — ✅ verified. Tiling window manager for macOS based on binary space partitioning. License: `MIT`. ★ ~29.7k.

## Launchers

- [Cerebro](https://github.com/cerebroapp/cerebro) — ✅ verified. Open-source launcher to improve productivity and efficiency. License: `MIT`. ★ ~8.6k. [Official site](https://www.cerebroapp.com/)
- [Zazu](https://github.com/tinytacoteam/zazu) — ✅ verified. Fully extensible open-source launcher for hackers and creators. (Repository archived; last updated 2019.). License: `MIT`. ★ ~2.1k. [Official site](http://zazuapp.org)

## Clipboard managers

- [CopyQ](https://github.com/hluk/copyq) — ✅ verified. Clipboard manager with advanced features. License: `GPL-3.0-only`. ★ ~12.3k.
- [Maccy](https://github.com/p0deje/Maccy) — ✅ verified. Lightweight clipboard manager for macOS. License: `MIT`. ★ ~21.8k. [Official site](https://maccy.app)

## Screenshot & recording

- [Flameshot](https://github.com/flameshot-org/flameshot) — ✅ verified. Powerful yet simple screenshot software with annotation tools. License: `GPL-3.0-only`. ★ ~31k. [Official site](https://flameshot.org)
- [Kap](https://github.com/wulkano/Kap) — ✅ verified. Open-source screen recorder built with web technology. License: `MIT`. ★ ~19.4k. [Official site](https://getkap.co)
- [ksnip](https://github.com/ksnip/ksnip) — ✅ verified. Cross-platform screenshot and annotation tool. License: `GPL-3.0-only`. ★ ~3.3k.

## Terminal emulators

- [Alacritty](https://github.com/alacritty/alacritty) — ✅ verified. Cross-platform, OpenGL terminal emulator. License: `Apache-2.0`. ★ ~65.9k. [Official site](https://alacritty.org)
- [Ghostty](https://github.com/ghostty-org/ghostty) — ✅ verified. Fast, feature-rich, GPU-accelerated terminal emulator with native UI. License: `MIT`. ★ ~61.7k. [Official site](https://ghostty.org)
- [iTerm2](https://github.com/gnachman/iTerm2) — ✅ verified. Feature-rich terminal emulator for macOS. License: `GPL-2.0-only`. ★ ~18.1k. [Official site](https://iterm2.com/)
- [kitty](https://github.com/kovidgoyal/kitty) — ✅ verified. Fast, feature-rich, GPU-based terminal emulator. License: `GPL-3.0-only`. ★ ~35.1k. [Official site](https://sw.kovidgoyal.net/kitty/)
- [Tabby](https://github.com/Eugeny/tabby) — ✅ verified. Modern, highly customizable terminal for the modern age. License: `MIT`. ★ ~74.8k. [Official site](https://tabby.sh)
- [WezTerm](https://github.com/wez/wezterm) — ✅ verified. GPU-accelerated cross-platform terminal emulator and multiplexer written in Rust. License: `MIT`. ★ ~29.1k. [Official site](https://wezterm.org/)

## Editors & IDEs

- [CotEditor](https://github.com/coteditor/CotEditor) — ✅ verified. Lightweight plain-text editor for macOS. (Source code Apache-2.0; bundled image resources CC BY-NC-ND 4.0.). License: `Apache-2.0`. ★ ~8.5k. [Official site](https://coteditor.com)
- [MacVim](https://github.com/macvim-dev/macvim) — ✅ verified. Vim, the text editor, as a native macOS app. License: `Vim`. ★ ~7.9k. [Official site](https://macvim.org)
- [TextMate](https://github.com/textmate/textmate) — ✅ verified. Graphical text editor for macOS. License: `GPL-3.0-only`. ★ ~14.6k. [Official site](https://macromates.com/)
- [Visual Studio Code](https://github.com/microsoft/vscode) — ✅ verified. Extensible, open-source code editor. (Microsoft's official branded builds add proprietary components.). License: `MIT`. ★ ~193.3k. [Official site](https://code.visualstudio.com)
- [Zed](https://github.com/zed-industries/zed) — ✅ verified. High-performance, multiplayer code editor from the creators of Atom and Tree-sitter. License: `GPL-3.0-or-later`. ★ ~91.1k. [Official site](https://zed.dev)

## Developer tools

- [Boop](https://github.com/IvanMathy/Boop) — ✅ verified. Scriptable scratchpad for developers. License: `MIT`. ★ ~4.2k. [Official site](https://boop.okat.best)
- [Bruno](https://github.com/usebruno/bruno) — ✅ verified. Open-source IDE for exploring and testing APIs; lightweight Postman/Insomnia alternative. License: `MIT`. ★ ~47.3k. [Official site](https://www.usebruno.com/)
- [GitUp](https://github.com/git-up/GitUp) — ✅ verified. Fast, visual Git client for macOS. License: `GPL-3.0-only`. ★ ~12.1k. [Official site](http://gitup.co)
- [Platypus](https://github.com/sveinbjornt/Platypus) — ✅ verified. Create native macOS applications from command-line scripts. License: `BSD-3-Clause`. ★ ~3.5k. [Official site](https://sveinbjorn.org/platypus)
- [Sequel Ace](https://github.com/Sequel-Ace/Sequel-Ace) — ✅ verified. MySQL/MariaDB database management for macOS. License: `MIT`. ★ ~7.5k. [Official site](https://sequel-ace.com)
- [Sparkle](https://github.com/sparkle-project/Sparkle) — ✅ verified. Software update framework for macOS apps. License: `MIT`. ★ ~9.8k. [Official site](https://sparkle-project.org)

## Package managers & automation

- [Homebrew](https://github.com/Homebrew/brew) — ✅ verified. The package manager for macOS (and Linux). License: `BSD-2-Clause`. ★ ~49.8k. [Official site](https://brew.sh)
- [MacPorts](https://github.com/macports/macports-base) — ✅ verified. Package manager providing a large collection of open-source ports for macOS. License: `BSD-3-Clause`. ★ ~1k. [Official site](https://trac.macports.org)
- [mas](https://github.com/mas-cli/mas) — ✅ verified. Mac App Store command-line interface. License: `MIT`. ★ ~12.4k.
- [nix-darwin](https://github.com/LnL7/nix-darwin) — ✅ verified. Manage your macOS system configuration using Nix. License: `MIT`. ★ ~6k. [Official site](https://nix-darwin.org)

## Media players

- [IINA](https://github.com/iina/iina) — ✅ verified. Modern video player for macOS built on mpv. License: `GPL-3.0-only`. ★ ~46.5k. [Official site](https://iina.io)
- [mpv](https://github.com/mpv-player/mpv) — ✅ verified. Minimal, scriptable command-line media player. License: `GPL-2.0-or-later`. ★ ~37.2k. [Official site](https://mpv.io)
- [VLC](https://github.com/videolan/vlc) — ✅ verified. Free media player that plays almost everything. License: `GPL-2.0-only`. ★ ~19.8k. [Official site](http://www.videolan.org/vlc)

## Video & image tools

- [Audacity](https://github.com/audacity/audacity) — ✅ verified. Free, open-source audio editor and recorder. License: `GPL-3.0-only`. ★ ~18.6k. [Official site](https://wiki.audacityteam.org/wiki/For_Developers)
- [Gifski](https://github.com/sindresorhus/Gifski) — ✅ verified. Convert videos to high-quality GIFs on your Mac. License: `MIT`. ★ ~8.6k. [Official site](https://sindresorhus.com/gifski)
- [HandBrake](https://github.com/HandBrake/HandBrake) — ✅ verified. Open-source video transcoder. License: `GPL-2.0-only`. ★ ~24.5k. [Official site](https://handbrake.fr)
- [LosslessCut](https://github.com/mifi/lossless-cut) — ✅ verified. Swiss army knife of lossless video and audio editing. License: `GPL-2.0-only`. ★ ~44.2k. [Official site](https://losslesscut.app/)
- [Picard](https://github.com/metabrainz/picard) — ✅ verified. Cross-platform music tagger powered by the MusicBrainz database. License: `GPL-2.0-only`. ★ ~5.2k. [Official site](https://picard.musicbrainz.org)
- [Shotcut](https://github.com/mltframework/shotcut) — ✅ verified. Cross-platform, open-source video editor. License: `GPL-3.0-only`. ★ ~15.3k. [Official site](https://www.shotcut.org)
- [Subler](https://github.com/sublerapp/subler) — ✅ verified. MP4 muxer and metadata editor for macOS. License: `GPL-2.0-only`. ★ ~250. [Official site](https://subler.org)

## Audio tools

- [Background Music](https://github.com/kyleneideck/BackgroundMusic) — ✅ verified. macOS audio utility: per-app volumes, auto-pause, and system-audio recording. License: `GPL-2.0-only`. ★ ~19.3k.
- [BlackHole](https://github.com/ExistentialAudio/BlackHole) — ✅ verified. Modern macOS virtual audio loopback driver with zero additional latency. (Source GPL-3.0; official compiled binaries and branding carry separate restrictions.). License: `GPL-3.0-only`. ★ ~19.8k.
- [eqMac](https://github.com/bitgapp/eqMac) — ✅ verified. System-wide audio equalizer and volume mixer for macOS. (Only the older free codebase is public; newer releases use a private fork.). License: `Apache-2.0`. ★ ~6.8k. [Official site](https://eqmac.app)
- [SwitchAudioSource](https://github.com/deweller/switchaudio-osx) — ✅ verified. Change the macOS audio source from the command line. License: `MIT`. ★ ~1.4k.

## Streaming & capture

- [OBS Studio](https://github.com/obsproject/obs-studio) — ✅ verified. Free and open-source software for live streaming and screen recording. License: `GPL-2.0-only`. ★ ~76.8k. [Official site](https://obsproject.com)

## System utilities

- [Hammerspoon](https://github.com/Hammerspoon/hammerspoon) — ✅ verified. Staggeringly powerful macOS desktop automation with Lua. License: `MIT`. ★ ~16.2k. [Official site](http://www.hammerspoon.org)
- [KeepingYouAwake](https://github.com/newmarcel/KeepingYouAwake) — ✅ verified. Menu-bar utility that prevents your Mac from going to sleep. License: `MIT`. ★ ~6.9k. [Official site](https://keepingyouawake.app)
- [MonitorControl](https://github.com/MonitorControl/MonitorControl) — ✅ verified. Control external display brightness and volume as if it were a native Apple display. License: `MIT`. ★ ~34.4k. [Official site](https://monitorcontrol.app)
- [OpenInTerminal](https://github.com/Ji4n1ng/OpenInTerminal) — ✅ verified. Finder toolbar app to open the current directory in Terminal, iTerm, or Alacritty. License: `MIT`. ★ ~7k.

## Menu bar tools

- [Hidden Bar](https://github.com/dwarvesf/hidden) — ✅ verified. Ultra-light utility that hides menu-bar icons. License: `MIT`. ★ ~15k. [Official site](https://d.foundation/opensource)
- [Ice](https://github.com/jordanbaird/Ice) — ✅ verified. Powerful menu-bar manager for macOS. License: `GPL-3.0-only`. ★ ~29.7k. [Official site](https://icemenubar.app)
- [Itsycal](https://github.com/sfsam/Itsycal) — ✅ verified. Tiny calendar for your Mac's menu bar. License: `MIT`. ★ ~4k.
- [MeetingBar](https://github.com/leits/MeetingBar) — ✅ verified. Your meetings at your fingertips in the macOS menu bar. License: `Apache-2.0`. ★ ~5.4k. [Official site](https://meetingbar.app)
- [Stats](https://github.com/exelban/stats) — ✅ verified. macOS system monitor in your menu bar. License: `MIT`. ★ ~42.2k. [Official site](https://mac-stats.com)
- [SwiftBar](https://github.com/swiftbar/SwiftBar) — ✅ verified. Powerful macOS menu-bar customization tool. License: `MIT`. ★ ~4.6k. [Official site](https://swiftbar.app)

## Backup & sync

- [Duplicati](https://github.com/duplicati/duplicati) — ✅ verified. Store securely encrypted backups in the cloud. License: `MIT`. ★ ~15k.
- [Mackup](https://github.com/lra/mackup) — ✅ verified. Backup and keep your application settings in sync. License: `GPL-3.0-only`. ★ ~15.3k.
- [rclone](https://github.com/rclone/rclone) — ✅ verified. "rsync for cloud storage": sync files with S3, Google Drive, Dropbox, and dozens more. License: `MIT`. ★ ~60k. [Official site](https://rclone.org)
- [Syncthing](https://github.com/syncthing/syncthing) — ✅ verified. Open-source continuous file synchronization. License: `MPL-2.0`. ★ ~89k. [Official site](https://syncthing.net/)

## Security

- [Bitwarden](https://github.com/bitwarden/clients) — ✅ verified. Open-source password manager clients (desktop, web, browser, CLI). (Core clients GPL-3.0; some directories under the separate Bitwarden License.). License: `GPL-3.0-only`. ★ ~13.9k. [Official site](https://bitwarden.com)
- [BlockBlock](https://github.com/objective-see/BlockBlock) — ✅ verified. Monitors persistence locations to block malware persistence. License: `GPL-3.0-only`. ★ ~852.
- [KnockKnock](https://github.com/objective-see/KnockKnock) — ✅ verified. See what's persistently installed on your Mac, like AutoRuns but for macOS. License: `GPL-3.0-only`. ★ ~800. [Official site](https://objective-see.org/products/knockknock.html)
- [LuLu](https://github.com/objective-see/LuLu) — ✅ verified. Free, open-source macOS firewall by Objective-See. License: `GPL-3.0-only`. ★ ~13.3k. [Official site](https://objective-see.org/products/lulu.html)
- [MacPass](https://github.com/mstarke/MacPass) — ✅ verified. Native macOS KeePass-compatible password manager. License: `GPL-3.0-or-later`. ★ ~6.9k. [Official site](http://macpass.app/)
- [OverSight](https://github.com/objective-see/OverSight) — ✅ verified. Monitors your Mac's mic and webcam, alerting you when they are accessed. License: `GPL-3.0-only`. ★ ~680.
- [Santa](https://github.com/google/santa) — ✅ verified. Binary authorization and monitoring system for macOS. (Archived by Google in 2025.). License: `Apache-2.0`. ★ ~4.5k. [Official site](https://santa.dev)

## Productivity

- [Joplin](https://github.com/laurent22/joplin) — ✅ verified. Privacy-focused note-taking app with sync across desktop and mobile. License: `AGPL-3.0-or-later`. ★ ~56.5k. [Official site](https://joplinapp.org)
- [Logseq](https://github.com/logseq/logseq) — ✅ verified. Privacy-first, open-source platform for knowledge management. License: `AGPL-3.0-only`. ★ ~45.1k. [Official site](https://logseq.com)
- [Standard Notes](https://github.com/standardnotes/app) — ✅ verified. End-to-end encrypted notes app. License: `AGPL-3.0-only`. ★ ~6.6k. [Official site](https://standardnotes.com)
- [Stretchly](https://github.com/hovancik/stretchly) — ✅ verified. Break-time reminder app. License: `BSD-2-Clause`. ★ ~6.6k. [Official site](https://hovancik.net/stretchly)
- [Super Productivity](https://github.com/johannesjo/super-productivity) — ✅ verified. Advanced todo list with timeboxing, time tracking, and Jira/GitHub integrations. License: `MIT`. ★ ~22.4k. [Official site](http://super-productivity.com?ref=github)
- [Zettlr](https://github.com/Zettlr/Zettlr) — ✅ verified. One-stop publication workbench for writers and researchers. License: `GPL-3.0-only`. ★ ~13.6k. [Official site](https://www.zettlr.com)

## Accessibility

- [Karabiner-Elements](https://github.com/pqrs-org/Karabiner-Elements) — ✅ verified. Powerful keyboard customization for macOS. License: `Unlicense`. ★ ~22.9k. [Official site](https://karabiner-elements.pqrs.org/)
- [KeyCastr](https://github.com/keycastr/keycastr) — ✅ verified. Open-source keystroke visualizer for macOS. License: `BSD-3-Clause`. ★ ~15.1k.
- [LinearMouse](https://github.com/linearmouse/linearmouse) — ✅ verified. Mouse and trackpad utility for Mac: per-device scrolling, acceleration, and buttons. License: `MIT`. ★ ~6.9k. [Official site](https://linearmouse.app)
- [Scroll Reverser](https://github.com/pilotmoon/Scroll-Reverser) — ✅ verified. Reverse scroll direction independently per device (mouse vs. trackpad). License: `Apache-2.0`. ★ ~3.6k. [Official site](https://pilotmoon.com/scrollreverser/)

## Browsers

- [Brave](https://github.com/brave/brave-browser) — ✅ verified. Privacy-focused browser with built-in ad blocking. License: `MPL-2.0`. ★ ~23.8k. [Official site](https://brave.com)
- [Chromium](https://github.com/chromium/chromium) — ✅ verified. Open-source browser project behind Chrome, Edge, Brave, and others. License: `BSD-3-Clause`. ★ ~24.9k. [Official site](https://chromium.googlesource.com/chromium/src/)
- [Firefox](https://github.com/mozilla-firefox/firefox) — ✅ verified. Mozilla's official open-source web browser. License: `MPL-2.0`. ★ ~13.3k. [Official site](https://www.firefox.com/)
- [Floorp](https://github.com/Floorp-Projects/Floorp) — ✅ verified. Advanced, customizable Firefox derivative. License: `MPL-2.0`. ★ ~8.4k. [Official site](https://floorp.app)
- [Min](https://github.com/minbrowser/min) — ✅ verified. Fast, minimal browser that protects your privacy. License: `Apache-2.0`. ★ ~9.2k. [Official site](https://minbrowser.org/)
- [qutebrowser](https://github.com/qutebrowser/qutebrowser) — ✅ verified. Keyboard-driven, vim-like browser based on Python and Qt. License: `GPL-3.0-only`. ★ ~11.7k. [Official site](https://www.qutebrowser.org/)
- [Zen Browser](https://github.com/zen-browser/desktop) — ✅ verified. Firefox-based browser aiming for a calmer internet. License: `MPL-2.0`. ★ ~44.7k. [Official site](https://zen-browser.app)

## Miscellaneous

- [AltStore](https://github.com/rileytestut/AltStore) — ✅ verified. Alternative app store for non-jailbroken iOS devices. License: `AGPL-3.0-only`. ★ ~14.5k. [Official site](https://altstore.io)
- [Heroic Games Launcher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher) — ✅ verified. Games launcher for GOG, Amazon, and Epic Games on Linux, Windows, and macOS. License: `GPL-3.0-only`. ★ ~12.3k. [Official site](https://heroicgameslauncher.com)
- [Latest](https://github.com/mangerlahn/Latest) — ✅ verified. Small utility that notifies you about updates to the apps you use. License: `GPL-3.0-only`. ★ ~4.8k. [Official site](https://max.codes/latest)
- [OpenMTP](https://github.com/ganeshrvel/openMTP) — ✅ verified. Advanced Android file-transfer application for macOS. License: `MIT`. ★ ~7.4k. [Official site](https://openmtp.ganeshrvel.com)
- [SwiftDefaultApps](https://github.com/Lord-Kamina/SwiftDefaultApps) — ✅ verified. Modern replacement for RCDefaultApp: manage default apps and file associations via a preference pane. License: `Beerware`. ★ ~1.7k.
- [Whisky](https://github.com/Whisky-App/Whisky) — ✅ verified. Modern Wine wrapper for macOS built with SwiftUI. (Archived; development discontinued in 2025.). License: `GPL-3.0-only`. ★ ~15.1k. [Official site](https://getwhisky.app)

## Guides

- [Choosing an open-source macOS app](docs/choosing-an-oss-macos-app.md) — what "open" covers, matching tools to jobs, Apple Silicon notes
- [Glossary](docs/glossary.md) — universal binaries, SIP, notarization, Gatekeeper, Homebrew terms, license families
- [Status changes](docs/status-changes.md) — license changes, archival, renames, retirements

## Related repositories

- [awesome](https://github.com/sindresorhus/awesome) — the canonical awesome list
- [Awesome-llms-labs](https://github.com/awesome-llms-labs) — sibling awesome-lists by the same author (LLM-focused)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The honesty policy is the whole point: if the official page is ambiguous, the entry says so.

## License

This list is [MIT](LICENSE) © 2026 Aaron Cross. The listed projects keep their own licenses — check each entry's `license` field.
