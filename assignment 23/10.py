def co_prime_check(func):
    def wrapper(a, b):
        def hcf(x, y):
            while y != 0:
                x, y = y, x % y
            return x
        if hcf(a, b) == 1:
            print(f"{a} and {b} are co-prime")
        else:
            print(f"{a} and {b} are not co-prime")
        func(a, b)
    return wrapper

@co_prime_check
def calculate_hcf(a, b):
    while b != 0:
        a, b = b, a % b
    print("HCF:", a)

calculate_hcf(15, 28)
calculate_hcf(12, 18)
