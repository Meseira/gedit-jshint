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

import json
import sys

from gi.repository import Gtk

from . import config as Config

__all__ = ("ConfigPanel", )

class ConfigPanel(Gtk.Box):
    """Panel to configure the JSHint plugin."""

    def __init__(self):
        Gtk.Box.__init__(self,
                orientation=Gtk.Orientation.VERTICAL,
                spacing=10,
                border_width=10)

        # Option selector panel
        selector_panel = Gtk.Notebook()
        selector_panel.append_page(
                Gtk.Label("Enforcing options"),
                Gtk.Label("Enforcing"))
        selector_panel.append_page(
                Gtk.Label("Relaxing options"),
                Gtk.Label("Relaxing"))
        selector_panel.append_page(
                Gtk.Label("Environments options"),
                Gtk.Label("Environments"))
        for child in selector_panel.get_children():
            selector_panel.child_set_property(child, "tab_expand", True)

        # Global options panel
        global_panel = Gtk.Box(
                orientation=Gtk.Orientation.HORIZONTAL,
                spacing=10)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)

        spin = Gtk.SpinButton()
        spin.set_numeric(True)
        spin.set_range(1, 999)
        spin.set_increments(1, 10)

        initial_value = 50 # Default
        with open(Config.get_options_file(), "r") as f:
            try:
                data = json.load(f)
            except ValueError as e:
                print("JSHint Plugin: error in options file:\n" + str(e),
                        file=sys.stderr)
            else:
                if ("maxerr" in data.keys() and
                        isinstance(data["maxerr"], int) and
                        data["maxerr"] > 0):
                    initial_value = data["maxerr"]
        spin.set_value(initial_value)

        grid.attach(Gtk.Label("Maximum amount of warnings:", xalign=0),
                0, 0, 1, 1)
        grid.attach(spin, 1, 0, 1, 1)
        grid.attach(Gtk.Label("warnings", xalign=0),
                2, 0, 1, 1)

        global_panel.pack_start(grid, True, True, 0)

        frame = Gtk.Frame(label="Other global options")
        global_panel.pack_start(frame, True, True, 0)

        self.pack_start(selector_panel, True, True, 0)
        self.pack_start(Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL),
                True, True, 0)
        self.pack_start(global_panel, True, True, 0)

        #self._widget = Gtk.Notebook()
        #self._widget = Gtk.Label("Configuration panel for JSHint Plugin")

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
