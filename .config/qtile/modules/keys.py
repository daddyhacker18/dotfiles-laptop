from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "kitty"
filemanager = "thunar"
browser = "brave"

keys = [
    # window controls
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), lazy.layout.section_down(), desc="Move windows down in current stack"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), lazy.layout.section_up(), desc="Move windows up in current stack"),
    Key([mod], "h", lazy.layout.shrink(), lazy.layout.decrease_nmaster(), desc="Shrink window (MonadTall), decrease number in master pane (Tile)"),
    Key([mod], "l", lazy.layout.grow(), lazy.layout.increase_nmaster(), desc="Expand window (MonadTall), increase number in master pane (Tile)"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # media bindings
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),

    # launchers
    Key([mod], "r", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
    Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # applications
    Key([mod], "F12", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "F1", lazy.spawn(browser), desc="Launches web browser"),
    Key([mod], "F2", lazy.spawn(filemanager), desc="Launches File Manager"),

    # system bindings
    Key([mod], "F10", lazy.spawn("xscreensaver-command -lock"), desc="Locks screen"),
    Key([mod], "F11", lazy.spawn("clipmenu"), desc="Show clipboard history"),
    Key([mod, "shift"], "F10", lazy.spawn("~/.config/rofi/powermenu.sh"), desc="Suspends system"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Monitors
    Key([mod], "w", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    Key([mod], "e", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),

]
