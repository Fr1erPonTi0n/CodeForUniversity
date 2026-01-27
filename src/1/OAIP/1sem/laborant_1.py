#  Методы (cash_change, feedback и list_tuples_dict_and_set) работают без print().
#  1 ЗАДАНИЕ


def cinema(film, cin, time):
    return f'Билет на "{film}" в "{cin}" на {time} забронирован.'


#  2 ЗАДАНИЕ


def monthly_salary(cash_mount, count_hours):
    return f'Размер премии: {(cash_mount * 0.01) * count_hours}'


#  3 ЗАДАНИЕ


def cash_change(n):
    n1 = n // 1000
    n2 = (n % 1000) // 100
    n3 = (n % 100) // 10
    n4 = (n % 10) // 1
    print(n4, '- по 1р')
    print(n3, '- по 10р')
    print(n2, '- по 100р')
    print(n1, '- по 1000р')


#  4 ЗАДАНИЕ


def positive_feedback(text):
    corret_words = ['весело', 'увлекательно', 'развлечения']
    corret_numbers = []
    for i in range(len(corret_words)):
        if corret_words[i] in text:
            corret_numbers.append(text.find(corret_words[i]))
        else:
            continue
    return corret_numbers


#  5 ЗАДАНИЕ


def middle_letter(text):
    if len(text) % 2 != 0:
        return f'Средняя буква: {text[len(text) // 2]}'
    else:
        return f'Средняя буква: {text[(len(text) // 2) - 1]}'


#  6 ЗАДАНИЕ


def feedback():
    fdb = 'Алиса и Вася, большое спасибо за теплый приём!'
    name1 = fdb[:5]
    name2 = fdb[8:12]
    print(f'Назначить премию: {name1}/{name2}')


#  7 ЗАДАНИЕ


def four_letters_alphabet(n):
    print_words = [chr(ord('A') + (n + i) % 26) for i in range(-1, 3)]
    return 'Буквы: ' + ''.join(print_words)


# 8-11 ЗАДАНИЕ


def list_tuples_dict_and_set():
    print('--list().start()--')
    lista = []
    print(lista)
    print('Создать список')
    print('-----')
    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    print(lista)  # [1, 2, 3, 4]
    print('Добавить элементы')
    print('-----')
    lista.pop(0)
    print(lista)  # [2, 3, 4]
    print('Удалить элемент')
    print('-----')
    print(lista[1:3])  # [3, 4]
    print('Сделать срез')
    print('-----')
    list2 = []
    for i in reversed(lista):
        list2.append(i)
    print(list2)  # [4, 3, 2]
    print('Перевернуть список (1 способ)')
    print('-----')
    print(lista[::-1])  # [4, 3, 2]
    print('Перевернуть список (2 способ)')
    print('-----')
    lista = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(lista)  # [[1, 2], [3, 4], [5, 6], [7, 8]]
    print('Сделать двумерный список')
    print('-----')
    print(lista[0])  # [1, 2]
    print('Работа с индексации двумерного списка (1)')
    print('-----')
    print(lista[1][1])  # 4
    print('Работа с индексации двумерного списка (2)')
    print('-----')
    lista.clear()
    print(lista)  # []
    print('Очистить список')
    print('--list().end()--')

    print()
    print('--tuple().start()--')
    print(())  # ()
    print('Создание пустого кортежа')
    print('-----')
    print((1, 2, 3, "hello", True))  # (1, 2, 3, 'hello', True)
    print('Создание заполненого кортежа')
    print('--tuple().end()--')

    print()
    print('--set().start()--')
    seta = set()
    print(set())  # set()
    print('Создание пустого множества')
    print('-----')
    sets = {'12', '45'}
    print(sets)  # {'12', '45'}
    print('Создание множества с элементами')
    print('-----')
    seta.add('123')
    seta.add('123')
    seta.add('44')
    seta.add('55')
    print(seta)  # {'44', '123', '55'}
    print('Добавить в пустое множество элементы')
    print('-----')
    print({1, 2, 3, 2, 1} == {3, 1, 2})  # True
    print('Выполнить основные операции с множествами (1)')
    print('-----')
    print(seta | sets)  # {'12', '45', '123', '44', '55'}
    print('Выполнить основные операции с множествами (2)')
    print('-----')
    print(seta & sets)  # set()
    print('Выполнить основные операции с множествами (3)')
    print('-----')
    print(seta - sets)  # {'123', '44', '55'}
    print('Выполнить основные операции с множествами (4)')
    print('-----')
    print(seta ^ sets)  # {'55', '44', '12', '45', '123'}
    print('Выполнить основные операции с множествами (5)')
    print('--set().end()--')

    print()
    print('--dict().start()--')
    empty_dict = {}
    print(empty_dict)  # {}
    print('Создание пустого словаря')
    print('-----')
    my_dict = {"name": "Иван", "age": 30, "city": "Москва"}
    print(my_dict)  # {'name': 'Иван', 'age': 30, 'city': 'Москва'}
    print('Создание словаря с элементами')
    print('-----')
    my_dict["profession"] = "программист"
    print(my_dict)  # {'name': 'Иван', 'age': 30, 'city': 'Москва', 'profession': 'программист'}
    print('Добавить значение')
    print('-----')
    del my_dict["age"]
    print(my_dict)  # {'name': 'Иван', 'city': 'Москва', 'profession': 'программист'}
    print('Удалить значение')
    print('-----')
    my_dict["city"] = "Санкт-Петербург"
    print(my_dict)  # {'name': 'Иван', 'city': 'Санкт-Петербург', 'profession': 'программист'}
    print('Изменить значение')
    print('--dict().end()--')
