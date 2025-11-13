laptop1 = Laptop("Dell", 8, "i5", 512)
laptop2 = Laptop("HP", 16, "i7", 1024)
laptop3 = Laptop("Lenovo", 4, "i3", 256)

laptops = [laptop1, laptop2, laptop3]
laptops.sort(key=lambda x: x.ram)

for laptop in laptops:
    laptop.showConfig()
