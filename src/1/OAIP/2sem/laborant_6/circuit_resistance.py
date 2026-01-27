def circuit_resistance(*resistances, connection='serial', conductivity=False):
    if connection == 'serial':
        total_resistance = sum(resistances)
    elif connection == 'parallel':
        total_resistance = 1 / sum(1 / r for r in resistances)
    else:
        total_resistance = None

    if total_resistance is not None:
        if conductivity:
            total_resistance = 1 / total_resistance
        return round(total_resistance, 4)