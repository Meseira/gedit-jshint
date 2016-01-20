JSHint plugin for Gedit
=======================

This software is a plugin for the text editor [Gedit][1]. It allows to check JavaScript source code with the static code analysis tool [JSHint][2]. To get more information about JSHint and to try it online, visit the [official website][3].

* Author: Xavier Gendre

Requirements
------------

This plugin is for Gedit 3 and is **not compatible with Gedit 2**.

The JavaScript runtime environment [Node.js][4] is needed to run the JSHint script. In a Debian-like operating system, simply install the package `nodejs`:
```
apt-get install nodejs
```

Installation
------------

1. Download this repository by clicking the `Download ZIP` button at the top of the [GitHub page][5] or clone it with the following command:

    git clone https://github.com/Meseira/gedit-jshint.git

2. Copy the file `jshint.plugin` and the folder `jshint` to `~/.local/share/gedit/plugins/` (you will need to create this folder if it does not already exist).

3. Restart Gedit.

4. Activate the plugin in the `Gedit Preferences`, go to the `Plugins` tab and check the box next to `JSHint`.

Usage
-----

When a JavaScript source code file is active, you can check it with `Tools > Check with JSHint` or with the accelerator `Ctrl+J`. The results are automatically displayed in the bottom panel.

Notes
-----

For now, the plugin only checks JavaScript source code with the JSHint default parameters. Allowing to modify the options is in the TODO list and will be available soon, hopefully.

License
-------

This plugin is a free software and is published under the [GNU General Public License][6] except one file, the JSHint script, that is published under the [MIT Expat License][7].

Compatibility
-------------

The JSHint plugin has been tested with Debian Jessie and Gedit 3.14. It should work without any trouble with any version of Gedit 3. Feel free to report any other working environment.

Issues
------

If you encounter any problem with this software, do not hesitate to report it in a [GitHub issue][8].

  [1]: https://wiki.gnome.org/Apps/Gedit
  [2]: https://github.com/jshint/jshint
  [3]: http://jshint.com/
  [4]: https://nodejs.org/
  [5]: https://github.com/Meseira/gedit-jshint
  [6]: https://gnu.org/licenses/gpl.html
  [7]: https://www.gnu.org/licenses/license-list.html#Expat
  [8]: https://github.com/Meseira/gedit-jshint/issues
