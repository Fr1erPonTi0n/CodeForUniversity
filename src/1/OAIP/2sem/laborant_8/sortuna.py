def sortuna(data):
    return sorted(data, key=lambda x: (x[2], -x[1], len(x[0]), -x[1]))