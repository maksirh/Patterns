from abc import ABC, abstractmethod



class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class Light:
    def on(self) -> None:
        print("Світло увімкнено")

    def off(self) -> None:
        print("Світло вимкнено")



class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.off()

    def undo(self) -> None:
        self.light.on()


class RemoteControl:
    def __init__(self):
        self.history: list[Command] = []

    def execute_command(self, command: Command) -> None:
        command.execute()
        self.history.append(command)

    def undo_last(self) -> None:
        if self.history:
            last = self.history.pop()
            print("Відкат останньої команди:")
            last.undo()
        else:
            print("Немає команд для відкату")


if __name__ == "__main__":

    light = Light()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    remote.execute_command(light_on)
    remote.execute_command(light_off)

    remote.undo_last()
    remote.undo_last()
    remote.undo_last()
