import math

from pygame.examples.testsprite import flags


def calculate_pn(n, flag):
    if n == 2:
        return 2 * math.sqrt(2)
    else:
        if flag:
            p_prev = calculate_pn(n - 1, True)
            term = (p_prev / (2 ** (n - 1))) ** 2
            return 2 ** (n - 1) * (2 * term) / (1 + math.sqrt(1 - term))
        else:
            p_prev = calculate_pn(n - 1, False)
            term = (p_prev / (2 ** (n - 1))) ** 2
            return 2 ** (n - 1) * math.sqrt(2 * (1 - math.sqrt(1 - term)))


for n in range(2, 40):
    pn1 = calculate_pn(n, False)
    pn2 = calculate_pn(n, True)
    delta1 = pn1 - math.pi
    delta2 = pn2 - math.pi
    print(f"p{n} = {pn1}    Δ = {delta1}     p{n} = {pn2}    Δ = {delta2}")
