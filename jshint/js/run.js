// JSHint plugin for Gedit
// Copyright (C) 2016 Xavier Gendre <gendre.reivax@gmail.com>
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

(function (jshint_script, target_file, options_file) {
  "use strict";

  var fs = require('fs');
  var JSHINT = require(jshint_script).JSHINT;

  var options = {};
  try {
    options = require(options_file);
  } catch(err) {
    /* An error occurred */
  }

  var array = fs.readFileSync(target_file).toString().split("\n");

  JSHINT(array, options, {});
  console.log(JSON.stringify(JSHINT.data()))

}(process.argv[2], process.argv[3], process.argv[4]));
