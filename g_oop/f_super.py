# super() : function used in child class to call method from parent class (superclass)

class Shape:
    def __init__(self, color):
        self.color = color
    
    def describe(self):
        return f"A {self.color} shape"


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)  # calling the __init__ method of Shape class
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

    # you already had describe methon in parent class, now if you are defining describe method in child class, it will override the describe method of parent class, means when you call describe method on child class object, it will call the describe method of child class, not parent class
    def describe(self):
        print(f"A rectangle of color {self.color}, width {self.width}, and height {self.height}.")

        # if you want to call the describe method of parent class, you can use super()
        super().describe()
        # now first it will print the describe method of child class, then it will call the describe method of parent class
        # Output:
        # A rectangle of color Red, width 4, and height 5.
        # A Red shape

    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)  # calling the __init__ method of Shape class
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def describe(self):
        print(f"A circle of color {self.color} and radius {self.radius}.")
        super().describe()


# creating objects of Rectangle and Circle classes
rect = Rectangle("Red", 4, 5)

# you can also pass parameters with names
circle = Circle(color="Blue", radius=3) 

# calling methods on Rectangle object
rect.describe()
print(f"Area of rectangle: {rect.area()}")  

# calling methods on Circle object
circle.describe()
print(f"Area of circle: {circle.area()}")