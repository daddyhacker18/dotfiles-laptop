from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"],
          ["#474747", "#474747"],
          ]

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background=colors[0], foreground=colors[2]),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background=colors[0], mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background=colors[0], foreground=colors[2]),
                widget.GroupBox(
                                font = "TerminessTTF Nerd Font",
                                fontsize = 18,
                                margin_y = 3,
                                margin_x = 0,
                                padding_y = 5,
                                padding_x = 3,
                                borderwidth = 3,
                                active = colors[2],
                                inactive = colors[7],
                                rounded = True,
                                highlight_color = colors[1],
                                highlight_method = "line",
                                this_current_screen_border = colors[8],
                                this_screen_border = colors [6],
                                other_current_screen_border = colors[8],
                                other_screen_border = colors[6],
                                foreground = colors[2],
                                background = colors[0]
                                ),
                widget.TextBox(
                    text = '|',
                    font = "TerminessTTF Nerd Font Bold",
                    background = colors[0],
                    foreground = colors[10],
                    padding = 2,
                    fontsize=18
                    ),
                widget.Prompt(),
                widget.Spacer(background=colors[0],length=5),
                widget.WindowName(
                    font="TerminessTTF Nerd Font Bold",
                    fontsize=18,
                    foreground=colors[6],
                    background=colors[0],
                    padding=0,
                    fmt='{}'
                    ),
                widget.Clock(
                    foreground = colors[2],
                    font="TerminessTTF Nerd Font Bold",
                    fontsize=18,
                    background = colors[0],
                    padding = 0,
                    format = "%A %d %B %H:%M "
                ),
                widget.Spacer(background=colors[0],length=bar.STRETCH),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CheckUpdates(
                    update_interval=1800,
                    fontsize=18,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground=colors[1],
                    background=colors[0],
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    },
                    ),
                widget.Systray(
                    icon_size = 20,
                    background=colors[0],
                    ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=colors[0],
                       background=colors[0]
                       ),
                widget.Load(
                    format = "{load:.2f}",
                    background = colors[0],
                    font="TerminessTTF Nerd Font Bold",
                    fmt = "loa: {}",
                    fontsize=18,
                    foreground=colors[4],
                    padding=5,
                ),
                widget.ThermalSensor(
                    foreground = colors[4],
                    background = colors[0],
                    font="TerminessTTF Nerd Font Bold",
                    fontsize=18,
                    threshold = 90,
                    fmt = 'tmp: {}',
                    padding = 5,
                ),
                widget.Memory(
                    foreground = colors[4],
                    background = colors[0],
                    font="TerminessTTF Nerd Font Bold",
                    fontsize=18,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e glances')},
                    measure_mem = "G",
                    format = "{MemUsed:.1f}G/{MemTotal:.1f}G",
                    fmt ="mem: {}",
                    padding = 5,
                ),
                widget.DF(
                    foreground = colors[4],
                    background = colors[0],
                    fontsize=18,
                    font="TerminessTTF Nerd Font Bold",
                    padding = 5,
                    visible_on_warn = False,
                    format = "{uf}{m}",
                    fmt = "dsk: {}",
                ),
                widget.Battery(
                    format = "{char}{percent:2.0%}",
                    fmt = "bat: {}",
                    background = colors[0],
                    foreground = colors[4],
                    padding = 2,
                    fontsize=18,
                    font="TerminessTTF Nerd Font Bold",
                ),
                widget.TextBox(
                    text = ' | ',
                    font = "TerminessTTF Nerd Font Bold",
                    background = colors[0],
                    foreground = colors[10],
                    padding = 2,
                    fontsize=18
                    ),
                widget.Prompt(),
                widget.Spacer(background=colors[0],length=5),
                volume,
                widget.CurrentLayoutIcon(
                    scale=0.75,
                    background=colors[0],
                    foreground=colors[7]
                    ),
                widget.TextBox(
                    text='',
                    fontsize=18,
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground=colors[3],
                    background=colors[0]
                ),
                widget.Spacer(background=colors[0],length=10)

            ],
            30,  # height in px
            background=colors[0]  # background color
        ), ),
]
