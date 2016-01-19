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
import subprocess as sp
import tempfile as tf

class JSHint(object):

    def __init__(self):
        # Path to JavaScript sources
        self._path_js = os.path.join(os.path.dirname(__file__), "js")
        self._path_jshint = os.path.join(self._path_js, "jshint.js")
        self._path_run = os.path.join(self._path_js, "run.js")

        # Locate the Node.js binary
        self._nodejs_bin = None

        try:
            output = sp.check_output(
                    ["whereis", "-b", "nodejs", "node"],
                    universal_newlines=True).strip().split('\n')
        except sp.CalledProcessError:
            return
        except OSError:
            return

        if len(output[0].split()) > 1:
            # Found a binary for 'nodejs'
            self._nodejs_bin = output[0].split()[1]
        elif len(output[1].split()) > 1:
            # Found a binary for 'node'
            self._nodejs_bin = output[1].split()[1]

    def run(self, doc):
        if not self._nodejs_bin:
            return '{"error":1,"data":"Cannot find Node.js binary"}'

        start = doc.get_start_iter()
        end = doc.get_end_iter()
        text = doc.get_text(start, end, True).encode()

        with tf.NamedTemporaryFile() as f:
            f.write(text)
            f.flush()

            cmd = ' '.join([
                self._nodejs_bin,
                self._path_run,
                self._path_jshint,
                f.name])
            cmd_array = shlex.split(cmd)

            try:
                output = sp.check_output(cmd_array, universal_newlines=True)
            except sp.CalledProcessError as e:
                output = '{"error":1,"data":"Code ' + str(e.returncode) + '"}'
            except OSError as e:
                output = '{"error":1,"data":"' + e.strerror.replace('"', '\'') + '"}'

        return output.strip()
