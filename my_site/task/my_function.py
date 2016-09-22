def MyIsinstance(obj):
    if isinstance(obj, BoolProperrtyInline):
        return True
    elif isinstance(obj, StrPropertyInline):
        return True
    else:
        return False

def SortProperty(dict, obj):
    for item in obj:
        try:
            dict[item.group].append(item)
        except KeyError:
            dict[item.group] = list()
            dict[item.group].append(item)
    return dict
