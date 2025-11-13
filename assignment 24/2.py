class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greet(self):
        print(f"Hello, {self.name}!")

user1 = User("Bob", 30, "bob@example.com")
user1.greet()
