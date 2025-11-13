def triangle_validity(func):
    def wrapper(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return func(a, b, c)
        else:
            print("Invalid triangle sides!")
    return wrapper

@triangle_validity
def perimeter(a, b, c):
    print("Perimeter:", a + b + c)

perimeter(3, 4, 5)  # Valid
perimeter(1, 2, 10) # Invalid
