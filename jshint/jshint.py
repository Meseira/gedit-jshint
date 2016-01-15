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

import subprocess as sp

class JSHint(object):

    script_path = "js/jshint-2.9.1-rc3.js"

    def __init__(self):
        # FIXME only for Debian based distribution (/usr/bin/node for others)
        self._nodejs_bin = "/usr/bin/nodejs"

    def run(self):
        print("Test JSHint Plugin : " + self.script_path)
        try:
            test_str = sp.check_output(
                [self._nodejs_bin, "-e", "console.log(42)"],
                universal_newlines=True)
            print("Test : " + test_str)
        except sp.CalledProcessError as e:
            print("CalledProcessError (" + e.returncode + ")")
        except OSError as e:
            print("OSError : " + e.strerror)
