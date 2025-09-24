from abc import ABC, abstractmethod
from typing import List, Optional


class FileSystemComponent(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        pass


class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size

    def display(self, indent: int = 0) -> None:
        print("  " * indent + f" {self.name} ({self.size} bytes)")


class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> None:
        self.children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        self.children.remove(component)

    def get_child(self, index: int) -> Optional[FileSystemComponent]:
        if 0 <= index < len(self.children):
            return self.children[index]
        return None

    def get_size(self) -> int:
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def display(self, indent: int = 0) -> None:
        print("  " * indent + f" {self.name}/ ({self.get_size()} bytes)")
        for child in self.children:
            child.display(indent + 1)


if __name__ == "__main__":

    file1 = File("document.txt", 1500)
    file2 = File("image.jpg", 25000)
    file3 = File("data.csv", 800)
    file4 = File("notes.md", 1200)

    root = Directory("Root")
    documents = Directory("Documents")
    images = Directory("Images")
    projects = Directory("Projects")

    documents.add(file1)
    documents.add(file4)

    images.add(file2)

    projects.add(file3)
    projects.add(documents)

    root.add(images)
    root.add(projects)

    print("=== File System Structure ===")
    root.display()

    print(f"\n=== Total Size: {root.get_size()} bytes ===")

    print("\n=== Working with individual components ===")
    file1.display()
    documents.display()