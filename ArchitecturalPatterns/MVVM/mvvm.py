class User:

    def __init__(self, name: str):
        self.name = name


class UserViewModel:
    def __init__(self, user: User):
        self.user = user
        self.subscribers = []

    def bind(self, callback):
        self.subscribers.append(callback)

    def notify(self):
        for cb in self.subscribers:
            cb(self)

    @property
    def name(self):
        return self.user.name

    @name.setter
    def name(self, new_name):
        if self.user.name != new_name:
            self.user.name = new_name
            self.notify()


def show_user_info(view_model: UserViewModel):
    print(f"Ім'я (View): {view_model.name}")


if __name__ == "__main__":
    user = User("Максим")

    view_model = UserViewModel(user)

    view_model.bind(show_user_info)

    show_user_info(view_model)

    print("\n Змінюємо ім'я у ViewModel")
    view_model.name = "Марія"

    print("\nІмітуємо зміну у View (користувач ввів нове ім'я)")
    view_model.name = "Петро"

    print("\nПеревіряємо Model напряму")
    print(f"Ім'я в Model: {user.name}")
