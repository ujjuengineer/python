# list comprehension : a concise way to create lists
# syntax: [expression for item in iterable if condition], don't forget the square brackets 

# Example 1: Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)] # creates list of squares
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print()

# Example 2: Create a list of even numbers from 0 to 19
evens = [x for x in range(20) if x % 2 == 0]
print(evens) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print()

# you can even call functions inside list comprehension
def square(n):
    return n * n

# Example 3: Using function inside list comprehension
squared_numbers = [square(x) for x in range(10)]