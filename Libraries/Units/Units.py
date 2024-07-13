"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
"""________________Welcome to BIM3DM-DYNAMO API___________________"""
import clr 
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

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


def getCurrentLengthUnits(doc):
    """
    Retrieve the current length unit used in a Revit document.
    Args:
    doc (Document): The active Revit document.
    Returns:
    ForgeTypeId: The current length unit as a ForgeTypeId.
    """
    projectUnits =doc.GetUnits()
    lengthUnit = projectUnits.GetFormatOptions(SpecTypeId.Length).GetUnitTypeId()
    return lengthUnit
def convertUnits(value, fromUnit='Feet'):
    """
    Convert a measurement from one unit to another.

    Args:
    value (float): The measurement in the 'fromUnit'.
    fromUnit (ForgeTypeId): The unit type of the input value.
    toUnit (ForgeTypeId): The unit type to convert to.

    Returns:
    float: The measurement in the 'toUnit'.
    """
    fromUnit = UnitTypeId.Feet
    if fromUnit == 'mm':
        fromUnit = UnitTypeId.Feet
    currentLengthUnit = getCurrentLengthUnits(doc)
    convertedValue = UnitUtils.Convert(value, fromUnit, currentLengthUnit)
    return convertedValue
