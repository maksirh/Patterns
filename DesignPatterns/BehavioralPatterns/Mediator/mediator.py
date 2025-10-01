

class Flight:
    def __init__(self, flight_id: str, seats: int):
        self.flight_id = flight_id
        self.seats = seats
        self.available_seats = seats
        self.passengers = []

    def book_seat(self, passenger: str) -> bool:
        if self.available_seats > 0:
            self.available_seats -= 1
            self.passengers.append(passenger)
            return True
        return False

    def cancel_booking(self, passenger: str) -> bool:
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            self.available_seats += 1
            return True
        return False


class BookingMediator:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight: Flight) -> None:
        self.flights[flight.flight_id] = flight
        print(f"Додано рейс {flight.flight_id}")

    def book_flight(self, flight_id: str, passenger: str) -> bool:
        if flight_id not in self.flights:
            print(f"Рейс {flight_id} не знайдено")
            return False

        flight = self.flights[flight_id]
        if flight.book_seat(passenger):
            print(f"{passenger} забронював {flight_id}")
            return True
        else:
            print(f"Немає місць на рейс {flight_id}")
            return False

    def cancel_booking(self, flight_id: str, passenger: str) -> bool:
        if flight_id not in self.flights:
            return False

        flight = self.flights[flight_id]
        if flight.cancel_booking(passenger):
            print(f"{passenger} скасував {flight_id}")
            return True
        return False

    def get_flight_info(self, flight_id: str) -> str:
        if flight_id in self.flights:
            flight = self.flights[flight_id]
            return f"{flight_id}: {flight.available_seats}/{flight.seats}"
        return "Рейс не знайдено"


class Passenger:
    def __init__(self, name: str, mediator: BookingMediator):
        self.name = name
        self.mediator = mediator

    def book(self, flight_id: str) -> bool:
        return self.mediator.book_flight(flight_id, self.name)

    def cancel(self, flight_id: str) -> bool:
        return self.mediator.cancel_booking(flight_id, self.name)

    def check_flight(self, flight_id: str) -> None:
        info = self.mediator.get_flight_info(flight_id)
        print(f"{self.name}: {info}")


if __name__ == "__main__":
    mediator = BookingMediator()

    mediator.add_flight(Flight("UA123", 2))
    mediator.add_flight(Flight("LH456", 1))

    passengers = [
        Passenger("Анна", mediator),
        Passenger("Богдан", mediator),
        Passenger("Катя", mediator)
    ]

    passengers[0].book("UA123")
    passengers[1].book("UA123")
    passengers[2].book("UA123")

    passengers[0].book("LH456")
    passengers[1].book("LH456")

    for p in passengers:
        p.check_flight("UA123")

    passengers[0].cancel("UA123")
    passengers[2].book("UA123")