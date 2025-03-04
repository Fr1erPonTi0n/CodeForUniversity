from chest import Chest
from button import Button
from pet import Pet


def chest():
    exam = Chest()
    print(f"Вы видите сундук типа: {exam.get_rarity()}.")
    while True:
        print()
        print("Что вы хотите c ним сделать?")
        print("(1) Попытаться открыть сундук.")
        print("(2) Открыть сундук или вскрыть сундук.")
        print('(3) Закрыть на ключ сундук.')
        print("(4) Взять предмет из сундука.")
        print("(5) Уйти.")
        try:
            choice_chest = int(input(">\t"))
        except ValueError:
            print('Введено значение, которое не является числом.')
            continue
        print()
        if choice_chest == 1:
            exam.open_chest()
        elif choice_chest == 2:
            exam.pick_lock(input('Введите число:\n>\t'))
        elif choice_chest == 3:
            exam.close_chest(input('Введите число для открытие замка:\n>\t'))
        elif choice_chest == 4:
            get_items = exam.get_item(input('Напишите название предмета в сундуке:\n>\t'))
            if get_items:
                print(f'Предмет {get_items[0]} в количестве {get_items[1]} успешно взят!' if get_items[1] else
                      f'Предмет {get_items[0]} успешно взят!')
        elif choice_chest == 5:
            print('Ты уходишь от сундука, удачного приключения!')
            print()
            return

        else:
            print('Ты ввёл неправильное число!')


def button():
    exam = Button()
    print(f"Вы видите кнопку.")
    while True:
        print()
        print("Что вы хотите c ней сделать?")
        print("(1) Попытаться нажать на кнопку.")
        print("(2) Навести курсор на кнопку.")
        print('(3) Включить или выключить кнопку.')
        print("(4) Посмотреть состояние кнопки")
        print("(5) Выключить браузер с кнопкой.")
        try:
            choice_button = int(input(">\t"))
        except ValueError:
            print('Введено значение, которое не является числом.')
            continue
        print()
        if choice_button == 1:
            exam.click_button()
        elif choice_button == 2:
            exam.hover_over()
        elif choice_button == 3:
            exam.active_button()
        elif choice_button == 4:
            exam.info_button()
        elif choice_button == 5:
            print('Ты выключаешь браузер с кнопкой!')
            print()
            return
        else:
            print('Ты ввёл неправильное число!')


def pet():
    print('Вы входите в комнату...')
    print(f"И вы видите питомца, у вас появилось огромное желание за ним ухаживать.")
    name = input('Как вы назовете своего питомца?\t')
    exam = Pet(name)
    while True:
        print()
        print(f"У вас есть питомец по имени {name}. Что вы хотите c ним сделать?")
        print(f"(1) Узнать состояние {name}.")
        print(f"(2) Покормить {name}.")
        print(f'(3) Поиграть с {name}.')
        print(f"(4) Уложить спать {name}.")
        print(f"(5) Разбудить {name}.")
        print("(6) Уйти.")
        try:
            choice_pet = int(input(">\t"))
        except ValueError:
            print('Введено значение, которое не является числом.')
            continue
        print()
        if choice_pet == 1:
            exam.info_status()
        elif choice_pet == 2:
            exam.feed()
        elif choice_pet == 3:
            exam.play()
        elif choice_pet == 4:
            exam.sleep()
        elif choice_pet == 5:
            exam.wake_up()
        elif choice_pet == 6:
            if exam.is_alive():
                print(f'Ты покидаешь комнату оставляя мертвого {name}...')
            else:
                print(f'Ты покидаешь комнату оставляя {name}!')
            print()
            return
        else:
            print('Ты ввёл неправильное число!')


if __name__ == "__main__":
    while True:
        print('Какой класс запустить?')
        print('(1) Класс сундук')
        print('(2) Класс кнопка')
        print('(3) Класс питомец')
        print('(4) Выход')
        try:
            choice = int(input(">\t"))
        except ValueError:
            print('Введено значение, которое не является числом.')
            continue
        print()
        if choice == 1:
            chest()
        elif choice == 2:
            button()
        elif choice == 3:
            pet()
        elif choice == 4:
            print('Выход из программы')
            break
        else:
            print('Ты ввёл неправильное число!')
