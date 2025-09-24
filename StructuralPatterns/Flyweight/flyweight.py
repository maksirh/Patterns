from typing import Dict
from enum import Enum


class WeaponType(Enum):
    SWORD = "меч"
    BOW = "лук"
    STAFF = "посох"
    DAGGER = "кинжал"


class WeaponStats:
    def __init__(self, weapon_type: WeaponType, damage: int, speed: float, range: int):
        self.weapon_type = weapon_type
        self.damage = damage
        self.speed = speed
        self.range = range

    def show(self, owner: str, level: int) -> None:
        print(f"{owner} ({level}р.): {self.weapon_type.value} - {self.damage}дмг, {self.speed}спд, {self.range}дст")


class WeaponFactory:
    cache: Dict[WeaponType, WeaponStats] = {}

    @classmethod
    def get_stats(cls, weapon_type: WeaponType) -> WeaponStats:
        if weapon_type not in cls.cache:
            stats_config = {
                WeaponType.SWORD: (50, 1.0, 1),
                WeaponType.BOW: (30, 1.5, 5),
                WeaponType.STAFF: (40, 0.8, 3),
                WeaponType.DAGGER: (25, 2.0, 1)
            }
            damage, speed, range = stats_config[weapon_type]
            cls.cache[weapon_type] = WeaponStats(weapon_type, damage, speed, range)
            print(f"Створено {weapon_type.value}")

        return cls.cache[weapon_type]


class Weapon:
    def __init__(self, owner: str, weapon_type: WeaponType, level: int = 1):
        self.owner = owner
        self.level = level
        self.stats = WeaponFactory.get_stats(weapon_type)

    def show(self) -> None:
        self.stats.show(self.owner, self.level)

    def upgrade(self) -> None:
        self.level += 1
        print(f"⬆{self.owner} тепер {self.level} рівень")


class Game:
    def __init__(self):
        self.weapons = []

    def add_weapon(self, owner: str, weapon_type: WeaponType, level: int = 1) -> None:
        self.weapons.append(Weapon(owner, weapon_type, level))

    def show_all(self) -> None:
        print("\n Вся зброя:")
        for weapon in self.weapons:
            weapon.show()

    def stats(self) -> None:
        print(f"\nСтатистика:")
        print(f"Зброї: {len(self.weapons)}")
        print(f"Типів: {len(WeaponFactory.cache)}")


if __name__ == "__main__":
    game = Game()

    warriors = [
        ("Воїн", WeaponType.SWORD, 5),
        ("Лучник", WeaponType.BOW, 3),
        ("Маг", WeaponType.STAFF, 7),
        ("Злодій", WeaponType.DAGGER, 4),
        ("Воїн2", WeaponType.SWORD, 2),
        ("Лучник2", WeaponType.BOW, 6),
        ("Новачок", WeaponType.SWORD, 1)
    ]

    for owner, w_type, level in warriors:
        game.add_weapon(owner, w_type, level)

    game.show_all()
    game.stats()

    game.weapons[0].upgrade()
    game.weapons[0].show()