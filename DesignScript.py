"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
"""________________Welcome to BIM3DM-DYNAMO API___________________"""
import clr 
import sys
sys.path.append(r'C:\Program Files\Autodesk\Revit 2020\AddIns\DynamoForRevit\IronPython.StdLib.2.7.8')
sys.path.append(r'U:\17_TrainingAdvanceDynamo\2_WORKING\Tool\Dynamo\Traning-Dynamo-2024\Library')
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *
from Points import getMaxPoints


#Preparing input from dynamo to revit
elements = UnwrapElement(IN[0])
field = IN[1]
distance = IN[2]

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

OUT = translatePointByField(elements, field, distance)