# Try, except, and else for division
def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero.")
    except ValueError as e:
        print(f"Error: Invalid number input.")
    else:
        print(f"Division result: {result}")

divide_numbers()
