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
import shlex
import subprocess
import tempfile

from gi.repository import Gedit

__all__ = ("JSHint", )

class JSHint(object):
    """Helper class to handle JSHint script."""

    def __init__(self):
        # JavaScript sources
        self._path_js = os.path.join(os.path.dirname(__file__), "js")
        self._path_jshint = os.path.join(self._path_js, "jshint.js")
        self._path_run = os.path.join(self._path_js, "run.js")

        # Locate Node.js binary
        self._nodejs_bin = None

        try:
            output = subprocess.check_output(
                        ["whereis", "-b", "nodejs", "node"],
                        universal_newlines=True)
        except subprocess.CalledProcessError:
            output = ""
        except OSError:
            output = ""
        finally:
            output = output.strip().split('\n')

        if len(output) == 2:
            if len(output[0].split()) > 1:
                # Found a binary for 'nodejs'
                self._nodejs_bin = output[0].split()[1]
            elif len(output[1].split()) > 1:
                # Found a binary for 'node'
                self._nodejs_bin = output[1].split()[1]

    def run(self, doc):
        """Run the JSHint script on the content of the GeditDocument
        doc with Node.js. Return a string with one error per line in
        JSON format.
        """

        if not self._nodejs_bin:
            return '{"error":1,"data":"Cannot find Node.js binary"}'

        text = doc.get_text(
                doc.get_start_iter(),
                doc.get_end_iter(),
                True).encode()

        with tempfile.NamedTemporaryFile() as f:
            f.write(text)
            f.flush()

            cmd = ' '.join([
                self._nodejs_bin,
                self._path_run,
                self._path_jshint,
                f.name])
            cmd_array = shlex.split(cmd)

            try:
                output = subprocess.check_output(
                        cmd_array,
                        universal_newlines=True)
            except subprocess.CalledProcessError as e:
                output = ' '.join([
                    '{"error":1,"data":"Code ',
                    str(e.returncode),
                    '"}'])
            except OSError as e:
                output = ' '.join([
                    '{"error":1,"data":"',
                    e.strerror.replace('"', '\''),
                    '"}'])

        return output.strip()
