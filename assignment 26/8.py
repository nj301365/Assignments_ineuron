import threading

def print_hello():
    print("Hello from thread!")

# Create thread
thread = threading.Thread(target=print_hello)
# Change thread name
print(f"Old Thread Name: {thread.name}")
thread.name = "MyCustomThreadName"

# Start thread
thread.start()

# Print thread name
print(f"Thread Name: {thread.name}")

# Wait for thread to complete
thread.join()
