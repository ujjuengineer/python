"""
A generator in Python is a special kind of function that allows you to loop over a sequence of values, but instead of creating the entire sequence in memory at once, it generates each item one at a time, on demand.

The easiest way to understand generators is to look at the memory problem they solve.

Imagine you need to process a list of 1 million numbers.

A standard function calculates all 1 million numbers, crams them into a massive list in your computer's RAM, and then returns that list. If the list is too big, your computer runs out of memory and crashes.

"""

# generator way

# A generator doesn't store a list. It acts like a factory conveyor belt. It calculates the first number, hands it to you, suspends its execution, and waits until you ask for the next one. It only ever holds one number in memory at a time.


def generate_num(num):
    i = 0
    while i < num:
        yield i # Pauses here and hands the value over
        i += 1

g = generate_num(10) # generator

print(next(g)) # gives you 0
print(next(g)) # gives you 1

# NOTE : yield pauses the function, saves its entire state (where it left off, current variable values), hands a value back to the caller, and waits to be resumed.



# lets read a long file using yeilds


def read_massive_file(file_path):
    with open(file_path, "r") as file: # the file is itself a generator 
        for line in file:
            yield line  # Hands you one line, drops the previous line from memory

# now you can use next to read the line 
g = read_massive_file("temp.txt")

while True:
    # If the generator runs out of lines, it will return the string 'End of File'
    line = next(g, "end of file") 

    print(line, end="")

    if line == "end of file":
        break


print(); print("---------------------------")


# Python's built-in file reading actually uses a generator under the hood!
# you can simple do like this
file = open('temp.txt', 'r')
for line in file:
    print(line, end="")
    
file.close()