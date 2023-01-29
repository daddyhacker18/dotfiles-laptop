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
          ["#a9a1e1", "#a9a1e1"]]

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background=colors[0], foreground=colors[2]),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background=colors[0], mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background=colors[0], foreground=colors[2]),
                widget.GroupBox(
                                font = "TerminessTTF Nerd Font",
                                # fmt = "bold",
                                fontsize = 15,
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
                    foreground = '474747',
                    padding = 2,
                    fontsize = 14
                    #   text = '',
                     #  padding = 0,
                      # fontsize = 28,
                       #foreground='#2f343f'
                       ),
                widget.Prompt(),
                widget.Spacer(background=colors[0],length=5),
                widget.WindowName(
                    foreground=colors[6],
                    background=colors[0],
                    padding=0,
                    fmt='{}'
                    ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(
                    scale=0.75,
                    background=colors[0],
                    foreground=colors[7]
                    ),
                widget.CheckUpdates(
                    update_interval=1800,
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
                    background=colors[0]
                    ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=colors[0],
                       background=colors[0]
                       ),
                volume,
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=colors[0],
                       background=colors[0]
                       ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=colors[0],
                       background=colors[0]
                       ),
                 widget.Clock(
                          foreground = colors[6],
                          background = colors[0],
                          padding = 0,
                          format = "%A %d %B %H:%M ",
                           ),
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground=colors[7],
                    background=colors[0]
                ),
                widget.Spacer(background=colors[0],length=10)

            ],
            30,  # height in px
            background=colors[0]  # background color
        ), ),
]
