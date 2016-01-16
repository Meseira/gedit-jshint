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
        '"reason":"' + encodeURI(element.reason) +
        '}');
  });

  process.exit(0);

}(process.argv[2], process.argv[3]));
