# property decorator : it is used to define a method as a property
#          benifit : add additional logic when getting, setting or deleting an attribute
#          gives you getter, setter and delete methods for a class attribute


# from cmath import rect


class Rectangle : 
    def __init__ (self, width, height) :
        self._width = width 
        self._height = height

    # for using property decorator make sure to keep your private or protected attributes with a leading underscore, otherwise it may lead to confusion and bugs

    # using property decorator we can add additional logic while accessing the property
    # for that you need to define a method with @property decorator
    @property
    def width (self):
        print(f"Getting width : ")
        return self._width

    @property
    def height (self):
        print(f"Getting height : ")
        return self._height
    # basically they are getter methods

    # similarly you can define setter and deleter methods using @<property_name>.setter and @<property_name>.deleter decorators respectively


#===============================================================================================

    # setter method

    @width.setter
    def width (self, value):
        if value < 0:
            raise ValueError("Width cannot be negative")
        self._width = value

    @height.setter
    def height (self, value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value


#===============================================================================================
   
    # deleter method

    @width.deleter
    def width (self):
        print("Deleting width")
        del self._width

    @height.deleter
    def height (self):
        print("Deleting height")
        del self._height


    


print("=================================================================================")


# create an object of Rectangle class
rectangle = Rectangle(10, 5)

# access the width and height properties
print(rectangle.width)   # Output: Getting width : 10
print(rectangle.height)  # Output: Getting height : 5



print("=================================================================================")  


rectangle.width = 15  # setting width using setter method
rectangle.height = 7  # setting height using setter method

print(rectangle.width)   # Output: Getting width : 15
print(rectangle.height)  # Output: Getting height : 7



print("=================================================================================")


del rectangle.width  # deleting width using deleter method 
del rectangle.height  # deleting height using deleter method

# print(rectangle.width)   # raises AttributeError as width is deleted
# print(rectangle.height)  # raises AttributeError as height is deleted

# you can check if the attribute is deleted or not using hasattr() function
print(hasattr(rectangle, '_width'))   # Output: False
print(hasattr(rectangle, '_height'))  # Output: False