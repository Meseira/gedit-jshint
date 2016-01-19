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

import json
import urllib.request

class OutputPanel(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self)

        self._view = Gtk.TreeView(Gtk.ListStore(int, int, str))
        for i, title in enumerate(["Line", "Character", "Message"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(title, renderer, text=i)
            self._view.append_column(column)
        self.pack_start(self._view, True, True, 0)

        self.show_all()

    def append(self, json_string):
        try:
            item = json.loads(json_string)
        except ValueError:
            item = json.loads('{"error":1,"data":"Invalid JSON"}')

        if "error" in item.keys():
            self._view.get_model().append([0, 0, item["data"]])
        else:
            self._view.get_model().append([
                item["line"], item["character"],
                urllib.request.unquote(item["reason"])])

    def clear(self):
        self._view.get_model().clear()

