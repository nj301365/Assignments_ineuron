class User:
    def __init__(self, name="Unknown", age=0, email="unknown@example.com"):
        self.name = name
        self.age = age
        self.email = email

user1 = User()
user2 = User("Charlie", 28, "charlie@example.com")
print(user1.name, user2.name)
