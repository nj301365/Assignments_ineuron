class User:
    def __init__(self, name="Unknown", age=0, email="unknown@example.com"):
        self.name = name
        self.age = age
        self.email = email
user = User("Alice", 25, "alice@example.com")
del user.age
# print(user.age)  # This would raise an AttributeError
