# Creating a ValueError
def create_value_error():
    try:
        int("abc")  # This will raise ValueError (invalid literal for int())
    except ValueError as e:
        print(f"ValueError: {e}")

create_value_error()
