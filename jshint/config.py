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

import os

from gi.repository import GLib

def check_config_files():
    config_dir = get_config_dir()
    os.makedirs(config_dir, exist_ok=True)

    options_file = get_options_file()
    if not os.path.exists(options_file):
        with open(options_file, "w") as f:
            # Default JSHint options
            print('{"maxerr": 50}', file=f)

def get_config_dir():
    return os.path.join(GLib.get_user_config_dir(), 'gedit/jshint')

def get_options_file():
    return os.path.join(get_config_dir(), "options.json")
