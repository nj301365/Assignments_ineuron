import threading

def task1():
    print("Task 1 is starting")
    time.sleep(2)
    print("Task 1 completed")

def task2():
    print("Task 2 is starting")
    time.sleep(2)
    print("Task 2 completed")

# Create threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start first thread
thread1.start()

# Wait for thread1 to finish before starting thread2
thread1.join()

# Start second thread
thread2.start()

# Wait for second thread to finish
thread2.join()

print("Both tasks completed.")
