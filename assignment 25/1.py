class Profile:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

# Example usage
p = Profile("Alice", "alice@example.com", 25)
print(p.name, p.email, p.age)
