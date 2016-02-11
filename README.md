JSHint plugin for Gedit
=======================

This software is a plugin for the text editor [Gedit][1]. It allows to check JavaScript source code with the static code analysis tool [JSHint][2]. To get more information about JSHint and to try it online, visit the [official website][3].

* Author: Xavier Gendre

Requirements
------------

This plugin is for Gedit 3 and is **not compatible with Gedit 2**.

The JavaScript runtime environment [Node.js][4] is needed to run the JSHint script. In a Debian-like operating system, simply install the package `nodejs`:

```sh
sudo apt-get update
sudo apt-get install nodejs
```

Installation
------------

1. Download this repository by clicking the *Download ZIP* button at the top of the [GitHub page][5] or clone it with the following command:

    ```sh
    git clone https://github.com/Meseira/gedit-jshint.git
    ```

2. Copy the file `jshint.plugin` and the folder `jshint` to `~/.local/share/gedit/plugins/` (you will need to create this folder if it does not already exist).

3. Restart Gedit.

4. Activate the plugin in the *Gedit Preferences*, go to the *Plugins* tab and check the box next to *JSHint*.

5. **(Optional)** To activate the plugin's configuration panel, some GSettings schemas need to be installed. Without this step, only [inline configuration][10] is available. Install the schemas with the commands:

    ```sh
    sudo cp org.gnome.gedit.plugins.jshint.gschema.xml /usr/share/glib-2.0/schemas/
    sudo glib-compile-schemas /usr/share/glib-2.0/schemas/
    ```

Usage
-----

When a JavaScript source code file is active, you can check it with *Tools > Check with JSHint* or with the accelerator `Ctrl+J`. The results are automatically displayed in the bottom panel. See the *Preferences* of the plugin to modify the JSHint options.

Notes
-----

By default, the plugin only checks JavaScript source code with the JSHint default parameters. JSHint options can be modified through the *Preferences* panel of the plugin (not all options are available for now, this is a work in progress). [Inline configuration][10] can be used to set JSHint options for a specific file.

License
-------

The JSHint plugin for Gedit is a free software and is distributed under the terms of the [GNU General Public License][6] as published by the [Free Software Foundation][7]; either version 3 of the License, or (at your option) any later version. A copy of this license can be found in the file `LICENSE` included with the source code of this plugin.

The included JSHint script (found in the subdirectory `jshint/js/`) has its own license, namely the [MIT Expat License][8], which can be found in the file `jshint/js/LICENSE` included with the source code of this plugin.  
**Website:** https://github.com/jshint/jshint/blob/master/dist/jshint.js

Compatibility
-------------

The JSHint plugin has been tested with Debian Jessie and Gedit 3.14. It should work without any trouble with any version of Gedit 3. Feel free to report any other working environment.

Issues
------

If you encounter any problem with this software, do not hesitate to report it in a [GitHub issue][9].

  [1]: https://wiki.gnome.org/Apps/Gedit
  [2]: https://github.com/jshint/jshint
  [3]: http://jshint.com/
  [4]: https://nodejs.org/
  [5]: https://github.com/Meseira/gedit-jshint
  [6]: https://gnu.org/licenses/gpl.html
  [7]: https://www.fsf.org/
  [8]: https://www.gnu.org/licenses/license-list.html#Expat
  [9]: https://github.com/Meseira/gedit-jshint/issues
  [10]: http://jshint.com/docs/#inline-configuration
