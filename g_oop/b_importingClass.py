# you can import classes from other modules using the import statement

from car import Car

# now you run the similar code as in a_object.py but using the imported Car class

car1 = Car("Toyota", "Red", 2020, True) # you don't need to pass self when creating an object
car2 = Car("Honda", "Blue", 2018, False)

# accessing the attributes of the objects
# you can access the attributes of an object using the dot notation
print(car1.model)  # Output: Toyota
print(car2.color)  # Output: Blue   
print(car1.year)   # Output: 2020
print(car2.for_sale)  # Output: False


# let us use methods present in our Car class
car1.display_info()  # Output: Model: Toyota, Color: Red, Year: 2020, For Sale: True
car2.display_info()  # Output: Model: Honda, Color: Blue, Year: 2018, For Sale: False