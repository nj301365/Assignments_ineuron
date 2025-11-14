# Raising a ValueError
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older")
    print("Age is valid")

try:
    check_age(15)  # This will raise ValueError
except ValueError as e:
    print(f"Error: {e}")
