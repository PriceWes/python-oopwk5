#ACTIVITY 1
# Base class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device: {self.brand} {self.model}"


# Derived class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage

    def device_info(self):
        return f"Smartphone: {self.brand} {self.model}, OS: {self.os}, Storage: {self.storage}GB"

    def make_call(self, number):
        return f"Calling {number} from {self.model}..."


# Derived class: Laptop
class Laptop(Device):
    def __init__(self, brand, model, processor, ram):
        super().__init__(brand, model)
        self.processor = processor
        self.ram = ram

    def device_info(self):
        return f"Laptop: {self.brand} {self.model}, Processor: {self.processor}, RAM: {self.ram}GB"

    def code(self):
        return f"Coding on {self.model} with {self.processor} processor."


#usage
smartphone = Smartphone("Apple", "iPhone 14", "iOS", 128)
laptop = Laptop("Dell", "XPS 15", "Intel i7", 16)

print(smartphone.device_info())
print(smartphone.make_call("123-456-7890"))
print(laptop.device_info())
print(laptop.code())


#ACTIVITY 2
# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Derived class: Car
class Car(Vehicle):
    def move(self):
        return "Driving "


# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying "


# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing "


# Example usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
