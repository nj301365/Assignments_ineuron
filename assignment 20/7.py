def outer_function():
    def inner_function():
        print("Hello from inner function")
    inner_function()  # calling inner function

outer_function()
