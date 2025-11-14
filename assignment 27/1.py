# Creating an ArithmeticError
def create_arithmetic_error():
    try:
        result = 1 / 0  # This will raise ArithmeticError (division by zero)
    except ArithmeticError as e:
        print(f"ArithmeticError: {e}")

create_arithmetic_error()
