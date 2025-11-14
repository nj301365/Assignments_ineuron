# Calculator with finally block
def calculator():
    try:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        operation = input("Enter operation (1/2/3/4): ")

        if operation not in ('1', '2', '3', '4'):
            raise ValueError("Invalid operation selected")
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation == '1':
            result = num1 + num2
        elif operation == '2':
            result = num1 - num2
        elif operation == '3':
            result = num1 * num2
        elif operation == '4':
            result = num1 / num2  # This could raise ZeroDivisionError
        
        print(f"Result: {result}")
    
    except ValueError as e:
        print(f"ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Execution completed.")

calculator()
