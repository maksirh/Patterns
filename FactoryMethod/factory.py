from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        return "Їдемо на автомобілі"


class Bike(Vehicle):
    def drive(self):
        return "Їдемо на велосипеді"


class Truck(Vehicle):
    def drive(self):
        return "Їдемо на вантажівці"



class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

    def deliver_vehicle(self):
        vehicle = self.create_vehicle()
        result = vehicle.drive()
        print(f"Доставка: {result}")


class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()


class BikeFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Bike()


class TruckFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Truck()


def client_code(factory: VehicleFactory):
    factory.deliver_vehicle()


if __name__ == "__main__":
    print("Створення автомобіля:")
    client_code(CarFactory())

    print("\nСтворення велосипеда:")
    client_code(BikeFactory())

    print("\nСтворення вантажівки:")
    client_code(TruckFactory())