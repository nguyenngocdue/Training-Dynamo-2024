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
from Points import *

#Preparing input from dynamo to revit
elements = UnwrapElement(IN[0])
field = IN[1]
distance = IN[2]




OUT = translatePointByField(elements, field, distance)