from typing import List, Dict


class ProductModel:

    def __init__(self):
        self.products = []
        self.next_id = 1

    def get_all_products(self) -> List[Dict]:
        return self.products.copy()

    def add_product(self, name: str, price: float) -> Dict:
        product = {
            'id': self.next_id,
            'name': name,
            'price': price
        }
        self.products.append(product)
        self.next_id += 1
        return product

    def delete_product(self, product_id: int) -> bool:
        for i, product in enumerate(self.products):
            if product['id'] == product_id:
                self.products.pop(i)
                return True
        return False



class ProductView:

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter) -> None:
        self.presenter = presenter

    def show_menu(self) -> None:
        print("\n" + "=" * 35)
        print("СИСТЕМА УПРАВЛІННЯ ПРОДУКТАМИ")
        print("=" * 35)
        print("1. Показати всі продукти")
        print("2. Додати продукт")
        print("3. Видалити продукт")
        print("0. Вийти")
        print("-" * 35)

    def get_user_choice(self) -> str:
        return input("Ваш вибір: ")

    def get_product_data(self) -> tuple:
        name = input("Назва продукту: ")
        try:
            price = float(input("Ціна: "))
            return name, price
        except ValueError:
            return name, 0.0

    def get_product_id(self) -> int:
        try:
            return int(input("ID продукту: "))
        except ValueError:
            return 0

    def show_products(self, products: List[Dict]) -> None:
        if not products:
            print("\n📭 Продуктів не знайдено")
            return

        print("\n📦 СПИСОК ПРОДУКТІВ:")
        for product in products:
            print(f"{product['id']}. {product['name']} - {product['price']}₴")

    def show_message(self, message: str) -> None:
        print(f"\n{message}")

    def show_error(self, error: str) -> None:
        print(f"\n{error}")


class ProductPresenter:

    def __init__(self, view: ProductView, model: ProductModel):
        self.view = view
        self.model = model
        self.view.set_presenter(self)

    def show_all_products(self) -> None:
        products = self.model.get_all_products()
        self.view.show_products(products)

    def add_product(self) -> None:
        name, price = self.view.get_product_data()

        if not name or price <= 0:
            self.view.show_error("Некоректні дані продукту")
            return

        product = self.model.add_product(name, price)
        self.view.show_message(f"Продукт '{product['name']}' додано!")
        self.show_all_products()

    def delete_product(self) -> None:
        product_id = self.view.get_product_id()

        if not product_id:
            self.view.show_error("Некоректний ID")
            return

        if self.model.delete_product(product_id):
            self.view.show_message("Продукт видалено!")
            self.show_all_products()
        else:
            self.view.show_error("Продукт не знайдено")


class ProductApp:

    def __init__(self):
        self.model = ProductModel()
        self.view = ProductView()
        self.presenter = ProductPresenter(self.view, self.model)

    def run(self) -> None:
        while True:
            self.view.show_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                self.presenter.show_all_products()
            elif choice == '2':
                self.presenter.add_product()
            elif choice == '3':
                self.presenter.delete_product()
            elif choice == '0':
                print("\nДо побачення!")
                break
            else:
                print("\nНевірний вибір!")


if __name__ == "__main__":
    print("ДЕМОНСТРАЦІЯ MVP ПАТЕРНУ")
    print("=" * 40)

    app = ProductApp()
    app.run()