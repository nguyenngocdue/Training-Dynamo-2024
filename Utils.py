def getPositivePointByX(objects):
    result = []
    for p in objects:
        if p.X % 2 != 1:
            result.append(p)
    return result

def getPositivePointByField(objects, field):
    result = []
    for p in objects:
        if field == 'Z':
            if p.Z % 2 != 1:
                result.append(p)
        elif field == 'Y':
            if p.Y % 2 != 1:
                result.append(p)

    return result
