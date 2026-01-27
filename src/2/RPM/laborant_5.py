from __future__ import annotations
from abc import ABC, abstractmethod


class RemoteControl:
    def __init__(self, device: Device) -> None:
        self.device = device

    def turn_on(self) -> str:
        pass

    def turn_off(self) -> str:
        pass

    def change_volume(self, level: int) -> str:
        pass


class IRRemoteControl(RemoteControl):
    def turn_on(self) -> str:
        return f"Инфракрасный пульт: {self.device.turn_on()}"

    def turn_off(self) -> str:
        return f"Инфракрасный пульт: {self.device.turn_off()}"

    def change_volume(self, level: int) -> str:
        return f"Инфракрасный пульт: {self.device.change_volume(level)}"


class BluetoothRemoteControl(RemoteControl):
    def turn_on(self) -> str:
        return f"Bluetooth-пульт: {self.device.turn_on()}"

    def turn_off(self) -> str:
        return f"Bluetooth-пульт: {self.device.turn_off()}"

    def change_volume(self, level: int) -> str:
        return f"Bluetooth-пульт: {self.device.change_volume(level)}"


class Device(ABC):
    @abstractmethod
    def turn_on(self) -> str:
        pass

    @abstractmethod
    def turn_off(self) -> str:
        pass

    @abstractmethod
    def change_volume(self, level: int) -> str:
        pass


class Television(Device):
    def turn_on(self) -> str:
        return "Телевизор включён."

    def turn_off(self) -> str:
        return "Телевизор выключен."

    def change_volume(self, level: int) -> str:
        return f"Громкость телевизора установлена на {level}."


class Radio(Device):
    def turn_on(self) -> str:
        return "Радиоприёмник включён."

    def turn_off(self) -> str:
        return "Радиоприёмник выключен."

    def change_volume(self, level: int) -> str:
        return f"Громкость радиоприёмника установлена на {level}."


def client_code(remote: RemoteControl) -> None:
    print("---" * 10)
    print(remote.turn_on())
    print(remote.change_volume(5))
    print(remote.turn_off())
    print("---" * 10)


if __name__ == "__main__":
    tv = Television()
    ir_remote = IRRemoteControl(tv)
    print("Инфракрасный пульт + Телевизор:")
    client_code(ir_remote)

    radio = Radio()
    ir_remote_radio = IRRemoteControl(radio)
    print("Инфракрасный пульт + Радиоприёмник:")
    client_code(ir_remote_radio)

    bt_remote = BluetoothRemoteControl(tv)
    print("Bluetooth-пульт + Телевизор:")
    client_code(bt_remote)

    bt_remote_radio = BluetoothRemoteControl(radio)
    print("Bluetooth-пульт + Радиоприёмник:")
    client_code(bt_remote_radio)
