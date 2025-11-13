user1 = User("Alice", 25, "alice@example.com")
user2 = User("Bob", 30, "bob@example.com")
user3 = User("Charlie", 22, "charlie@example.com")

youngest = min(user1, user2, user3, key=lambda x: x.age)
print("Youngest:", youngest.name)
