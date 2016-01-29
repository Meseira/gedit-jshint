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
import urllib.request

from gi.repository import Gtk

__all__ = ("OutputPanel", )

class OutputPanel(Gtk.ScrolledWindow):
    """Panel to display the results of a JSHint run."""

    def __init__(self):
        Gtk.ScrolledWindow.__init__(self)

        self._tree_view = Gtk.TreeView(Gtk.ListStore(int, int, str, str))
        renderer = Gtk.CellRendererText()
        for i, title in enumerate(["Line", "Character", "Message"]):
            column = Gtk.TreeViewColumn(title, renderer, text=i, background=3)
            self._tree_view.append_column(column)
        self.add(self._tree_view)

        self.show_all()

    def append(self, json_string):
        """Append a new line from a JSHint error in JSON format."""

        try:
            item = json.loads(json_string)
        except ValueError:
            item = json.loads('{"error":1,"data":"Invalid JSON"}')

        if "error" in item.keys():
            # Something went wrong
            self._tree_view.get_model().append([0, 0, item["data"], "red"])
        else:
            self._tree_view.get_model().append([
                item["line"],
                item["character"],
                urllib.request.unquote(item["reason"]),
                "white"])

    def clear(self):
        """Remove all rows."""
        self._tree_view.get_model().clear()
