import time
import random
import queue

from threading import Thread

counter = 0
job_queue = queue.Queue() # things to be printed
counter_queue = queue.Queue() # amount by which increase counter

def increment_manager():
    global counter

    while True:
        increment = counter_queue.get()
        time.sleep(random.random())
        old_counter = counter
        time.sleep(random.random())
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put(f"new counter value is {counter}")
        time.sleep(random.random())
        counter