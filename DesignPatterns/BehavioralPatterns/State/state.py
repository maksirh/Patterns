from abc import ABC, abstractmethod


class VendingMachineState(ABC):
    @abstractmethod
    def insert_coin(self, machine):
        pass

    @abstractmethod
    def select_drink(self, machine):
        pass

    @abstractmethod
    def dispense(self, machine):
        pass


class WaitingForMoneyState(VendingMachineState):
    def insert_coin(self, machine):
        print("Монетка прийнята")
        machine.state = HasMoneyState()

    def select_drink(self, machine):
        print("Спочатку киньте монетку")

    def dispense(self, machine):
        print("Немає монетки")


class HasMoneyState(VendingMachineState):
    def insert_coin(self, machine):
        print("Вже є монетка")

    def select_drink(self, machine):
        print("Напиток обрано")
        machine.state = DispensingState()

    def dispense(self, machine):
        print("Спочатку оберіть напій")


class DispensingState(VendingMachineState):
    def insert_coin(self, machine):
        print("Зачекайте, видаємо напій")

    def select_drink(self, machine):
        print("Зачекайте, видаємо напій")

    def dispense(self, machine):
        print("Напій видано!")
        machine.state = WaitingForMoneyState()


class VendingMachine:
    def __init__(self):
        self.state = WaitingForMoneyState()

    def insert_coin(self):
        self.state.insert_coin(self)

    def select_drink(self):
        self.state.select_drink(self)

    def dispense_drink(self):
        self.state.dispense(self)




if __name__ == "__main__":

    machine = VendingMachine()

    machine.select_drink()
    machine.insert_coin()
    machine.select_drink()
    machine.dispense_drink()
