from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self, destination: str) -> str:
        pass


class Packaging(ABC):
    @abstractmethod
    def pack(self, item: str) -> str:
        pass


class Tracking(ABC):
    @abstractmethod
    def track(self, order_id: str) -> str:
        pass


class NovaPoshtaTransport(Transport):
    def deliver(self, destination: str) -> str:
        return f"NovaPoshta доставка до {destination}"


class NovaPoshtaPackaging(Packaging):
    def pack(self, item: str) -> str:
        return f"NovaPoshta упаковка для {item}"


class NovaPoshtaTracking(Tracking):
    def track(self, order_id: str) -> str:
        return f"NovaPoshta відстеження замовлення {order_id}"


class UkrPoshtaTransport(Transport):
    def deliver(self, destination: str) -> str:
        return f"UkrPoshta доставка до {destination}"


class UkrPoshtaPackaging(Packaging):
    def pack(self, item: str) -> str:
        return f"UkrPoshta упаковка для {item}"


class UkrPoshtaTracking(Tracking):
    def track(self, order_id: str) -> str:
        return f"UkrPoshta відстеження замовлення {order_id}"


class DHLTransport(Transport):
    def deliver(self, destination: str) -> str:
        return f"DHL міжнародна доставка до {destination}"


class DHLPackaging(Packaging):
    def pack(self, item: str) -> str:
        return f"DHL міжнародна упаковка для {item}"


class DHLTracking(Tracking):
    def track(self, order_id: str) -> str:
        return f"DHL міжнародне відстеження замовлення {order_id}"


class DeliveryFactory(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    @abstractmethod
    def create_packaging(self) -> Packaging:
        pass

    @abstractmethod
    def create_tracking(self) -> Tracking:
        pass

    def process_order(self, item: str, destination: str, order_id: str):
        packaging = self.create_packaging()
        transport = self.create_transport()
        tracking = self.create_tracking()

        print(packaging.pack(item))
        print(transport.deliver(destination))
        print(tracking.track(order_id))
        print("---")


class NovaPoshtaFactory(DeliveryFactory):
    def create_transport(self) -> Transport:
        return NovaPoshtaTransport()

    def create_packaging(self) -> Packaging:
        return NovaPoshtaPackaging()

    def create_tracking(self) -> Tracking:
        return NovaPoshtaTracking()


class UkrPoshtaFactory(DeliveryFactory):
    def create_transport(self) -> Transport:
        return UkrPoshtaTransport()

    def create_packaging(self) -> Packaging:
        return UkrPoshtaPackaging()

    def create_tracking(self) -> Tracking:
        return UkrPoshtaTracking()


class DHLFactory(DeliveryFactory):
    def create_transport(self) -> Transport:
        return DHLTransport()

    def create_packaging(self) -> Packaging:
        return DHLPackaging()

    def create_tracking(self) -> Tracking:
        return DHLTracking()


class DeliveryService:
    @staticmethod
    def get_factory(service_type: str) -> DeliveryFactory:
        if service_type.lower() == "novaposhta":
            return NovaPoshtaFactory()
        elif service_type.lower() == "ukrposhta":
            return UkrPoshtaFactory()
        elif service_type.lower() == "dhl":
            return DHLFactory()
        else:
            raise ValueError(f"Невідома служба доставки: {service_type}")


if __name__ == "__main__":
    print("=== СИСТЕМА ОБРОБКИ ЗАМОВЛЕНЬ ===\n")

    print("Замовлення через NovaPoshta:")
    nova_factory = DeliveryService.get_factory("novaposhta")
    nova_factory.process_order("Ноутбук", "Київ, вул. Хрещатик 1", "NP123456")

    print("Замовлення через UkrPoshta:")
    ukr_factory = DeliveryService.get_factory("ukrposhta")
    ukr_factory.process_order("Книги", "Львів, пл. Ринок 10", "UP789012")

    print("Міжнародне замовлення через DHL:")
    dhl_factory = DeliveryService.get_factory("dhl")
    dhl_factory.process_order("Електроніка", "Берлін, Германія", "DHL456789")