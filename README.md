Python BRL-CAD Interface
=======================

Synopsis
--------
This repository contains functions in Python to program complex structures conveniently in [BRL-CAD] (http://brlcad.org/). 
These functions are simple enough to be useful, but not comprehensive enough to be a Python Package.

Status
------
This project is no longer under active development as [OpenSCAD] (http://www.openscad.org/) has stabilized to the point where for my small projects there is no compelling reason for me to use BRL-CAD over OpenSCAD.

Usage Instructions
------------------

 1. Change the 'mged' binary directory in the interface to point to the correct directory.
   -- You may need to change the executable name, based on your system. --
 2. Change the object name to your desired '.g' output filename.
 3. Insert your CSG operations by using the provided functions (see example) appropriately.
 4. Run, open 'mged' to view results.

Notes:
 The resultant '.g' file is placed in the 'mged' directory. Older versions of the '.g' file with the same name
 are overwritten.
 
Future work
------------
1. Add more of BRL-CAD's functionality into this interface.
2. Refactor this interface into a proper Python library.
3. Add custom functionality (extruded text? surfaces of revolution? extrusions?)
4. Add something and create a PR.