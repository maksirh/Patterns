from abc import ABC, abstractmethod


class Game(ABC):

    def play(self) -> None:
        self.initialize()
        self.start_play()
        self.end_play()

    def initialize(self) -> None:
        print("Гра ініціалізована")

    @abstractmethod
    def start_play(self) -> None:
        pass

    def end_play(self) -> None:
        print("Гра завершена\n")


class Chess(Game):

    def start_play(self) -> None:
        print("Початок гри в шахи")
        print("Грають білі та чорні фігури")


class Monopoly(Game):

    def start_play(self) -> None:
        print("Початок гри в монополію")
        print("Гравці кидають кубики")

    def end_play(self) -> None:
        print("Гра в монополію завершена")
        print("Переможець отримує всі гроші!\n")


if __name__ == "__main__":

    chess = Chess()
    chess.play()

    monopoly = Monopoly()
    monopoly.play()