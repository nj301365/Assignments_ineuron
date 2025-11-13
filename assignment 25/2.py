class Profile:
    def __init__(self, name, email, age):
        self.name = name
        self.__email = email
        self.__age = age

    # Getter for email
    def get_email(self):
        return self.__email

    # Setter for email
    def set_email(self, email):
        self.__email = email

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        self.__age = age

p = Profile("Alice", "alice@example.com", 25)
print(p.get_email(), p.get_age())
p.set_email("alice123@example.com")
p.set_age(26)
print(p.get_email(), p.get_age())
