# for loop : execute a block of code a fixed number of time
# you can iterate over a range of numbers, list, string, etc.

# syntax :
# for variable in sequence:
#     # code to be executed repeatedly  

# example 1 : iterating over a range of numbers
for i in range(0,5):  # iterates from 0 to 4, last number is exclusive
    print("Iteration number:", i)

print()

# range function accept 3 inputs : range(start, end, steps) , end is exclusive
print("Using range with start, end, step:")
for i in range(1, 10, 2):  # iterates from 1 to 9 with step of 2
    print(i)    


print()

# example 2 : iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

print()

# example 3 : iterating over a string
my_string = "hello"
for char in my_string:
    print("Character:", char)

print()

# example 4 : using break statement in for loop
for i in range(10):
    if i == 5:
        break  # exit the loop when i is 5
    print("i is:", i)
print("Loop exited with break.")

print()

# example 5 : using continue statement in for loop
for i in range(10):
    if i % 2 == 0:
        continue  # skip even numbers
    print("Odd number:", i) 

print()

# example 6 : using else with for loop
for i in range(3):
    print("i is:", i)
else:
    print("For loop completed normally.")
# else block executes only if the loop was not terminated by a break statement

print()

# example 7 : nested for loops
for i in range(2):
    for j in range(3):
        print(f"Outer: {i}, Inner: {j}")
print("Finished nested loops.")     

print()

# example 8 : iterating with index using enumerate()
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")

