# input () : This function is used to take input from the user in Python. When this function is called, the program will pause and wait for the user to type something and press the Enter key. 

# The input provided by the user is then returned as a string. 
# you can typecast the input to other data types if needed.

# you can also provide a prompt message inside the input() function to guide the user on what kind of input is expected.

# example of taking input from the user
name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello, {name}! You are {age} years old.")


# typecasting input from the user 
x = int(input("enter your number: "))
print(type(x))