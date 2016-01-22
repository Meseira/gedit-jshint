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

from gi.repository import GObject, Gedit, Gio

from .jshint import JSHint
from .outputpanel import OutputPanel

class WindowActivatable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "JSHintWindowActivatable"

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)
        self._action = None
        self._jshint = None
        self._panel = None

    def do_activate(self):
        self._action = Gio.SimpleAction(name="check-with-jshint")
        self._action.connect("activate", self._run_jshint)
        self.window.add_action(self._action)

        self._panel = OutputPanel()
        bottom_panel = self.window.get_bottom_panel()
        bottom_panel.add_titled(self._panel, "JSHintOutputPanel", "JSHint")

        self._jshint = JSHint()

    def do_deactivate(self):
        self._jshint = None
        self._panel = None

        self.window.remove_action("check-with-jshint")
        self._action = None

    def do_update_state(self):
        doc = self.window.get_active_document()
        state = False

        if doc:
            lang = doc.get_language()
            # Only for JavaScript
            if lang and lang.get_id() == "js":
                state = True

        self._action.set_enabled(state)
        if state:
            self._panel.show()
        else:
            self._panel.hide()

    def _run_jshint(self, action, data=None):
        doc = self.window.get_active_document()
        if doc:
            bottom_panel = self.window.get_bottom_panel()
            result = self._jshint.run(self.window.get_active_document())

            # Show JSHint panel if not visible
            if not bottom_panel.is_visible():
                bottom_panel.set_visible(True)
            if bottom_panel.get_visible_child() != self._panel:
                bottom_panel.set_visible_child(self._panel)

            self._panel.clear()
            for item in result.split('\n'):
                self._panel.append(item)
