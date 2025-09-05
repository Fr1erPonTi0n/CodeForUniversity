from inventory import Inventory
from times import Time

def main():
    inv = Inventory()
    inv["stone"] = 25
    inv["wood"] = 15
    print(inv)

    inv2 = Inventory()
    inv2["silver"] = 5
    inv2["wood"] = 10
    inv2["diamond"] = 4
    print(inv2)

    combined = inv + inv2
    print(combined)

    if 'diamond' in inv2:
        print("В инвентаре2 есть алмазы.")
    else:
        print("В инвентаре2 нет алмазов.")

    del inv2["diamond"]
    print(inv2)
    if 'diamond' in inv2:
        print("В инвентаре2 есть алмазы.")
    else:
        print("В инвентаре2 нет алмазов.")

    t1 = Time(2, 30, 15)
    t2 = Time(1, 45, 30)

    print("Время 1:", t1)
    print("Время 2:", t2)

    sum_time = t1 + t2
    print("Сумма времени:", sum_time)

    diff_time = t1 - t2
    print("Разница времени:", diff_time)

    print("Общее количество секунд в t1:", t1.total_seconds())
    print("Общее количество секунд в t2:", t2.total_seconds())

    if t1 == t2:
        print("Времена равны")
    else:
        print("Времена не равны")

if __name__ == "__main__":
    main()
