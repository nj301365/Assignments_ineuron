import threading

def print_even_numbers():
    for i in range(0, 101, 2):
        print(f"Even: {i}")

def print_odd_numbers():
    for i in range(1, 101, 2):
        print(f"Odd: {i}")

# Create threads
thread1 = threading.Thread(target=print_even_numbers)
thread2 = threading.Thread(target=print_odd_numbers)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()
