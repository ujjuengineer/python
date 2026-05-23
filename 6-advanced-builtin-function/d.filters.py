"""
The filter() function in Python is a built-in tool used to extract elements from a collection (like a list) that meet a specific condition.

filter behaves exactly like a generator! In Python 3, filter() returns a special filter object, which is a lazy iterator. It does not calculate or store the filtered items in memory all at once; it yields them one by one on demand.


Here is how it works, why it's efficient, and how it compares to generators.

1. The Basic Syntax
The filter() function takes two arguments:
    A function that returns True or False (the condition).
    An iterable (the data you want to filter).
"""

# A function that checks if a number is even
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

# Apply the filter
even_numbers = filter(is_even, numbers)

print(even_numbers)  # Output: <filter object at 0x...>
# Notice that printing even_numbers does not print [2, 4, 6]. It prints a <filter object>. This is because it is lazy—just like a generator, it hasn't actually done any filtering work yet!

""" extracting the data ffrom the filter """
# either you can do next(even_numbers) or you can iterate over it
for num in even_numbers:
    print(num)





# how filter mirror the generator function


numbers = [1, 2, 3, 4, 5, 6]
even_filter = filter(lambda x: x % 2 == 0, numbers)




def custom_filter_generator(data):
    for x in data:
        if x % 2 == 0:
            yield x  # Pauses and streams one item

even_gen = custom_filter_generator(numbers)



# Both even_filter and even_gen do the exact same thing in your computer's RAM. They act as automated conveyor belts that only process a number when you call next() or run a for loop over them.





# SUMMARY
"""
-> filter() yields elements that return True when passed through a testing function.

-> It is a generator/iterator under the hood, meaning it is highly memory-efficient for massive datasets.

-> Like any generator, once you loop through a filter object once, it is exhausted (empty), and you cannot loop through it a second time without recreating it.
"""