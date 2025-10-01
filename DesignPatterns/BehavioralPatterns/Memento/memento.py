from typing import List


class EditorMemento:
    def __init__(self, text: str):
        self.text = text


class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, words: str) -> None:
        self.text += words
        print(f"Текст: {self.text}")

    def save(self) -> EditorMemento:
        return EditorMemento(self.text)

    def restore(self, memento: EditorMemento) -> None:
        self.text = memento.text
        print(f"Відновлено: {self.text}")


class History:
    def __init__(self):
        self.states: List[EditorMemento] = []

    def push(self, memento: EditorMemento) -> None:
        self.states.append(memento)

    def pop(self) -> EditorMemento:
        return self.states.pop()




if __name__ == "__main__":

    editor = TextEditor()
    history = History()

    editor.write("Привіт")
    history.push(editor.save())

    editor.write(" світ")
    history.push(editor.save())

    editor.write("!")
    print(f"Поточний текст: {editor.text}")

    editor.restore(history.pop())
    editor.restore(history.pop())

