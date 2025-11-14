import threading
import time
from datetime import datetime

def print_current_time():
    while True:
        print(f"Current Time: {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(1)

def print_one_minute_message():
    while True:
        time.sleep(60)
        print("1 Minute Completed")

# Create threads
thread1 = threading.Thread(target=print_current_time)
thread2 = threading.Thread(target=print_one_minute_message)

# Start threads
thread1.start()
thread2.start()

# Let them run for a while
time.sleep(300)  # Run for 5 minutes

# Join threads
thread1.join()
thread2.join()
