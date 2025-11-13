class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greet(self):
        print(f"Hello, {self.name}!")


user1 = User("Alice", 25, "alice@example.com")
user2 = User("Bob", 30, "bob@example.com")

print(user1.name, user2.name)
