from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def request(self) -> str:
        pass


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee


    def request(self) -> str:
        result = self.adaptee.specific_request()
        return result[::-1]


def client_code(target: Target) -> None:
    print(target.request())

if __name__ == '__main__':

    adaptee = Adaptee()
    print("Оригінал: ")
    print(adaptee.specific_request())

    adapter = Adapter(adaptee)
    print("Адаптований результат:")
    client_code(adapter)
