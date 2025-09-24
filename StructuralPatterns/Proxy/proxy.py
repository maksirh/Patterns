from abc import ABC, abstractmethod


class Image(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename

    def load_from_disk(self) -> None:
        print(f"Завантаження зображення {self.filename} з диска...")

    def display(self) -> None:
        print(f"Відображення зображення {self.filename}")


class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None

    def display(self) -> None:
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        else:
            print(f"(Proxy) Використовуємо вже завантажене зображення {self.filename}")
        self.real_image.display()


if __name__ == "__main__":

    image = ProxyImage("photo.png")

    print("Перше відображення:")
    image.display()

    print("Друге відображення:")
    image.display()
