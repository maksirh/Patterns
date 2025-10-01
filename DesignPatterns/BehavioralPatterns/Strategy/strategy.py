from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, start: str, end: str) -> None:
        pass


class CarRoute(RouteStrategy):
    def build_route(self, start: str, end: str) -> None:
        print(f"Маршрут на авто: {start} → {end}")


class WalkingRoute(RouteStrategy):
    def build_route(self, start: str, end: str) -> None:
        print(f"Піший маршрут: {start} → {end}")


class PublicTransportRoute(RouteStrategy):
    def build_route(self, start: str, end: str) -> None:
        print(f"Маршрут транспортом: {start} → {end}")


class NavigationApp:
    def __init__(self):
        self.strategy = None

    def set_route_strategy(self, strategy: RouteStrategy):
        self.strategy = strategy

    def navigate(self, start: str, end: str):
        if self.strategy:
            self.strategy.build_route(start, end)
        else:
            print("Не обрано тип маршруту")


if __name__ == "__main__":
    navigator = NavigationApp()

    navigator.set_route_strategy(CarRoute())
    navigator.navigate("Київ", "Львів")

    navigator.set_route_strategy(WalkingRoute())
    navigator.navigate("вул. Шевченка", "пл. Ринок")

    navigator.set_route_strategy(PublicTransportRoute())
    navigator.navigate("Залізничний вокзал", "Аеропорт")