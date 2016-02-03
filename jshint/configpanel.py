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

from gi.repository import Gtk

__all__ = ("ConfigPanel", )

class ConfigPanel(object):
    """Panel to configure the JSHint plugin."""

    def __init__(self):
        #self._widget = Gtk.Notebook()
        #self._widget = Gtk.Label("Configuration panel for JSHint Plugin")
        self._widget = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self._widget.pack_start(
                Gtk.Label("Options selector comes here"),
                True, True, 0)
        self._widget.pack_start(
                Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL),
                True, True, 0)
        self._widget.pack_start(
                Gtk.Label("Global options come here"),
                True, True, 0)

        #grid = Gtk.Grid()
        #for i in range(30):
        #    button = Gtk.CheckButton("Button {}".format(i))
        #    button.set_tooltip_text("This is the button {}".format(i))
        #    grid.attach(button, i // 10, i % 10, 1, 1)
        #self._widget.append_page(grid, Gtk.Label("Enforcing"))

        #page = Gtk.Box()
        #page.add(Gtk.Label("Relaxing options"))
        #self._widget.append_page(page, Gtk.Label("Relaxing"))

        #page = Gtk.Box()
        #page.add(Gtk.Label("Environments options"))
        #self._widget.append_page(page, Gtk.Label("Environments"))

    def get_widget(self):
        """Get the underlying Gtk widget."""

        return self._widget
