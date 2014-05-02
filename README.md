Python BRL-CAD Interface
=======================
Gustave Granroth.
03/29/2014

Functions in Python to program complex structures conveniently in BRL-CAD. 
Simple enough to be useful, but not comprehensive enough to be a Python Package.

Usage Instructions:

 1. Change the 'mged' binary directory in the interface to point to the correct directory.
   -- You may need to change the executable name, based on your system. --
 2. Change the object name to your desired '.g' output filename.
 3. Insert your CSG operations by using the provided functions (see example) appropriately.
 4. Run, open 'mged' to view results.

Notes:
 The resultant '.g' file is placed in the 'mged' directory. Older versions of the '.g' file with the same name
 are overwritten.
 
TODO List:

 Anyone who wants to contribute can:
 1. Add more of BRL-CAD's functionality into this interface.
 2. Refactor this interface into a proper Python library.
 3. Add custom functionality (extruded text? surfaces of revolution? extrusions?)
 4. Do what you want and send me an email.

Contact Information:
 Gustave Granroth
 gus.gran@gmail.com