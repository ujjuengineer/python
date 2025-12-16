# while loop : execute some code repeatedly as long as a condition is true
# syntax :
# while condition:
#     # code to be executed repeatedly



# example 1 : simple while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # increment count to avoid infinite loop
print("Finished counting!")



# example 2 : while loop with break statement
num = 0
while True:
    print("Number is:", num)
    num += 1
    if num >= 3:
        break  # exit the loop when num is 3
print("Loop exited with break.")



# example 3 : while loop with continue statement
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # skip the rest of the loop when i is 3
    print("i is:", i)
print("Finished loop with continue.")



# example 4 : using else with while loop
n = 0
while n < 3:
    print("n is:", n)
    n += 1
else:
    print("While loop completed normally.")

# else block executes only if the loop was not terminated by a break statement



# example 5 : nested while loops
outer = 1
while outer <= 2:
    inner = 1
    while inner <= 3:
        print(f"Outer: {outer}, Inner: {inner}")
        inner += 1
    outer += 1
print("Finished nested loops.")     

