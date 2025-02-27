import random


class Button:
    def __init__(self):
        self.hover = False  # Состояние "наводит курсор на кнопку"
        self.click = False  # Состояние "нажимает на кнопку"
        self.long_press = False  # Состояние "долгое нажатие"
        self.active = True  # Состояние "активности кнопки"
        self.success = True  # Состояние "успешного выполнения нажатия кнопки"
        self.count_click = 0  # Сколько была нажата кнопка

    def __random_success(self):
        if random.randint(1, 10) <= 8:
            self.success = True
        else:
            self.success = False

    def __tap_tap(self):
        if self.click and not self.long_press:
            self.__random_success()
            if self.success:
                print('Вы нажимаете на кнопку!')
                self.count_click += 1
            else:
                print('Что-то пошло не так!')
                self.active = False
        elif self.long_press and not self.click:
            while True:
                self.__random_success()
                if self.success:
                    self.count_click += 3
                    quest = input('Вы хотите отжать кнопку (да, нет)?\t')
                    if quest.lower() == 'да':
                        print('Вы отжали кнопку!')
                        break
                    elif quest.lower() == 'нет':
                        print('Вы, по какой-то причине, не захотели отжимать кнопку.')
                        continue
                    else:
                        print('Введите конкретный вариант ответа, выбранный из скобок.')
                        continue
                else:
                    print('Что-то пошло не так!')
                    self.active = False
                    break
        else:
            print('Кнопка была не в состояние нажатия или долгого нажатия.')

    def active_button(self):
        while True:
            if self.active:
                quest = input('Кнопка была уже активна, вы хотите её выключить (да, нет)?\t')
                if quest.lower() == 'да':
                    print('Вы выключили кнопку!')
                    self.active = False
                    break
                elif quest.lower() == 'нет':
                    print('Вы, по какой-то причине, не захотели выключать кнопку.')
                    break
                else:
                    print('Введите конкретный вариант ответа, выбранный из скобок')
                    continue
            else:
                quest = input('Вы точно хотите включить кнопку (да, нет)?\t')
                if quest.lower() == 'да':
                    print('Вы включили кнопку!')
                    self.active = True
                    break
                elif quest.lower() == 'нет':
                    print('Вы, по какой-то причине, не захотели выключать кнопку.')
                    break
                else:
                    print('Введите конкретный вариант ответа, выбранный из скобок')
                    continue

    def hover_over(self):
        while True:
            if self.hover:
                quest = input('Курсор был уже передвинут на кнопку, вы хотите убрать курсор с кнопки (да, нет)?\t')
                if quest.lower() == 'да':
                    print('Вы убрали курсор от кнопки!')
                    self.hover = False
                    break
                elif quest.lower() == 'нет':
                    print('Вы, по какой-то причине, не захотели передвигать курсор.')
                    break
                else:
                    print('Введите конкретный вариант ответа, выбранный из скобок')
                    continue
            else:
                quest = input('Вы точно хотите перенести курсор на кнопку (да, нет)?\t')
                if quest.lower() == 'да':
                    print('Вы передвинули курсор на кнопку!')
                    self.hover = True
                    break
                elif quest.lower() == 'нет':
                    print('Вы, по какой-то причине, не захотели передвигать курсор.')
                    break
                else:
                    print('Введите конкретный вариант ответа, выбранный из скобок')
                    continue

    def click_button(self):
        if not self.hover:
            print('Вы не навели курсор на кнопку!')
        elif not self.active:
            print('Кнопка не активна!')
        else:
            while True:
                print('Вы можете нажать на кнопку двумя способами:')
                print('(1) Обычное нажатие.')
                print('(2) Долгое нажатие')
                try:
                    quest = int(input('Как вы хотите нажать на кнопку?\t'))
                except ValueError:
                    print('Введено значение, которое не является числом.')
                    continue
                if quest == 1:
                    print('Вы нажали кнопку обычным способом!')
                    self.click = True
                    self.__tap_tap()
                    self.click = False
                    break
                elif quest == 2:
                    print('Вы решили зажать кнопку!')
                    self.long_press = True
                    self.__tap_tap()
                    self.long_press = False
                    break
                else:
                    print('Введите конкретный вариант ответа.')
                    continue

    def info_button(self):
        print(f'Вот сколько раз была нажата кнопка: {self.count_click}')
        print(f'Состояния самой кнопки:')
        if self.hover:
            print('Курсор был наведен на кнопку.')
        else:
            print('Курсор не был наведен на кнопку.')
        if self.active:
            print('Кнопка активна.')
        else:
            print('Кнопка не активна.')
            
