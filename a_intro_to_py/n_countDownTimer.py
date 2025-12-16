# countdown timer program

import time 

# time.sleep(seconds) : This function is used to pause the execution of the program for a specified number of seconds.

# we will create a countdown timer that counts down from a specified number of seconds to zero.
# we will use time.sleep() to create a delay of 1 second between each count.

my_time  = int(input("Enter time in sec for countdown: "))

for x in range(my_time, 0, -1):
    sec = x % 60
    mins = (x // 60) % 60
    hrs = (x // 3600)
    print(f"{hrs:02}:{mins:02}:{sec:02}")
    time.sleep(1) # pause for 1 second

print("Time's up !!")