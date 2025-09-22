class Database:
    instance = None

    def __new__(cls, *args, **kwargs):
        if Database.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __del__(self):
        Database.instance = None

    def __init__(self, user: str, port: str, connection: bool):
        self.user = user
        self.port = port
        self.connection = connection


if __name__ == '__main__':
    db1 = Database("Mike", "123", True)
    db2 = Database("Alice", "343", True)

    print(db1)
    print(db2)
    print(db1 is db2)




