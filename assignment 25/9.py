class Truecaller:
    def __init__(self):
        self.contacts = {}

    def fetch(self, number):
        return self.contacts.get(number, "Number not found")

    def add_contact(self, number, name):
        self.contacts[number] = name

tc = Truecaller()
tc.add_contact("1234567890", "Alice")
print(tc.fetch("1234567890"))
print(tc.fetch("9876543210"))
