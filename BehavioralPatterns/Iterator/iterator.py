from typing import List, Iterator


class Book:
    def __init__(self, title: str):
        self.title = title

    def __str__(self) -> str:
        return f"{self.title}"


class BookIterator(Iterator):
    def __init__(self, books: List[Book]):
        self.books = books
        self.index = 0

    def __next__(self) -> Book:
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def __iter__(self) -> BookIterator:
        return BookIterator(self.books)


if __name__ == "__main__":

    library = Library()
    library.add_book(Book("Гаррі Поттер"))
    library.add_book(Book("Володар Перснів"))
    library.add_book(Book("Майстер і Маргарита"))

    print("Перегляд бібліотеки за допомогою for:")
    for book in library:
        print(book)

    print("Перегляд вручну через next():")
    iterator = iter(library)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        print("Книги закінчились")
