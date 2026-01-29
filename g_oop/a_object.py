# object : a bundle of related attributes(variable) and methods(function)
# you need to use class to create an object

class Car:
    def __init__(self, model, color, year, for_sale):
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale

# explanation of the code above
# class Car:  --> this line defines a class named Car
# def __init__(self, model, color, year, for_sale):  --> this line defines the constructor method that initializes the object's attributes
# self in the method refers to the object we are currently working with, it is passed automatically when you create an object of the class

# let use create an object of the Car class
car1 = Car("Toyota", "Red", 2020, True) # you don't need to pass self when creating an object
car2 = Car("Honda", "Blue", 2018, False)

# accessing the attributes of the objects
# you can access the attributes of an object using the dot notation
print(car1.model)  # Output: Toyota
print(car2.color)  # Output: Blue   
print(car1.year)   # Output: 2020
print(car2.for_sale)  # Output: False
        

# the class above is taking too much space, so we can put it in a separate file named a_object.py and import it here to use it

# see example in next file

