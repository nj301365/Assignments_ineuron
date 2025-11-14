import threading

def sum_numbers(start, end):
    total = sum(range(start, end + 1))
    print(f"Sum of numbers from {start} to {end}: {total}")

# Split range for two threads
thread1 = threading.Thread(target=sum_numbers, args=(1, 50))
thread2 = threading.Thread(target=sum_numbers, args=(51, 100))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()
