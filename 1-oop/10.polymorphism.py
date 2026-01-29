# NOTE : mro (method resolution order)




# NOTE : 
# IMPORTANT
"""
Python does NOT support traditional method overloading
like C++ / Java.

Last defined method wins ❌
"""
# for an example here we have defined 2 add funcition
def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c

# add(1,2) => error , because python will call last defined add funciton 
add(1,2,3) # => will run properly 


#==================================================================================

"""
===========================
POLYMORPHISM IN PYTHON (OOP)
===========================

Polymorphism means:
-------------------
"Many forms"

Same function / method name
→ behaves differently
→ depending on object / context

In simple words:
----------------
One interface, multiple behaviors
"""


"""
--------------------------------
WHY POLYMORPHISM?
--------------------------------
1. Code flexibility
2. Scalability
3. Clean & readable design
4. Core concept behind OOP
5. Used heavily in real-world frameworks (Django, FastAPI)
"""


"""
--------------------------------
TYPES OF POLYMORPHISM IN PYTHON
--------------------------------

1. Compile-time Polymorphism
   - Method Overloading
   - Operator Overloading

2. Runtime Polymorphism
   - Method Overriding (Inheritance based)
"""


"""
================================
1. METHOD OVERRIDING (IMPORTANT 🔥)
================================

Definition:
-----------
When a child class provides its own implementation
of a method that already exists in the parent class.

Rules:
------
1. Same method name
2. Same parameters
3. Happens in inheritance
4. Decided at runtime
"""


class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")


a1 = Dog()
a2 = Cat()

a1.speak()   # Woof
a2.speak()   # Meow


"""
Explanation:
------------
- speak() exists in parent
- Child overrides it
- Correct method chosen at runtime
- This is Runtime Polymorphism
"""


"""
--------------------------------
POLYMORPHISM WITH PARENT REFERENCE
--------------------------------
"""

animal: Animal = Dog()
animal.speak()

"""
Output:
-------
Woof

Why?
----
- Reference type = Parent (Animal)
- Object type = Child (Dog)
- Python checks object, not reference
"""


"""
--------------------------------
CALLING PARENT METHOD (super)
--------------------------------
"""

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")


"""
================================
2. METHOD OVERLOADING
================================

Definition:
-----------
Same method name
Different number/type of parameters

IMPORTANT:
----------
Python does NOT support traditional method overloading
like C++ / Java.

Last defined method wins ❌
"""


class Test:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


"""
Problem:
--------
Second method overrides first one
Python keeps only ONE method
"""


"""
--------------------------------
HOW PYTHON ACHIEVES OVERLOADING?
--------------------------------
Using:
1. Default arguments
2. *args
3. **kwargs
"""


"""
Example 1: Default arguments
----------------------------
"""

class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(5))        # 5
print(m.add(5, 6))     # 11
print(m.add(5, 6, 7))  # 18


"""
Example 2: *args
----------------
"""

class Math:
    def add(self, *args):
        return sum(args)

m = Math()
print(m.add(1, 2))
print(m.add(1, 2, 3, 4))


"""
================================
3. OPERATOR OVERLOADING : use archive operator overloading using magic funciton 
================================

Definition:
-----------
Giving special meaning to operators
(+  -  *  /  ==  >  <)
for user-defined objects

Achieved using MAGIC METHODS
"""


"""
--------------------------------
Example WITHOUT operator overloading
--------------------------------
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


"""
--------------------------------
Example WITH operator overloading
--------------------------------
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x,
                     self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2
print(p3)   # (6, 8)


"""
Explanation:
------------
p1 + p2
→ calls p1.__add__(p2)
"""


"""
--------------------------------
COMMON OPERATOR METHODS
--------------------------------

+   → __add__()
-   → __sub__()
*   → __mul__()
/   → __truediv__()
==  → __eq__()
>   → __gt__()
<   → __lt__()
"""


"""
================================
DUCK TYPING (BONUS 🔥)
================================

Definition:
-----------
"If it looks like a duck and quacks like a duck,
it is a duck."

Python cares about behavior, not class
"""


class Dog:
    def speak(self):
        print("Woof")

class Human:
    def speak(self):
        print("Hello")

def make_sound(obj):
    obj.speak()

make_sound(Dog())
make_sound(Human())


"""
Explanation:
------------
- No inheritance
- Same method name
- Behavior-based polymorphism
"""


"""
================================
IMPORTANT INTERVIEW POINTS
================================
- Polymorphism = many forms
- Method overriding = runtime
- Python does NOT support traditional overloading
- Operator overloading uses magic methods
- Duck typing is Python-specific polymorphism
"""


"""
--------------------------------
TL;DR
--------------------------------
Method Overriding → Inheritance, runtime
Method Overloading → Achieved via args/defaults
Operator Overloading → Magic methods
Duck typing → Behavior > class
"""
