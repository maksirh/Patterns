from abc import ABC, abstractmethod


class Pizza():

    def __init__(self):
        self.parts = []

    def add_part(self, part: str):
        self.parts.append(part)

    def __str__(self):
        return f"Pizza with: {', '.join(self.parts)}"



class PizzaBuilder(ABC):

    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def add_dough(self): pass

    @abstractmethod
    def add_sauce(self): pass

    @abstractmethod
    def add_topping(self): pass

    def get_pizza(self):
        return self.pizza


# --- Конкретні Builder-и ---
class MargheritaBuilder(PizzaBuilder):
    def add_dough(self):
        self.pizza.add_part("thin dough")

    def add_sauce(self):
        self.pizza.add_part("tomato sauce")

    def add_topping(self):
        self.pizza.add_part("mozzarella")
        self.pizza.add_part("basil")


class PepperoniBuilder(PizzaBuilder):
    def add_dough(self):
        self.pizza.add_part("thick dough")

    def add_sauce(self):
        self.pizza.add_part("tomato sauce")

    def add_topping(self):
        self.pizza.add_part("pepperoni")
        self.pizza.add_part("cheese")


class Chef:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def cook_pizza(self):
        self.builder.add_dough()
        self.builder.add_sauce()
        self.builder.add_topping()
        return self.builder.get_pizza()


if __name__ == "__main__":
    chef = Chef(MargheritaBuilder())
    pizza1 = chef.cook_pizza()
    print(pizza1)

    chef = Chef(PepperoniBuilder())
    pizza2 = chef.cook_pizza()
    print(pizza2)