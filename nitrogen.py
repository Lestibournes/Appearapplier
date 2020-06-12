import os
from xdg import BaseDirectory
from gi.repository import GLib, Gio

from pydbus import SystemBus
bus = SystemBus()
accounts = bus.get('org.freedesktop.Accounts', '/org/freedesktop/Accounts')

for line in open(os.path.join(BaseDirectory.load_first_config("nitrogen"), "bg-saved.cfg"), "r").readlines():
	if line.startswith("file="):
		file = line.split("=")[1].strip()

		#Get current user's dbus path:
		user_name = GLib.get_user_name()
		user = accounts.FindUserByName(user_name)
		up = bus.get('org.freedesktop.Accounts', user)

		#Set current user's background picture file:
		up.SetBackgroundFile(file) # User Account
		up.Set("org.freedesktop.DisplayManager.AccountsService", "BackgroundFile", GLib.Variant ('s', (file))) # Display Manager
		Gio.Settings.new("org.gnome.desktop.background").set_string("picture-uri", file) # GSettings

		break