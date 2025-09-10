from random import randint, choice


class SmartHomeFacade:

    """
    Класс Фасада предоставляет простой интерфейс для сложной логики одной или
    нескольких подсистем. Фасад делегирует запросы клиентов соответствующим
    объектам внутри подсистемы. Фасад также отвечает за управление их жизненным
    циклом. Все это защищает клиента от нежелательной сложности подсистемы.
    """

    def __init__(self) -> None:

        self._ligsystem = LightingSystem()
        self._tempsystem = TemperatureSystem()
        self._secursystem = SecuritySystem()

    """
    Методы Фасада удобны для быстрого доступа к сложной функциональности
    подсистем. Однако клиенты получают только часть возможностей подсистемы.
    """

    def on_smart_home(self) -> str:

        results = ["--- Включение умного дома... ---",
                   self._ligsystem.on_lighting(),
                   self._tempsystem.on_temperature(),
                   self._secursystem.on_security(),
                   "--- Умный дом: включен! ---"
                   ]
        return "\n".join(results)

    def off_smart_home(self) -> str:
        results = ["--- Выключение умного дома... ---",
                   self._ligsystem.off_lighting(),
                   self._tempsystem.off_temperature(),
                   self._secursystem.off_securiy(),
                   "--- Умный дом: выключен! ---"
                   ]
        return "\n".join(results)

    def check_smart_home(self) -> str:
        results = ["--- Проверка состояния умного дома... ---",
                   self._ligsystem.check_lighting(),
                   self._tempsystem.check_temperature(),
                   self._secursystem.check_security(),
                   "--- Завершение состояние проверки умного дома! ---"
                   ]
        return "\n".join(results)


""" 
Подсистема может принимать запросы либо от фасада, либо от клиента напрямую.
В любом случае, для Подсистемы Фасад – это ещё один клиент, и он не является
частью Подсистемы.
Некоторые фасады могут работать с разными подсистемами одновременно.
"""


class LightingSystem:
    def __init__(self):
        self._enable = False

    def on_lighting(self) -> str:
        self._enable = True
        return "Система управления светом: включена!"

    def off_lighting(self) -> str:
        self._enable = False
        return "Система управления светом: выключена!"

    def check_lighting(self) -> str:
        if self._enable:
            return "Система управления светом была включена!"
        return "Система управления светом была выключена!"


class TemperatureSystem:
    def __init__(self):
        self._enable = False

    def on_temperature(self) -> str:
        self._enable = True
        return "Система отслеживание температуры: включена!"

    def off_temperature(self) -> str:
        self._enable = False
        return "Система отслеживание температуры: выключена!"

    def check_temperature(self) -> str:
        if self._enable:
            return f"Система отслеживание температуры была включена! Температура дома: {randint(16, 35)}."
        return "Система отслеживание температуры была выключена!"


class SecuritySystem:
    def __init__(self):
        self._enable = False

    def on_security(self) -> str:
        self._enable = True
        return "Система безопасности: включена!"

    def off_securiy(self) -> str:
        self._enable = False
        return "Система безопасности: включена!"

    def check_security(self) -> str:
        if self._enable:
            return f"Система безопасности была включена! В доме {choice(['есть', 'нету'])} сторонние люди."
        return "Система безопасности была выключена!"


if __name__ == "__main__":
    # Пример работы паттерна Фасада клиентским кодом. Включение и выключение умного дома
    facade = SmartHomeFacade()
    print(facade.check_smart_home())
    print(facade.on_smart_home())
    print(facade.check_smart_home())
    print(facade.off_smart_home())
    print(facade.check_smart_home())
