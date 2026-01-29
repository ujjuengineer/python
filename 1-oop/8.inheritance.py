# child class can't inherit the privtatt memeber of parent clss 
# example when both child and parent class have constructor and child can't inherit all the instance varialbe of your parent class

# example of when only parent calss have constructor, and you will inherti all the instance variable of your parent calss

# method overriding -> polymorphism
# 3 things in polymorphism : method overriding, method overloading, operator overloading

"""
===========================
INHERITANCE IN PYTHON (OOP)
===========================

Inheritance allows a class (Child) to acquire:
- properties (variables)
- behaviors (methods)

from another class (Parent).

Definition:
-----------
Inheritance represents an "IS-A" relationship.

Example:
--------
Dog IS-A Animal
Student IS-A Person
Car IS-A Vehicle
"""


"""
--------------------------------
WHY DO WE USE INHERITANCE?
--------------------------------
1. Code reusability
2. Avoid duplication
3. Logical class hierarchy
4. Easy maintenance
5. Polymorphism support
"""


"""
--------------------------------
BASIC SYNTAX
--------------------------------
"""

class Parent:
    pass

class Child(Parent):
    pass


"""
--------------------------------
SIMPLE EXAMPLE
--------------------------------
"""

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()    # inherited
d.bark()   # own method


"""
--------------------------------
TYPES OF INHERITANCE IN PYTHON
--------------------------------

1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
"""


"""
--------------------------------
1. SINGLE INHERITANCE
--------------------------------
"""

class A:
    pass

class B(A):
    pass


"""
--------------------------------
2. MULTILEVEL INHERITANCE
--------------------------------
"""

class A:
    pass

class B(A):
    pass

class C(B):
    pass


"""
--------------------------------
3. MULTIPLE INHERITANCE
--------------------------------
"""

class A:
    pass

class B:
    pass

class C(A, B):
    pass


"""
--------------------------------
4. HIERARCHICAL INHERITANCE
--------------------------------
"""

class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass


"""
--------------------------------
CONSTRUCTOR (__init__) & INHERITANCE
--------------------------------
This is the MOST IMPORTANT part 🔥
"""


"""
=====================================================
SCENARIO 1:
ONLY PARENT HAS CONSTRUCTOR
=====================================================
"""

class Parent:
    def __init__(self):
        print("Parent constructor called")

class Child(Parent):
    pass

c = Child()

"""
Output:
-------
Parent constructor called

Explanation:
------------
- Child has no constructor
- Python automatically calls Parent's constructor
"""


"""
=====================================================
SCENARIO 2:
BOTH PARENT AND CHILD HAVE CONSTRUCTOR
(BUT super() NOT USED)
=====================================================
"""

class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        print("Child constructor")

c = Child()

"""
Output:
-------
Child constructor

Explanation:
------------
- Child's constructor OVERRIDES Parent's constructor
- Parent constructor is NOT called automatically
"""


"""
=====================================================
SCENARIO 3:
BOTH HAVE CONSTRUCTOR (USING super())
=====================================================
"""

class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()   # calling parent constructor
        print("Child constructor")

c = Child()

# NOTE : super() keyword class ke bahar kaam nhi krta hai
# like you can't do this c.super().__init__(); 




class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera) # pehle parent constructtor ko call kr diya
        # baad me bake ke variable set kr diya
        self.os = os
        self.ram = ram

s = SmartPhone(200000, "iPhone-17", "30Px", "ios-17", 6)

"""
Output:
-------
Parent constructor
Child constructor

Explanation:
------------
- super() explicitly calls Parent's constructor
- This is the CORRECT & RECOMMENDED way
"""


"""
=====================================================
SCENARIO 4:
PARENT HAS PARAMETERS
=====================================================
"""

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

c = Child("Ujjwal")
print(c.name)

"""
Explanation:
------------
- Parent constructor needs arguments
- Child must pass them using super()
"""


"""
=====================================================
SCENARIO 5:
WRONG WAY (COMMON MISTAKE)
=====================================================
"""

class Parent:
    def __init__(self, name):
        self.name = name
        self.isAlive = True

class Child(Parent):
    def __init__(self, name):
        self.name = name   # ❌ Parent init NOT called

"""
Problem:
--------
- isAlive is never created
- Parent initialization logic is LOST

Correct Way:
------------
Always use super().__init__()
"""


"""
--------------------------------
METHOD OVERRIDING
--------------------------------
"""

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

c = Child()
c.show()

"""
Output:
-------
Child method

Explanation:
------------
- Child method overrides Parent method
"""


"""
--------------------------------
CALLING PARENT METHOD EXPLICITLY
--------------------------------
"""

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")


"""
--------------------------------
POLYMORPHISM USING INHERITANCE
--------------------------------
"""

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

animal: Animal = Dog()
animal.speak()

"""
Output:
-------
Woof

Explanation:
------------
- Reference type = Parent
- Object type = Child
- Method resolution happens at runtime
- This is Runtime Polymorphism
"""


"""
--------------------------------
IMPORTANT INTERVIEW POINTS
--------------------------------
- Inheritance = IS-A relationship
- Constructor is NOT inherited
- Child constructor overrides Parent constructor
- super() is used to call Parent constructor
- Enables polymorphism
"""


"""
--------------------------------
TL;DR
--------------------------------
Inheritance = IS-A
Parent constructor is called ONLY if:
- Child has no constructor
- OR super().__init__() is used

Always use super() to avoid bugs
"""
