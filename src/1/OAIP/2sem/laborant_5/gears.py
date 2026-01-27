def gears(data, n, m):
    a, b = {}, {}
    for gear_list in data:
        for gear in gear_list:
            if gear % n == 0 and gear >= n:
                rn = gear // n
                if rn not in a and rn in b:
                    return gear, b[rn]
                a[rn] = gear
            elif gear % m == 0 and gear >= m:
                rm = gear // m
                if rm not in b and rm in a:
                    return a[rm], gear
                b[rm] = gear
    return None, None
