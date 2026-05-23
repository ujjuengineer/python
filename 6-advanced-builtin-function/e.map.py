"""
the map() function is a built-in Python tool designed to process collections of data efficiently.

map() also behaves exactly like a generator! It returns a lazy map object (an iterator) that does not calculate anything up front. It transforms your data one item at a time, strictly on demand.

map() is a factory machine that transforms every item passing down the conveyor belt.


1. The Basic Syntax
The map() function takes two arguments:
    -> A function that contains the transformation logic (what you want to do to the data).
    -> An iterable (the data you want to transform).
"""

# A function that doubles a number
def double(n):
    return n * 2

numbers = [1, 2, 3, 4]

# Apply the map
doubled_numbers = map(double, numbers)

print(doubled_numbers)  # Output: <map object at 0x...>

# The double function hasn't actually run on a single number yet!


# you can iterate through the generator to process every numbers one by one
for num in doubled_numbers:
    print(num)







numbers = [1, 2, 3, 4]
squared_map = map(lambda x: x ** 2, numbers)



def custom_map_generator(data):
    for x in data:
        yield x ** 2  # Transforms and hands over one item at a time

squared_gen = custom_map_generator(numbers)


# both coded behave identical in memory, they wait until a loop ask for a value , process that single value, hand it over and pause




# NOTE : A powerful feature of map() that people often forget is that it can accept multiple iterables at the same time, as long as your function accepts that many arguments. It will pair the items up by index:

def add_together(a, b):
    return a + b

list_one = [1, 2, 3]
list_two = [10, 20, 30]

# map() passes index 0 of both lists to the function, then index 1, etc.
summed_results = list(map(add_together, list_one, list_two))

print(summed_results)  # Output: [11, 22, 33]