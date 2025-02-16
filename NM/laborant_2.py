import math


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


for n in range(3, 40):
    pn1 = calculate_pn(n, False)
    pn2 = calculate_pn(n, True)

    # Вычисляем разницу с π
    delta1 = pn1 - math.pi if pn1 != 0 else float('nan')
    delta2 = pn2 - math.pi if pn2 != 0 else float('nan')

    # Форматируем вывод
    delta1_str = f"{delta1:.16f}" if not math.isnan(delta1) else "---"
    delta2_str = f"{delta2:.16f}" if not math.isnan(delta2) else "---"

    print(f"p{n} = {pn1:.16f}    Δ = {delta1_str}     p{n} = {pn2:.16f}    Δ = {delta2_str}")