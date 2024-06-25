
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

def createLineByPoints(points):
    lines = []
    #logic
    return lines

# The inputs to this node will be stored as a list in the IN variables.
counts = IN[1]
disPointY = IN[2]
disPointZ = IN[3]
if int(counts)>0 and int(disPointZ) > 0:
	lstPoint1,lstPoint2,lstPoint3,lstPoint4,lstPoint5,lstPoint6,lstPoint7 = []
# Place your code below this line

	for i in range(int(counts)):
	    point1 = Point.ByCoordinates(i,0,int(disPointZ))
	    lstPoint1.append(point1)
	    point2 = Point.ByCoordinates(i,int(disPointY),int(disPointZ))
	    lstPoint2.append(point2)
	    point3 = Point.ByCoordinates(i,2*int(disPointY),int(disPointZ))
	    lstPoint3.append(point3)
	    if i == int(counts)-1:
	        point4 = Point.ByCoordinates(i,0,0)
	        point5 = Point.ByCoordinates(i,2*int(disPointY),0)
	P1 =  Point.ByCoordinates(lstPoint1[0].X,0,0)
	P2 =  Point.ByCoordinates(lstPoint3[0].X,2*int(disPointY),0)
	lstLine1,lstLine2,lstLine3,lstLine4,lstLine5,lstLine6,lstLine7,lstLine8 = []
	for i in range(len(lstPoint1)-1):
	    lstLine1.append(Line.ByStartPointEndPoint(lstPoint1[i],lstPoint2[1:][i]))
	    lstLine2.append(Line.ByStartPointEndPoint(lstPoint2[i],lstPoint1[1:][i]))
	    lstLine3.append(Line.ByStartPointEndPoint(lstPoint3[i],lstPoint2[1:][i]))
	    lstLine4.append(Line.ByStartPointEndPoint(lstPoint2[i],lstPoint3[1:][i]))
	lstLine5.append(Line.ByStartPointEndPoint(lstPoint1[0],P1))
	lstLine6.append(Line.ByStartPointEndPoint(lstPoint1[len(lstPoint1)-1],point4))
	lstLine7.append(Line.ByStartPointEndPoint(lstPoint3[0],P2))
	lstLine8.append(Line.ByStartPointEndPoint(lstPoint3[len(lstPoint1)-1],point5))
	OUT = lstLine1,lstLine2,lstLine3,lstLine4,lstLine5,lstLine6,lstLine7,lstLine8

lstLine1, lstLine2, lstLine3 = [[1],[2],[3]]


