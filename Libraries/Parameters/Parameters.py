def getParameterValueFromLookup(element, paramName):
    parameter = element.LookupParameter(paramName)
    if parameter is not None and parameter.HasValue:
        #StorageType.Double
        if parameter.StorageType == StorageType.Double:
            if not parameter.AsDouble(): return "empty value"
            else: return parameter.AsDouble()*factorUnit
        #StorageType.String
        elif parameter.StorageType == StorageType.String:
            if not parameter.AsString(): return "empty value"
            else: return parameter.AsString()
        #StorageType.ElementId
        elif parameter.StorageType == StorageType.ElementId:
            if not parameter.AsElementId(): "empty value"
            else: return parameter.AsElementId()
        else: "123"
    else:
        None