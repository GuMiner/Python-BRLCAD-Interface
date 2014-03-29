# Atmel Programmer Case Design (For USBAsp v2) 
# Gustave Granroth 03/28/2014

# Imports
import math
import os
import subprocess

# Standard conversion factors
INtoMM = 25.4
DEGtoRAD = math.pi/180

# Command storage holders (for block-applications of geometry)
global itemCount
itemCount = 1 # The item count we are at ... we combine all items together.

# Create our object and prepare for using BRL-CAD
objName = 'ProgrammerCase';
os.chdir(r"C:\users\<INSERT YOUR BINARY PATH HERE>\Documents\BRLCAD 7.24.0\bin")
subprocess.call("del " + objName + ".g", shell=True)

header = "mged.exe -c " + objName + ".g "
commandQueue = []

## Start of Library Code ##
    
# Creates an arbitrary 6-point shape.
def Arb6(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, x5, y5, z5, x6, y6, z6):
    global itemCount
    commandQueue.append('in shape' + str(itemCount) + '.s arb6 '
        + str(x1) + ' ' + str(y1) + ' ' + str(z1) + ' '
        + str(x2) + ' ' + str(y2) + ' ' + str(z2) + ' '
        + str(x3) + ' ' + str(y3) + ' ' + str(z3) + ' '
        + str(x4) + ' ' + str(y4) + ' ' + str(z4) + ' '
        + str(x5) + ' ' + str(y5) + ' ' + str(z5) + ' '
        + str(x6) + ' ' + str(y6) + ' ' + str(z6) + ' \n')
    itemCount += 1
    return itemCount - 1

# Creates an arbitrary 8-pointed shape.
def Arb8(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, x5, y5, z5, x6, y6, z6, x7, y7, z7, x8, y8, z8):
    global itemCount
    commandQueue.append('in shape' + str(itemCount) + '.s arb8 '
        + str(x1) + ' ' + str(y1) + ' ' + str(z1) + ' '
        + str(x2) + ' ' + str(y2) + ' ' + str(z2) + ' '
        + str(x3) + ' ' + str(y3) + ' ' + str(z3) + ' '
        + str(x4) + ' ' + str(y4) + ' ' + str(z4) + ' '
        + str(x5) + ' ' + str(y5) + ' ' + str(z5) + ' '
        + str(x6) + ' ' + str(y6) + ' ' + str(z6) + ' '
        + str(x7) + ' ' + str(y7) + ' ' + str(z7) + ' '
        + str(x8) + ' ' + str(y8) + ' ' + str(z8) + ' \n')
    itemCount += 1
    return itemCount - 1
    
# Creates a triangular wedge growing in the z-direction
def Wedge(x1, y1, x2, y2, x3, y3, height, zOffset): 
    return Arb6(x1, y1, zOffset, x2, y2, zOffset, x2, y2, height + zOffset, x1, y1, height + zOffset,
        x3, y3, zOffset, x3, y3, height + zOffset)
    
# Creates a smooth wedge at x1, y1 pointing towards x2, y2 with height 'height', width 'width'
def SmoothWedge(x1, y1, z1, x2, y2, height, width):
    global itemCount
    commandQueue.append('in shape' + str(itemCount) + '.s rpc '
        + str(x1) + ' ' + str(y1) + ' ' + str(z1) + ' '
        + '0 0 ' + str(height) + ' '
        + str(x2) + ' ' + str(y2) + ' 0 '
        + str(width) + ' \n')
    itemCount += 1
    return itemCount - 1
            
# Creates a cylinder pointing in the z direction
def Cylinder(x, y, z, r, h):
    global itemCount
    commandQueue.append('in shape' + str(itemCount) + '.s rcc '
        + str(x) + ' ' 
        + str(y) + ' ' 
        + str(z) + ' 0 0 '
        + str(h) + ' '
        + str(r) + ' \n')
    itemCount += 1
    return itemCount - 1

# Create an "arbitrary cylinder" pointing from two points with radius r
def ArbCylinder(x, y, z, xx, yy, zz, r):
    global itemCount
    commandQueue.append('in shape' + str(itemCount) + '.s rcc '
        + str(x) + ' ' 
        + str(y) + ' ' 
        + str(z) + ' '
        + str(xx) + ' '
        + str(yy) + ' '
        + str(zz) + ' '
        + str(r) + ' \n')
    itemCount += 1
    return itemCount - 1
    
# Create a sphere
def Sphere(x, y, z, r):
    global itemCount
    commandQueue.append('in shape' + str(itemCount) + '.s sph '
        + str(x) + ' '
        + str(y) + ' ' 
        + str(z) + ' '
        + str(r) + ' \n')
    itemCount += 1
    return itemCount - 1

# Create a x-y-z oriented cube
def Cube(x, y, z, xw, yw, zw):
    return Arb8(x, y, z, x + xw, y, z, x + xw, y, z + zw, x, y, z + zw,
        x, y + yw, z, x + xw, y + yw, z, x + xw, y + yw, z + zw, x, y + yw, z + zw)
    
## Start of library manipulation code ##

# Clear the command list as a block.
def FlushList(text):
    global commandQueue
    if len(commandQueue) >= 0:
        subprocess.call(header + ''.join(commandQueue))
        commandQueue = []
    print(text)

## Start of CSG operation code ##

# Performs the difference of one item to another item
def Difference(total, removal):
    global itemCount    
    commandQueue.append('comb shape' + str(itemCount) + '.s u shape' 
        + str(total) + '.s - shape' + str(removal) + '.s \n')
    itemCount += 1
    return itemCount - 1

# Unions two items together.
def Union(first, second):
    global itemCount
    commandQueue.append('comb shape' + str(itemCount) + '.s u shape'
        + str(first) + '.s u shape' + str(second) + '.s \n')
    itemCount += 1
    return itemCount - 1

# A very simple pipe (no fancy bend radius stuffs.
def Spipe(x, y, z, r1, r2, h):
    return difference(cylinder(x, y, z, r2, h), cylinder(x, y, z - 0.1, r1, h + 0.2))
    
## Start of application code ##

wallThickness = 1.2; # mm

length = INtoMM*1.724 
width = INtoMM*0.743

jumpWidth = INtoMM*0.095
jumpSep = INtoMM*0.078
jumpOffset = INtoMM*1.206

usbWidthLowX = INtoMM*0.135
usbWidthHighX = INtoMM*0.125
usbWidth = INtoMM*0.474
usbExtLength = INtoMM*0.163

lightWidthOffset = INtoMM*0.369
lightWidth = INtoMM*0.170
lightLength = INtoMM*0.160

usbHeight = INtoMM*0.20 
underHeight = INtoMM*0.080

smallUpDown = INtoMM*0.050
intoDistance = INtoMM*0.100

# Main cube and cutouts
mainCube = Cube(0, -wallThickness, -wallThickness, 
    length + wallThickness, width + 2*wallThickness, usbHeight + underHeight + 2*wallThickness)

smallCutout = Cube(-wallThickness, 0, underHeight - smallUpDown, 
    length + wallThickness, intoDistance + wallThickness, smallUpDown*2)
smallCutoutTop = Cube(-wallThickness, -2*wallThickness, smallUpDown*2 + wallThickness,
    length + 2*wallThickness, intoDistance + wallThickness, usbHeight + underHeight - smallUpDown*2)

insideCutout = Cube(-wallThickness, intoDistance, 0, 
    length + wallThickness, width - intoDistance, underHeight + usbHeight)

mainCutouts = Difference(Difference(Difference(mainCube, smallCutout), smallCutoutTop), insideCutout)

# Light Hole and slider hole
lightHole = Cube(length - jumpOffset, width - (lightWidthOffset + lightWidth), underHeight, 
    lightLength, lightWidth, usbHeight + 2*wallThickness)
sliderHole = Cube(-wallThickness, width - (jumpWidth + jumpSep), underHeight,
    length - jumpOffset, jumpWidth, usbHeight + 2*wallThickness)
    
specialCutouts = Difference(Difference(mainCutouts, lightHole), sliderHole)

# USB Hole
usbHolder = Cube(length, usbWidthLowX - wallThickness, 0, 
    usbExtLength, usbWidth + 2*wallThickness, usbHeight + underHeight)
usbHole = Cube(length - wallThickness, usbWidthLowX, wallThickness, 
    usbExtLength + 2*wallThickness, usbWidth, usbHeight + underHeight - 2*wallThickness)

#Final object
finObject = Difference(Union(specialCutouts, usbHolder), usbHole)

FlushList('Done with describing the programmer')

# Group all combinations and apply a region specifier for rendering
subprocess.call(header + 'r region1.r u shape' + str(finObject) + '.s \n');     
# For fancy transparency (but slower) use "plastic {tr 0.5 re 0.2}"
subprocess.call(header + 'mater region1.r plastic 0 255 0 0\n')
    
# At this point, open mged to check your results using your .g input file
# Call 'draw region1.r', 'ae 45 45' 'rt -s 900'
# l-click, zoom out , r-click, zoom in
# 'exit' to quit.