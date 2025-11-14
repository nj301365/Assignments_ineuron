# Handling multiple exceptions in one try block
try:
    x = int("abc")  # ValueError
    y = 1 / 0  # ArithmeticError
except (ValueError, ArithmeticError) as e:
    print(f"Handled error: {e}")
