def future(vin, *mass, **const):
    CountConst = 1
    for key, value in const.items():
        CountConst *= float(value)
    sum_of_masses = sum(mass) * CountConst
    if sum_of_masses > vin:
        return 'ACCELERATION'
    elif sum_of_masses < vin:
        return 'DECELERATION'
    return 'UNCHANGED'