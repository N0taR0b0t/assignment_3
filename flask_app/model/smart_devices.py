from abc import ABC, abstractmethod
import json

class SmartDevice(ABC):
    def __init__(self, name: str, manufacturer: str):
        self.__name = name
        self.__manufacturer = manufacturer

    @abstractmethod
    def to_json(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer

class LightBulb(SmartDevice):
    def __init__(self, name: str, manufacturer: str, brightness: int):
        super().__init__(name, manufacturer)
        self.__brightness = brightness

    def to_json(self):
        return json.dumps({
            'name': self.__name,
            'manufacturer': self.__manufacturer,
            'brightness': self.__brightness
        })

    def adjust_brightness(self, brightness: float):
        self.brightness = brightness

    @property
    def brightness(self):
        return self.__brightness
    @brightness.setter

    def brightness(self, brightness: float):
        self.__brightness = brightness
        print(f"Brightness is set to {brightness}")

class Home:
    def __init__(self, address: str):
        self.__address = address 
        self.__smart_devices = []

    def add_device(self, dev: SmartDevice):
        self.__smart_devices.append(dev)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def smart_devices(self):
        return self.__smart_devices

    def print_devices(self):
        for device in self.__smart_devices:
            print(device.to_json())
