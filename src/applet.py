#!/usr/bin/python2

# applet.py: contains code for the gnome-schedule applet
# Copyright (C) 2004, 2005 Philip Van Hoof <me at freax dot org>
# Copyright (C) 2004, 2005 Gaute Hope <eg at gaute dot eu dot org>
# Copyright (C) 2004, 2005 Kristof Vansant <de_lupus at pandora dot be>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

#python modules
import pygtk
import gtk
import gnomeapplet
import sys

import config

class Applet:
	def __init__(self, window = 0):
		if window == 1:
			main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
			main_window.set_title("gnome-schedule-applet")
			main_window.connect("destroy", gtk.mainquit) 
			self.app = gnomeapplet.Applet()
			self.app_factory(self.app, None)
			self.app.reparent(main_window)
			main_window.show_all()
		else:
			gnomeapplet.bonobo_factory("OAFIID:GNOME_schedule_Factory", gnomeapplet.Applet.__gtype__, "gnome-schedule", config.getVersion(), self.app_factory)

	def app_factory(self, applet, iid):	
		label = gtk.Label("bleh")
		applet.add(label)
		applet.show_all()
		return gtk.TRUE
		