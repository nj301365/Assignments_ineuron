import threading
import random

def fill_list_random_numbers(lst, count):
    for _ in range(count):
        lst.append(random.randint(1, 100))

random_numbers = []

# Create 5 threads
threads = [threading.Thread(target=fill_list_random_numbers, args=(random_numbers, 20)) for _ in range(5)]

# Start threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Random Numbers List:", random_numbers)
