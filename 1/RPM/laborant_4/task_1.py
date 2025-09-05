class Vehicle:
    def __init__(self, max_speed, fuel_type):
        self.max_speed = max_speed
        self.fuel_type = fuel_type

    @staticmethod
    def start_engine():
        print('Двигатель запущен.')


class WheeledVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, wheel_count):
        Vehicle.__init__(self, max_speed, fuel_type)
        self.wheel_count = wheel_count

    @staticmethod
    def check_tires():
        print('Проверка шин')


class CargoTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, cargo_capacity):
        Vehicle.__init__(self, max_speed, fuel_type)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, weight):
        if weight <= self.cargo_capacity:
            print(f"Загружено {weight} кг груза.")
        else:
            print(f"Превышена грузоподъемность!")


class PassengerTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, passenger_capacity):
        Vehicle.__init__(self, max_speed, fuel_type)
        self.passenger_capacity = passenger_capacity

    def board_passengers(self, passengers):
        if passengers <= self.passenger_capacity:
            print(f"Посажено {passengers} пассажиров.")
        else:
            print(f"Превышена вместимость!")

class HeavyDutyVehicle(WheeledVehicle, CargoTransport):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight):
        WheeledVehicle.__init__(self, max_speed, fuel_type, wheel_count)
        CargoTransport.__init__(self, max_speed, fuel_type, cargo_capacity)
        self.max_weight = max_weight

    @staticmethod
    def reinforce_frame(self):
        print(f"Усиление рамы...")


class EcoFriendlyVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, emission_level):
        Vehicle.__init__(self, max_speed, fuel_type)  # Явный вызов конструктора Vehicle
        self.emission_level = emission_level

    def reduce_emission(self):
        print(f"Снижение выбросов до уровня {self.emission_level}.")


class HybridDeliveryVan(HeavyDutyVehicle, PassengerTransport, EcoFriendlyVehicle):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight, passenger_capacity,
                 emission_level):
        HeavyDutyVehicle.__init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight)
        PassengerTransport.__init__(self, max_speed, fuel_type, passenger_capacity)
        EcoFriendlyVehicle.__init__(self, max_speed, fuel_type, emission_level)

    def status(self):
        print(
            f"Гибридный фургон: Скорость: {self.max_speed}, Топливо: {self.fuel_type}, Колеса: {self.wheel_count}, "
            f"Грузоподъемность: {self.cargo_capacity}кг, Максимальный вес: {self.max_weight}кг, "
            f"Пассажиры: {self.passenger_capacity}, Выбросы: {self.emission_level}."
        )
