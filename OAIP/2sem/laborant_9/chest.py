import random

all_items =  {
    "Зелье лечения": True,
    "Большое зелье лечения": True,
    "Зелье магии": True,
    "Большое зелье магии": True,
    "Зелье запаса сил": True,
    "Яд замедления": True,
    "Кусок сыра": True,
    "Жареный лосось": True,
    "Хлеб": True,
    "Яблоко": True,
    "Медовуха": True,
    "Железный слиток": True,
    "Серебряный слиток": True,
    "Золотой слиток": True,
    "Эбонитовый слиток": True,
    "Слоёное тесто": True,
    "Морозная соль": True,
    "Сердце даэдра": True,
    "Камень душ (пустой)": True,
    "Камень душ (заполненный)": True,
    "Чёрный камень душ": True,
    "Руда железная": True,
    "Руда эбонитовая": True,
    "Руда серебряная": True,
    "Руда золотая": True,
    "Сломанный двемерский гироскоп": True,
    "Древний нордский амулет": False,
    "Амулет Талоса": False,
    "Амулет Мары": False,
    "Амулет Дибеллы": False,
    "Амулет Акатоша": False,
    "Стеклянный меч": False,
    "Эбонитовый двуручный топор": False,
    "Стальной боевой молот": False,
    "Орочий боевой топор": False,
    "Двемерский кинжал": False,
    "Даэдрический меч": False,
    "Даэдрический двуручный меч": False,
    "Сапоги скрытности": False,
    "Перчатки кузнеца": False,
    "Капюшон архимага": False,
    "Одеяние некроманта": False,
    "Кираса братства теней": False,
    "Зачарованный эбонитовый щит": False,
    "Щит стражника Вайтрана": False,
    "Имперский шлем": False,
    "Стеклянные сапоги": False,
    "Одеяние мага разрушения": False,
    "Шлем пепельного стража": False,
    "Лунный сахар": True,
    "Скальпель алхимика": True,
    "Корень Нирна": True,
    "Светящийся гриб": True,
    "Крыло синей бабочки": True,
    "Огненная соль": True,
    "Лаванда": True,
    "Чеснок": True,
    "Сырой кроличий окорок": True,
    "Соль": True,
    "Свиток огненного шара": True,
    "Свиток ледяного шипа": True,
    "Свиток громового копья": True,
    "Костная мука": True,
    "Коготь дракона": False,
    "Коготь из чистого золота": False,
    "Древний свиток": False,
    "Кольцо некроманта": False,
    "Кольцо с рубином": False,
    "Рунический молот": False,
    "Глаз Фалмера": False,
    "Сфера двемеров": False,
    "Книга заклинаний: Оживление трупа": True,
    "Книга заклинаний: Ледяная стена": True,
    "Книга заклинаний: Огненная стрела": True,
    "Книга заклинаний: Грозовой удар": True,
    "Дневник Авеллы": False,
    "Журнал искателя приключений": False,
    "Записка Сибби": False,
    "Письмо от ярла": False,
    "Карта сокровищ": False,
    "Сундук с добычей": False,
    "Фляга с водой": True,
    "Чаша двемерская": True,
    "Козья шкура": True,
    "Мех волка": True,
    "Шкура саблезуба": True,
    "Шкура медведя": True,
    "Тролльский жир": True,
    "Ядовитый гриб": True,
    "Сахарная пыльца": True,
    "Броня Стражи Рассвета": False,
    "Арбалет": False,
    "Стеклянный кинжал": False,
    "Копьё рыбака": False,
    "Зачарованный эбонитовый меч": False,
    "Лук охотника": False,
    "Эльфийский лук": False,
    "Древний нордский лук": False,
    "Стальной арбалет": False,
    "Стрела двемерская": True,
    "Стрела эбонитовая": True,
    "Стрела даэдрическая": True,
    "Двемерское масло": True,
    "Стеклянный слиток": True,
    "Кровь вампира": True,
    "Слезы гиганта": True,
    "Ожерелье здоровья": False,
    "Ожерелье магии": False,
    "Зачарованный амулет": False,
    "Кольцо скрытности": False,
    "Плащ из меха саблезуба": False,
    "Череп тролля": False,
    "Череп мамонта": False
}

class Chest:
    def __init__(self):
        self.lock = False # Сундук закрыт или нет.
        self.code = 0 # Код для закрытия сундука.
        self.rarity = random.randint(1, 4) # Уровень редкости - 1: Редкий, 2: Эпический, 3: Мифический, 4: Легендарный.
        self.chest_items = {} # Предметы в сундуке.
        self.player_items = {} # Предметы игрока в инвентаре.

        if self.rarity == 4 or random.randint(1, 10) <= self.rarity + 5: # Определение шанса золота в сундуке в зависимости от редкости.
            self.chest_items['Золото'] = random.randint(8, 110) * self.rarity

        if self.rarity not in (1, 2) or random.randint(1, 10) <= self.rarity + 4: # Определение шанса предметов в сундуке в зависимости от редкости.
            count_items = random.randint(1, 3) * self.rarity # Кол-во предметов умножаем на редкость сундука.
            for i in range(count_items):
                temp_item = random.choice(list(all_items.items()))
                item_name, item_value = temp_item[0], temp_item[1]
                if item_name in self.chest_items:  # Проверяем, есть ли предмет в self.items
                    if item_value:  # Если предмет уже есть, проверяем умение стака предмета
                        new_value = random.randint(1, 4)
                        self.chest_items[item_name] += new_value * self.rarity  # Увеличиваем количество предмета
                else: # Если предмета нет, добавляем его в self.items
                    self.chest_items[item_name] = item_value
                    if item_value:  # Проверяем умение стака предмета
                        new_value = random.randint(1, 2)
                        self.chest_items[item_name] += (new_value * self.rarity) - 1 # Добавляем значение new_values

        if self.rarity not in (1, 2, 3) or random.randint(1, 10) <= self.rarity + 5: # Определение шанса того, что сундук будет закрыт, зависит от редкости.
            self.lock = True

    def pick_lock(self):
        if self.lock and self.code == 0:
            while True:
                random_number = random.randint(2, 6)
                open_number = random.randint(1, random_number)
                try:
                    number = int(input(f'Введите число для взлома замка от 1 до {random_number}:\t'))
                    if number < 1 or number > random_number:
                        print(f'Число должно быть от 1 до {random_number}, попробуйте ещё раз.')
                        continue
                    break
                except ValueError:
                    print('Вы ввели не число, попробуйте ещё раз.')
            if number == open_number:
                print('Замок взломан!')
                self.lock = False
            else:
                print('Замок не взломан, попробуйте ещё раз!')
        elif self.lock:
            while True:
                try:
                    number = int(input('Введите число для открытие сундука:\t'))
                except ValueError:
                    print('Не правильно введено число.')
                    continue
                if number == self.code:
                    print('Сундук открыт!')
                    self.lock = False
                    break
                else:
                    print('Сундук не открылся, попробуйте ещё раз!')
        else:
            print('Сундук был уже открыт!')

    def get_rarity(self):
        rarity_names = {1: 'редкий', 2: 'эпический', 3: 'мифический', 4: 'легендарный'}
        return rarity_names.get(self.rarity)

    def open_chest(self):
        if self.lock:
            print('Сундук закрыт. Взломайте его или откройте ключом!' if self.code == 0
                  else 'Сундук закрыт специальным ключом, надо открыть его!')
            return
        print(f'Сундук типа: {self.get_rarity()}, открывается...')
        if not self.chest_items:
            print('В этом сундуке ничего нет!')
        else:
            print('Вот что лежит в сундуке:')
            if self.chest_items:
                for item_name, item_value in self.chest_items.items():
                    if item_value is not False:
                        print(f'>\t{item_name} - {item_value} шт.')
                    else:
                        print(f'>\t{item_name}')

    def close_chest(self):
        if self.lock:
            print('Сундук закрыт. Взломайте его или откройте ключом!' if self.code == 0
                  else 'Сундук закрыт специальным ключом, надо открыть его!')
            return
        while True:
            try:
                number = int(input('Введите число для открытие замка, не меньше 1:\t'))
            except ValueError:
                print('Не правильно введено число.')
                continue
            if number > 0:
                print('Замок закрыт на ключ! Запомните его.')
                self.lock = True
                self.code = number
                break

    def get_item(self):
        if self.lock:
            print('Сундук закрыт. Взломайте его или откройте ключом!' if self.code == 0
                  else 'Сундук закрыт специальным ключом, надо открыть его!')
            return
        if self.chest_items == {}:
            print('Сундук пуст!')
            return
        item = input('Напишите название предмета в сундуке:\t')
        if item not in self.chest_items:
            print('Такого предмета нет в сундуке.')
            return
        if self.chest_items[item]:
            while True:
                try:
                    count = int(input('В каком количестве вы хотите взять этот тип предмета:\t'))
                except ValueError:
                    print('Не правильно введено число.')
                    continue
                if count <= 0:
                    print('Количество должно быть больше нуля.')
                    continue
                elif count > self.chest_items[item]:
                    print('Количество предмета превышает доступное.')
                    continue
                else:
                    self.player_items[item] = self.player_items.get(item, 0) + count
                    self.chest_items[item] -= count
                    if self.chest_items[item] == 0:
                        del self.chest_items[item]  # Удаляем предмет, если его количество стало нулевым
                    print(f'Предмет {item} в количестве {count} успешно взят!')
                    break
        else:
            self.player_items[item] = False
            del self.chest_items[item]
            print(f'Предмет {item} успешно взят!')

    def input_item(self):
        if self.lock:
            print('Сундук закрыт. Взломайте его или откройте ключом!' if self.code == 0
                  else 'Сундук закрыт специальным ключом, надо открыть его!')
            return
        if self.player_items == {}:
            print('Инвентарь игрока пуст!')
            return
        item = input('Напишите название предмета из вашего инвентаря:\t')
        if item not in self.player_items:
            print('Такого предмета нет в вашем инвентаре.')
            return
        if self.player_items[item]:
            while True:
                try:
                    count = int(input('В каком количестве вы хотите положить этот тип предмета в сундук:\t'))
                except ValueError:
                    print('Не правильно введено число.')
                    continue
                if count <= 0:
                    print('Количество должно быть больше нуля.')
                elif count > self.player_items[item]:
                    print('Количество предмета превышает доступное в вашем инвентаре.')
                else:
                    self.chest_items[item] = self.chest_items.get(item, 0) + count
                    self.player_items[item] -= count
                    if self.player_items[item] == 0:
                        del self.player_items[item]  # Удаляем предмет, если его количество стало нулевым
                    print(f'Предмет "{item}" в количестве {count} успешно положен в сундук!')
                    break
        else:
            self.chest_items[item] = False
            del self.player_items[item]
            print(f'Предмет "{item}" успешно взят!')

    def open_player_inventor(self):
        print(f'Инвентарь игрока открывается...')
        if not self.player_items:
            print('В инвентаре игрока ничего нет!')
        else:
            print('Вот что лежит в инвентаре игрока:')
            if self.player_items:
                for item_name, item_value in self.player_items.items():
                    if item_value is not False:
                        print(f'>\t{item_name} - {item_value} шт.')
                    else:
                        print(f'>\t{item_name}')