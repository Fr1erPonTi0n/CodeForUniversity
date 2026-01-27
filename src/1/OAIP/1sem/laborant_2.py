#  1 ЗАДАНИЕ


def string(text):
    if text == 'Python':
        return 'ДА'
    else:
        return 'НЕТ'


#  2 ЗАДАНИЕ


def double_str(text1, text2):
    if (text1 == 'да' and text2 == 'да') or (text1 == 'нет' and text2 == 'нет'):
        return 'ВЕРНО'
    else:
        return 'НЕВЕРНО'


#  3 ЗАДАНИЕ


def tree_burn(one, two, three):
    if one == '1' or one == 'раз':
        if two == '2' or two == 'два':
            if three == '3' or three == 'три':
                return 'ГОРИ'
            else:
                return 'НЕ ГОРИ'
        else:
            return 'НЕ ГОРИ'
    else:
        return 'НЕ ГОРИ'


#  4 ЗАДАНИЕ


def city_tour(city_1, city_2):
    if (((city_1 == 'Тула' and city_2 != 'Пенза' or city_1 != 'Тула' and city_2 == 'Пенза')
         or (city_2 == 'Пезна' or city_1 == 'Пенза') or (city_2 == 'Тула' or city_1 == 'Тула'))
            and city_1 != city_2):
        return 'ДА'
    else:
        return 'НЕТ'


#  5 ЗАДАНИЕ


def marafon(n, m):
    if n % m == 0:
        return n // m
    else:
        return n // m + 1


#  6 ЗАДАНИЕ


def drofosek(n):
    text_n = str(n)
    first_n = int(text_n[0])
    middle_n = int(text_n[1])
    third_n = int(text_n[2])
    if (first_n + third_n) % 8 != 0 and middle_n == 3:
        return "Подходит"
    else:
        return f"{first_n + third_n} {middle_n}"


#  7 ЗАДАНИЕ


def product_category(category):
    if category.lower() == "продукты":
        price = int(input("Введите цену: "))
        if price < 100:
            return "Попробуйте нашу выпечку!"
        elif 100 <= price < 500:
            return "Как насчёт орехов в шоколаде?"
        else:
            return "Попробуйте экзотические фрукты!"
    else:
        return "Загляните в товары для дома!"


#  8 ЗАДАНИЕ


def product_promotion(prices=[]):
    if prices == sorted(prices):
        total = sum(prices) / 2
        return f"Акция!\nК оплате: {total:.2f}"
    elif prices == sorted(prices, reverse=True):
        total = sum(prices) / 3
        return f"Акция!\nК оплате: {total:.2f}"
    else:
        total = sum(prices)
        return f"К оплате: {total:.2f}"


#  9 ЗАДАНИЕ


def predict_customers(n1, n2):
    if n1 < n2:
        return f'Сегодня магазин посетит: {n2 + (n2 - n1)} человек'
    elif n1 > n2:
        return f'Сегодня магазин посетит: {n2 - (n2 - n1)} человек'
    elif n1 == n2:
        return f'Сегодня магазин посетит: {n2} человек'


#  10 ЗАДАНИЕ


def leap_year(a):
    if ((abs(a) % 4) == 0 and not (abs(a) % 100) == 0) or (abs(a) % 400) == 0:
        return 'Високосный'
    else:
        return 'Не високосный'


#  11 ЗАДАНИЕ



def even_number(number):
    if number % 2 == 0:
        return "Четное"
    else:
        return "Нечетное"
