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

from gi.repository import GLib, GObject, Gedit, Gio

class AppActivatable(GObject.Object, Gedit.AppActivatable):
    __gtype_name__ = "JSHintAppActivatable"

    app = GObject.property(type=Gedit.App)

    def __init__(self):
        GObject.Object.__init__(self)
        self._menu_ext = None

    def do_activate(self):
        action = Gio.SimpleAction(name="check-with-jshint")
        action.connect("activate",
                lambda action, data: print("Test JSHint Plugin"))
        self.app.add_action(action)

        self.app.set_accels_for_action("app.check-with-jshint", ["<Ctrl>J"])

        self._menu_ext = self.extend_menu("tools-section")
        item = Gio.MenuItem.new("Check with JSHint", "app.check-with-jshint")
        self._menu_ext.append_menu_item(item)

    def do_deactivate(self):
        self._menu_ext = None
        self.app.set_accels_for_action("app.check-with-jshint", [])
        self.app.remove_action("check-with-jshint")
