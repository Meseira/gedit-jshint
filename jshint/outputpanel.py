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
import urllib.request

from gi.repository import Gtk

__all__ = ("OutputPanel", )

class OutputPanel(Gtk.ScrolledWindow):
    """Panel to display the results of a JSHint run."""

    def __init__(self):
        Gtk.ScrolledWindow.__init__(self)

        self._tree_view = Gtk.TreeView(Gtk.ListStore(str, str))
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Message", renderer, text=0, background=1)
        self._tree_view.append_column(column)
        self.add(self._tree_view)

        self.show_all()

    def clear(self):
        """Remove all rows."""

        self._tree_view.get_model().clear()

    def update(self, report_json):
        """Update the panel with informations from the JSHint report
        given as a JSON string.
        """

        self.clear()

        report = {}
        try:
            report = json.loads(report_json)
        except ValueError:
            print("JSHint Plugin: error parsing JSON", file=sys.stderr)

        if report:
            if "unused" in report.keys():
                for item in report["unused"]:
                    message = ''.join([
                        str(item["line"]), ":", str(item["character"]), " ",
                        "Unused variable '", item["name"], "'"])
                    self._tree_view.get_model().append([message, "white"])

            if "errors" in report.keys():
                for item in report["errors"]:
                    message = ''.join([
                        str(item["line"]), ":", str(item["character"]), " ",
                        urllib.request.unquote(item["reason"])])
                    self._tree_view.get_model().append([message, "white"])

            if not ("unused" in report.keys() or "errors" in report.keys()):
                # No error, perfect code!
                self._tree_view.get_model().append([
                    "No error, congrats!",
                    "green"])
        else:
            # Something went wrong
            self._tree_view.get_model().append([
                "An error occurred, see the logs",
                "red"])
