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
        self._widget = Gtk.Notebook()

        page = Gtk.Box()
        page.add(Gtk.Label("Enforcing options"))
        self._widget.append_page(page, Gtk.Label("Enforcing"))

        grid = Gtk.Grid()
        grid.add(Gtk.CheckButton("Button 1"))

        page = Gtk.Box()
        page.add(Gtk.Label("Relaxing options"))
        self._widget.append_page(page, Gtk.Label("Relaxing"))

        page = Gtk.Box()
        page.add(Gtk.Label("Environments options"))
        self._widget.append_page(page, Gtk.Label("Environments"))

    @property
    def widget(self):
        """Get the underlying Gtk widget."""
        return self._widget
