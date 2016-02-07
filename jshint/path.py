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

import os.path

__all__ = ("Path", )

class Path(object):
    """Class to recover useful paths for JSHint plugin."""

    def __init__(self, module_dir):
        self._base_dir = os.path.join(os.path.abspath(module_dir), "jshint")

    @property
    def base_dir(self):
        """JSHint plugin directory"""
        return self._base_dir

    @property
    def js_dir(self):
        """JavaScript sources directory"""
        return os.path.join(self._base_dir, "js")

    @property
    def jshint_script(self):
        """Path to JSHint script"""
        # TODO Check if file exists
        return os.path.join(self.js_dir, "jshint.js")

    @property
    def run_script(self):
        """Path to the script running JSHint"""
        # TODO Check if file exists
        return os.path.join(self.js_dir, "run.js")
