from abc import ABC, abstractmethod


class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass


class Warrior(GameCharacter):
    def attack(self) -> str:
        return "Воин атакует мечом! 💪"


class Mage(GameCharacter):
    def attack(self) -> str:
        return "Маг выпускает огненный шар! 🔥"


class Archer(GameCharacter):
    def attack(self) -> str:
        return "Лучник стреляет из лука! 🏹"


class CharacterFactory(ABC):
    @abstractmethod
    def create_character(self) -> GameCharacter:
        pass


class WarriorFactory(CharacterFactory):
    def create_character(self) -> GameCharacter:
        print('Создание персонажа Warrior!')
        return Warrior()


class MageFactory(CharacterFactory):
    def create_character(self) -> GameCharacter:
        print('Создание персонажа Mage!')
        return Warrior()


class ArcherFactory(CharacterFactory):
    def create_character(self) -> GameCharacter:
        print('Создание персонажа Archer!')
        return Archer()


if __name__ == "__main__":
    print("Добро пожаловать в игру! Выберите персонажа: warrior, mage или archer. 🎮")

    factories = {
        "warrior": WarriorFactory(),
        "mage": MageFactory(),
        "archer": ArcherFactory()
    }

    while True:
        choice = input("Ваш выбор: ").strip().lower()

        if choice in factories:
            factory = factories[choice]
            character = factory.create_character()
            print(f"Вы выбрали {choice.capitalize()}!")
            print(f"Способность: {character.attack()}")
            break
        else:
            print("Ошибка: Неизвестный тип персонажа. Попробуйте снова! 🤷‍♂️")
