from abc import ABC, abstractmethod


# Реалізація - інтерфейс для фарбування
class ColorImplementor(ABC):
    @abstractmethod
    def apply_color(self, color: str) -> str:
        pass


# Конкретні реалізації фарбування
class MetallicColor(ColorImplementor):
    def apply_color(self, color: str) -> str:
        return f"металік {color}"


class MatteColor(ColorImplementor):
    def apply_color(self, color: str) -> str:
        return f"мат {color}"



# Абстракція - автомобіль
class Car(ABC):
    def __init__(self, color_impl: ColorImplementor):
        self.color_impl = color_impl

    @abstractmethod
    def drive(self) -> str:
        pass

    def paint(self, color: str) -> str:
        applied_color = self.color_impl.apply_color(color)
        return f"Автомобіль пофарбовано в {applied_color}"


# Конкретні абстракції - типи автомобілів
class SportCar(Car):
    def drive(self) -> str:
        return "Спортивна машина швидко їде!"


class FamilyCar(Car):
    def drive(self) -> str:
        return "Сімейна машина комфортно їде"



if __name__ == "__main__":

    metallic = MetallicColor()
    matte = MatteColor()

    sport_car_metallic = SportCar(metallic)
    sport_car_matte = SportCar(matte)
    family_car_metallic = FamilyCar(metallic)

    print("1. Спортивне авто з металіком:")
    print(sport_car_metallic.paint("червоний"))
    print(sport_car_metallic.drive())

    print("\n2. Спортивне авто з матовим фарбуванням:")
    print(sport_car_matte.paint("синій"))
    print(sport_car_matte.drive())

    print("\n3. Сімейне авто з металіком:")
    print(family_car_metallic.paint("зелений"))
    print(family_car_metallic.drive())

    print("\n4. Зміна фарбування на льоту:")
    car = SportCar(metallic)
    print(car.paint("жовтий"))

    car.color_impl = matte
    print(car.paint("чорний"))