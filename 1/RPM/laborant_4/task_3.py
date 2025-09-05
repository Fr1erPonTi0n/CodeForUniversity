class Device:
    def __init__(self, power):
        self.power = power

    def turn_on(self):
        print(f"Включение устройства с мощностью {self.power}")


class NetworkedDevice(Device):
    def __init__(self, power, ip_address):
        Device.__init__(self, power)
        self.ip_address = ip_address

    def connect(self):
        print(f"Подключение к сети с IP-адресом {self.ip_address}")

    def turn_on(self):
        print(f"Включение сетевого устройства с мощностью {self.power}")


class PortableDevice(Device):
    def __init__(self, power, battery_level):
        Device.__init__(self, power)
        self.battery_level = battery_level

    def charge(self):
        print(f"Зарядка устройства с уровнем батареи {self.battery_level}")

    def turn_on(self):
        print(f"Включение портативного устройства с мощностью {self.power}")


class SmartPhone(NetworkedDevice, PortableDevice):
    def __init__(self, power, ip_address, battery_level):
        NetworkedDevice.__init__(self, power, ip_address)
        PortableDevice.__init__(self, power, battery_level)

    def turn_on(self):
        print("Включение смартфона:")
        NetworkedDevice.turn_on(self)
        PortableDevice.turn_on(self)

    def call(self):
        print("Совершение телефонного звонка")


smartphone = SmartPhone(power=50, ip_address="192.168.1.100", battery_level=80)
smartphone.turn_on()
smartphone.connect()
smartphone.charge()
smartphone.call()
