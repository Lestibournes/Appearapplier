# Appearapplier
Applies Nitrogen background and themes to system and user settings.

Nitrogen doesn't apply it's background setting to the system, so the display manager isn't aware of what the user's background is. Also, if there are other desktop environments, nitrogen won't change their wallpaper.

Similarly, LXAppearance doesn't apply the gtk, icon, and cursor themes everywhere where they matter.

This script will modify the GNOME and display manager backgrounds for the current user to follow the Nitrogen background image, and it will modify GNOME GSettings, ~/.Xresources, the user's default icon theme, and the gtk2 themes to match the setting of gtk3.

Run in the background:
nitroplier -d
themeplier -d

Run once:
nitroplier
themeplier

Requires the python modules:
xdg, watchdog, glib, gio, and for nitroplier also pydbus.