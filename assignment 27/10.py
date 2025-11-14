# Nested try/except blocks
def nested_try_except():
    try:
        print("Outer try block")
        try:
            print("Inner try block")
            x = 1 / 0  # Will cause ZeroDivisionError in inner block
        except ZeroDivisionError as inner_e:
            print(f"Handled inner ZeroDivisionError: {inner_e}")
        
        # Further code in outer try block
        y = int("abc")  # Will cause ValueError in outer block
    except ValueError as outer_e:
        print(f"Handled outer ValueError: {outer_e}")
    except Exception as e:
        print(f"Handled other error: {e}")
    finally:
        print("Finally block executed")

nested_try_except()
