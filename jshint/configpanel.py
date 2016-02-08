# -*- coding: utf-8 -*-
#    JSHint plugin for Gedit
#    Copyright (C) 2016 Xavier Gendre <gendre.reivax@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gio, Gtk

__all__ = ("ConfigPanel", )

class ConfigPanel(Gtk.Box):
    """Panel to configure the JSHint plugin."""

    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)

        label = Gtk.Label("Configuration panel for JSHint Plugin")
        self.pack_start(label, True, True, 0)

        if "org.gnome.gedit.plugins.jshint" in Gio.Settings.list_schemas():
            label = Gtk.Label()
            label.set_markup("<b>With GSettings</b>")
            self.pack_start(label, True, True, 0)
        else:
            label = Gtk.Label()
            label.set_markup('<span color="#FF0000">Without GSettings</span>')
            self.pack_start(label, True, True, 0)
