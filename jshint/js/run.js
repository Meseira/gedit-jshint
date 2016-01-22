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

(function (jshint_script, target_file) {
  "use strict";

  if (!jshint_script || !target_file) {
    process.exit(1);
  }

  var fs = require('fs');
  var array = fs.readFileSync(target_file).toString().split("\n");

  var JSHINT = require(jshint_script).JSHINT;
  JSHINT(array);

  JSHINT.errors.forEach(function (element, index, array) {
    console.log(
        '{' +
        '"line":' + element.line + ',' +
        '"character":' + element.character + ',' +
        '"reason":"' + encodeURI(element.reason) + '"' +
        '}');
  });

  process.exit(0);

}(process.argv[2], process.argv[3]));
