class Calculator:
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

calc = Calculator()
print(calc.multiply(2, 3))  # Multiply 2 numbers
print(calc.multiply(2, 3, 4))  # Multiply 3 numbers
print(calc.multiply(2, 3, 4, 5))  # Multiply 4 numbers
