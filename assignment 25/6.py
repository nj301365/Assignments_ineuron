class Calculator2(Calculator):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

calc2 = Calculator2()
print(calc2.add(2, 3))       # inherited
print(calc2.multiply(2, 3))  # 6
