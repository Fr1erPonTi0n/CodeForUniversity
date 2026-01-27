def nearby(data, places=1):
    return list(filter(lambda row: "0" * places in row, data))