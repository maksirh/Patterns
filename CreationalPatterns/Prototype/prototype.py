from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self): pass


class PhonePrototype(Prototype):

    def clone(self):

        new_brand = self.brand
        new_model = self.model
        new_os = self.os
        new_features = []

        for feature in self.features:
            new_features.append(feature)

        return Phone(new_brand, new_model, new_os, new_features)


class Phone(PhonePrototype):

    def __init__(self, brand, model, os, features=None):
        self.brand = brand
        self.model = model
        self.os = os
        self.features = features if features else []

    def add_feature(self, feature):
        self.features.append(feature)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.os}) with features: {', '.join(self.features)}"



if __name__ == "__main__":
    # Оригінал
    phone1 = Phone("Samsung", "Galaxy S24", "Android", ["Camera", "Bluetooth", "5G"])
    print("Original:", phone1)

    # Клон з додатковими змінами
    phone2 = phone1.clone()
    phone2.model = "Galaxy S24 Pro"
    phone2.add_feature("Stylus")

    print("Clone:", phone2)
    print("Original after clone:", phone1)


