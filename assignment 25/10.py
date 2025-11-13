class SmartPhone(Calculator2, Phone):
    def use_truecaller(self, truecaller_obj, number):
        print(truecaller_obj.fetch(number))

sp = SmartPhone()
tc = Truecaller()
tc.add_contact("1234567890", "Alice")

sp.use_truecaller(tc, "1234567890")  # Alice
sp.use_truecaller(tc, "9876543210")  # Number not found
