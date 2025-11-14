# Handling an ArithmeticError
try:
    result = 1 / 0  # This will raise ArithmeticError
except ArithmeticError as e:
    print(f"Handled ArithmeticError: {e}")
