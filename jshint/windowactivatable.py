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

class WindowActivatable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "JSHintWindowActivatable"

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)
        self._action = None

    def do_activate(self):
        # Action for checking code
        self._action = Gio.SimpleAction(name="check-with-jshint")
        self._action.connect("activate",
                lambda action, data: print("Test JSHint Plugin"))
        self.window.add_action(self._action)

    def do_deactivate(self):
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
