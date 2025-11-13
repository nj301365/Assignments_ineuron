class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# Example
user1 = User("Alice", 25, "alice@example.com")
print(user1.name, user1.age, user1.email)
