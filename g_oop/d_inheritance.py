# inheritance : allows a class to inherit attributes and methods from another class 
#               it helps to reuse code and establish a relationship between classes   
#               class Child(Parent):

class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):  # Dog class inherits from Animal class
    
    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):  # Cat class inherits from Animal class
    
    def meow(self):
        print(f"{self.name} says Meow!")

dog1 = Dog("Buddy")
cat1 = Cat("Whiskers") 

dog1.eat()      # Output: Buddy is eating
dog1.sleep()    # Output: Buddy is sleeping
dog1.bark()     # Output: Buddy says Woof!

cat1.eat()      # Output: Whiskers is eating
cat1.sleep()    # Output: Whiskers is sleeping
cat1.meow()     # Output: Whiskers says Meow!

"""
NOTE 
why are we not defining __init__ method in Dog and Cat classes?
because they are inheriting the __init__ method from the Animal class

if we define __init__ method in Dog or Cat class, it will override the __init__ method of Animal class, means the __init__ method of Animal class will not be called when we create an object of Dog or Cat class and we have to manually initialize the attributes of Animal class in the __init__ method of Dog or Cat class
"""