import threading

def check_prime(num):
    if num < 2:
        print(f"{num} is not a prime number")
        return
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            return
    print(f"{num} is a prime number")

def check_armstrong(num):
    digits = [int(digit) for digit in str(num)]
    order = len(digits)
    sum_of_powers = sum(digit ** order for digit in digits)
    if sum_of_powers == num:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

number = 153  # Example number

# Create threads
prime_thread = threading.Thread(target=check_prime, args=(number,))
armstrong_thread = threading.Thread(target=check_armstrong, args=(number,))

# Start threads
prime_thread.start()
armstrong_thread.start()

# Wait for threads to complete
prime_thread.join()
armstrong_thread.join()
