import clr 
import sys
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

def getMaxPoints(points):
    maxPointZ = points[0].Z
    tempPoint = points[0]
    for point in points:
        if point.Z > maxPointZ:
            maxPointZ = point.Z
            tempPoint = point
    return tempPoint
def translatePointByField(points, field = 'x', distance = 0):
    newPoints = []
    for point in points:
        x = point.X
        y = point.Y
        z = point.Z
        
        if field == 'x' or field == 'X':
            x = x + distance
        if field == 'y' or field == 'Y':
            y = y + distance
        if field == 'z' or field == 'Z':
            z = z + distance
        _point = Point.ByCoordinates(x,y,z)
        newPoints.append(_point)
    return newPoints