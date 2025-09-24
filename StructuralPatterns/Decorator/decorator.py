from abc import ABC, abstractmethod


# Базовий компонент
class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass


class Coffee(Beverage):
    def get_description(self) -> str:
        return "Кава"

    def cost(self) -> float:
        return 25.0


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        pass



class MilkDecorator(CondimentDecorator):
    def get_description(self) -> str:
        return self.beverage.get_description() + ", молоко"

    def cost(self) -> float:
        return self.beverage.cost() + 5.0


class SugarDecorator(CondimentDecorator):
    def get_description(self) -> str:
        return self.beverage.get_description() + ", цукор"

    def cost(self) -> float:
        return self.beverage.cost() + 2.0



class WhippedCreamDecorator(CondimentDecorator):
    def get_description(self) -> str:
        return self.beverage.get_description() + ", збиті вершки"

    def cost(self) -> float:
        return self.beverage.cost() + 7.0


if __name__ == "__main__":

    coffee = Coffee()
    print(f"{coffee.get_description()}: {coffee.cost()} грн")

    coffee_with_milk_and_sugar = SugarDecorator(MilkDecorator(Coffee()))
    print(f"{coffee_with_milk_and_sugar.get_description()}: {coffee_with_milk_and_sugar.cost()} грн")

    combinations = [
        Coffee(),
        MilkDecorator(Coffee()),
        SugarDecorator(Coffee()),
        WhippedCreamDecorator(SugarDecorator(Coffee()))
    ]

    print("Усі комбінації")
    for i, beverage in enumerate(combinations, 1):
        print(f"{i}. {beverage.get_description()} - {beverage.cost()} грн")

