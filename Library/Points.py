def getMaxPoints(points):
    maxPointZ = points[0].Z
    tempPoint = points[0]
    for point in points:
        if point.Z > maxPointZ:
            maxPointZ = point.Z
            tempPoint = point
    return tempPoint