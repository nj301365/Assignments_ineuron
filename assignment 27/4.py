# Handling a ValueError
try:
    value = int("xyz")  # This will raise ValueError
except ValueError as e:
    print(f"Handled ValueError: {e}")
