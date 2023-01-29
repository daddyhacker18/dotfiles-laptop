#!/bin/sh

# set up Monitors
~/.screenlayout/main.sh

# wallpapers and screensavers
feh --bg-scale /usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png
xscreensaver --no-splash & disown

# system daemons
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed
~/.config/qtile/scripts/check_battery.sh & disown # Low battery notifier
eos-welcome & disown # Start welcome
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
tresorit-daemon & disown
clipmenud & disown
