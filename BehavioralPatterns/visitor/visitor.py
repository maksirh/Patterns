from abc import ABC, abstractmethod
from typing import List



class DocumentElement(ABC):
    @abstractmethod
    def accept(self, visitor: 'DocumentVisitor') -> None:
        pass


class Paragraph(DocumentElement):
    def __init__(self, text: str):
        self.text = text

    def accept(self, visitor: 'DocumentVisitor') -> None:
        visitor.visit_paragraph(self)


class Image(DocumentElement):
    def __init__(self, filename: str):
        self.filename = filename

    def accept(self, visitor: 'DocumentVisitor') -> None:
        visitor.visit_image(self)


class Table(DocumentElement):
    def __init__(self, data: List[List[str]]):
        self.data = data

    def accept(self, visitor: 'DocumentVisitor') -> None:
        visitor.visit_table(self)



class DocumentVisitor(ABC):
    @abstractmethod
    def visit_paragraph(self, paragraph: Paragraph) -> None:
        pass

    @abstractmethod
    def visit_image(self, image: Image) -> None:
        pass

    @abstractmethod
    def visit_table(self, table: Table) -> None:
        pass


class WordCountVisitor(DocumentVisitor):
    def __init__(self):
        self.total_words = 0

    def visit_paragraph(self, paragraph: Paragraph) -> None:
        words = len(paragraph.text.split())
        self.total_words += words

    def visit_image(self, image: Image) -> None:
        pass

    def visit_table(self, table: Table) -> None:
        for row in table.data:
            for cell in row:
                self.total_words += len(cell.split())


class ExportVisitor(DocumentVisitor):
    def visit_paragraph(self, paragraph: Paragraph) -> None:
        print(f"<p>{paragraph.text}</p>")

    def visit_image(self, image: Image) -> None:
        print(f'<img src="{image.filename}">')

    def visit_table(self, table: Table) -> None:
        print("<table>")
        for row in table.data:
            print("  <tr>")
            for cell in row:
                print(f"    <td>{cell}</td>")
            print("  </tr>")
        print("</table>")


class Document:
    def __init__(self):
        self.elements: List[DocumentElement] = []

    def add(self, element: DocumentElement) -> None:
        self.elements.append(element)

    def accept(self, visitor: DocumentVisitor) -> None:
        for element in self.elements:
            element.accept(visitor)


if __name__ == "__main__":
    document = Document()
    document.add(Paragraph("Це перший параграф."))
    document.add(Image("photo.jpg"))
    document.add(Table([["A", "B"], ["C", "D"]]))
    document.add(Paragraph("Це другий параграф з текстом."))

    word_counter = WordCountVisitor()
    document.accept(word_counter)
    print(f"Загальна кількість слів: {word_counter.total_words}")

    print("\nЕкспорт у HTML:")
    exporter = ExportVisitor()
    document.accept(exporter)