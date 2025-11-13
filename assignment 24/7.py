class Laptop:
    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def showConfig(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}GB, CPU: {self.cpu}, HDD: {self.hdd}GB")

    def upgrade_ram(self, new_ram):
        self.ram = new_ram
        print(f"RAM upgraded to {self.ram}GB")

    def change_hdd(self, new_hdd):
        self.hdd = new_hdd
        print(f"HDD changed to {self.hdd}GB")

# Example usage
laptop1 = Laptop("Dell", 8, "i5", 512)
laptop1.showConfig()
laptop1.upgrade_ram(16)
laptop1.change_hdd(1024)
laptop1.showConfig()
