from abc import ABC, abstractmethod



class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler: "Handler") -> "Handler":
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> None:
        if self.next_handler:
            self.next_handler.handle(request)


# Конкретні обробники
class Level1Support(Handler):
    def handle(self, request: str) -> None:
        if request == "пароль":
            print("Level 1: Допомога з відновленням паролю")
        else:
            super().handle(request)


class Level2Support(Handler):
    def handle(self, request: str) -> None:
        if request == "помилка програми":
            print("Level 2: Аналіз та виправлення помилки")
        else:
            super().handle(request)


class Level3Support(Handler):
    def handle(self, request: str) -> None:
        if request == "сервер впав":
            print("Level 3: Відновлення сервера!")
        else:
            print(f"Запит '{request}' не може бути оброблений")



if __name__ == "__main__":
    print("=== Паттерн Chain of Responsibility Demo ===\n")

    l1 = Level1Support()
    l2 = Level2Support()
    l3 = Level3Support()

    l1.set_next(l2).set_next(l3)

    requests = ["пароль", "помилка програми", "сервер впав", "дизайн сайту"]

    for r in requests:
        print(f"Запит: {r}")
        l1.handle(r)
