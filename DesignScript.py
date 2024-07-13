"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
"""________________Welcome to BIM3DM-DYNAMO API___________________"""
import clr 
import sys
import sys
import importlib

sys.path.append(r'U:\17_TrainingAdvanceDynamo\2_WORKING\Tool\Dynamo\Training-Dynamo-2024')

from Libraries.ListObjects import *
from Libraries.Parameters import *
from Libraries.Points import *
from Libraries.Units import *

import math 
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

################################################################
elements = UnwrapElement(IN[0])

points = [getLocationElement(e) for e in elements]
index , sortedPoints  = sortPoints(points)
OUT = getItemsByIndexes(elements, index)



