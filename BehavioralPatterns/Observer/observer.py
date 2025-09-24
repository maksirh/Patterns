from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(message)


class NewsPublisher(Subject):
    def publish_news(self, news: str):
        print(f"Новина: {news}")
        self.notify_observers(news)


class WeatherStation(Subject):
    def update_weather(self, temp: int, humidity: int):
        message = f"Погода: {temp}°C, вологість {humidity}%"
        self.notify_observers(message)


class PhoneApp(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f"{self.name}: {message}")


class TV(Observer):
    def update(self, message: str):
        print(f"Телевізор: {message}")


if __name__ == "__main__":

    news = NewsPublisher()
    weather = WeatherStation()

    phone1 = PhoneApp("Телефон Анни")
    phone2 = PhoneApp("Телефон Петра")
    tv = TV()

    news.add_observer(phone1)
    news.add_observer(tv)

    weather.add_observer(phone2)
    weather.add_observer(tv)

    news.publish_news("Python 3.12 вийшов!")
    weather.update_weather(25, 60)

    news.remove_observer(tv)
    news.publish_news("Новини про штучний інтелект")