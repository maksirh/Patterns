from abc import ABC, abstractmethod
from typing import List


class TaskModel:

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def get_all_tasks(self) -> List[dict]:
        return self.tasks.copy()

    def add_task(self, title: str) -> dict:
        task = {
            'id': self.next_id,
            'title': title,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        return task

    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                return True
        return False

    def delete_task(self, task_id: int) -> bool:

        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks.pop(i)
                return True
        return False


class TaskView:

    def show_menu(self):
        print("\n" + "=" * 30)
        print("МІЙ СПИСОК ЗАВДАНЬ")
        print("=" * 30)
        print("1. Показати всі завдання")
        print("2. Додати завдання")
        print("3. Виконати завдання")
        print("4. Видалити завдання")
        print("0. Вийти")
        print("-" * 30)

    def show_tasks(self, tasks: List[dict]):
        if not tasks:
            print("\nСписок завдань порожній")
            return

        print("\nВСІ ЗАВДАННЯ:")
        for task in tasks:
            status = "✅" if task['completed'] else "⏳"
            print(f"{task['id']}. {status} {task['title']}")

    def show_message(self, message: str):
        print(f"\nℹ{message}")

    def show_error(self, error: str):
        print(f"\n{error}")

    def get_task_title(self) -> str:
        return input("Введіть назву завдання: ")

    def get_task_id(self) -> int:
        try:
            return int(input("Введіть ID завдання: "))
        except ValueError:
            return 0


class TaskController:

    def __init__(self):
        self.model = TaskModel()
        self.view = TaskView()

    def show_all_tasks(self):
        tasks = self.model.get_all_tasks()
        self.view.show_tasks(tasks)

    def add_task(self):
        title = self.view.get_task_title()
        if title.strip():
            self.model.add_task(title)
            self.view.show_message("Завдання додано!")
        else:
            self.view.show_error("Назва завдання не може бути порожньою")

    def complete_task(self):
        task_id = self.view.get_task_id()
        if task_id:
            if self.model.complete_task(task_id):
                self.view.show_message("Завдання позначено як виконане!")
            else:
                self.view.show_error("Завдання з таким ID не знайдено")
        else:
            self.view.show_error("Невірний ID завдання")

    def delete_task(self):
        task_id = self.view.get_task_id()
        if task_id:
            if self.model.delete_task(task_id):
                self.view.show_message("Завдання видалено!")
            else:
                self.view.show_error("Завдання з таким ID не знайдено")
        else:
            self.view.show_error("Невірний ID завдання")


class TodoApp:

    def __init__(self):
        self.controller = TaskController()

    def run(self):
        while True:
            self.controller.view.show_menu()
            choice = input("Ваш вибір: ")

            if choice == '1':
                self.controller.show_all_tasks()
            elif choice == '2':
                self.controller.add_task()
            elif choice == '3':
                self.controller.complete_task()
            elif choice == '4':
                self.controller.delete_task()
            elif choice == '0':
                print("\n До побачення!")
                break
            else:
                print("\nНевірний вибір! Спробуйте ще раз.")


if __name__ == "__main__":
    app = TodoApp()
    app.run()