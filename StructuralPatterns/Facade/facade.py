from typing import List, Dict


class MenuService:
    def get_menu(self) -> Dict[str, float]:
        return {
            "Піца Маргарита": 150.0,
            "Піца Пепероні": 180.0,
            "Бургер": 120.0,
            "Салат Цезар": 90.0,
            "Картопля фрі": 50.0,
            "Кока-кола": 25.0
        }

    def is_available(self, item: str) -> bool:
        return item not in ["Бургер"]  # Недоступні страви


class OrderValidator:
    def validate(self, items: List[str], menu: Dict[str, float]) -> bool:
        for item in items:
            if item not in menu:
                print(f"'{item}' відсутня в меню")
                return False
            if not MenuService().is_available(item):
                print(f"'{item}' недоступна")
                return False
        return True

    def get_total(self, items: List[str], menu: Dict[str, float]) -> float:
        return sum(menu[item] for item in items)


class PaymentProcessor:
    def pay(self, amount: float, method: str) -> bool:
        print(f"Оплата {amount} грн ({method})...")
        return amount > 0 and method in ["картка", "готівка", "онлайн"]


class KitchenService:
    def cook(self, items: List[str]) -> None:
        print("👨‍🍳 Готуємо:", ", ".join(items))


class DeliveryService:
    def deliver(self, address: str, items: List[str]) -> None:
        print(f"Доставка за адресою: {address}")


class NotificationSystem:
    def notify(self, phone: str, message: str) -> None:
        print(f"Сповіщення для {phone}: {message}")


class FoodOrderFacade:
    def __init__(self):
        self.menu = MenuService()
        self.validator = OrderValidator()
        self.payment = PaymentProcessor()
        self.kitchen = KitchenService()
        self.delivery = DeliveryService()
        self.notifier = NotificationSystem()

    def place_order(self, items: List[str], address: str, phone: str, payment_method: str) -> bool:
        print("\n🍕 Оформлення замовлення...")

        menu = self.menu.get_menu()
        if not self.validator.validate(items, menu):
            return False

        total = self.validator.get_total(items, menu)
        print(f"💰 Сума: {total} грн")

        if not self.payment.pay(total, payment_method):
            return False

        self.kitchen.cook(items)
        self.delivery.deliver(address, items)

        order_info = f"{', '.join(items)} - {total} грн"
        self.notifier.notify(phone, order_info)

        print("✅ Замовлення успішне!")
        return True


if __name__ == "__main__":
    service = FoodOrderFacade()

    service.place_order(
        ["Піца Маргарита", "Картопля фрі", "Кока-кола"],
        "вул. Центральна, 123",
        "+380501234567",
        "картка"
    )

    print("\n" + "=" * 40 + "\n")

    service.place_order(
        ["Бургер", "Салат Цезар"],
        "вул. Центральна, 123",
        "+380501234567",
        "готівка"
    )