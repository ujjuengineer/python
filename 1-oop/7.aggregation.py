"""
===========================
AGGREGATION IN PYTHON (OOP)
===========================

Aggregation is a type of relationship between classes.

Definition:
------------
Aggregation represents a "HAS-A" relationship where:
- One class uses another class
- BUT the owned object can exist independently

In simple words:
----------------
Aggregation = Weak HAS-A relationship

Example:
---------
College HAS-A Student
Company HAS-A Employee
Library HAS-A Book

If College is destroyed → Student can still exist
If Company is destroyed → Employee can still exist

This is what makes aggregation different from composition.
"""


"""
--------------------------------
WHY DO WE NEED AGGREGATION?
--------------------------------
1. Code reusability
2. Better modular design
3. Loose coupling between classes
4. Real-world modeling
"""


"""
--------------------------------
BASIC EXAMPLE
--------------------------------
"""

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine   # Aggregation (Car HAS-A Engine)

    def drive(self):
        self.engine.start()
        print("Car is moving")


engine = Engine()      # Engine exists independently
car = Car(engine)     # Engine is passed to Car

car.drive()


"""
Explanation:
------------
- Engine is created outside Car
- Car just uses Engine
- Engine can exist without Car
- This is AGGREGATION
"""


"""
--------------------------------
KEY CHARACTERISTICS OF AGGREGATION
--------------------------------
1. HAS-A relationship
2. Objects have independent lifecycle
3. One class uses another class
4. Loose coupling
"""


"""
--------------------------------
AGGREGATION vs INHERITANCE
--------------------------------

Inheritance:
------------
Dog IS-A Animal
- Tight coupling
- Child depends on Parent
- Uses "extends" concept

Aggregation:
------------
Car HAS-A Engine
- Loose coupling
- Objects are independent
- Uses object reference
"""


"""
--------------------------------
AGGREGATION vs COMPOSITION
--------------------------------

Aggregation:
------------
- Weak HAS-A
- Child object can live alone
- Example: Department HAS-A Teacher

Composition:
------------
- Strong HAS-A
- Child object cannot live alone
- Example: House HAS-A Room

If House is destroyed → Rooms are destroyed
"""


"""
--------------------------------
REAL LIFE EXAMPLE
--------------------------------
"""

class Student:
    def __init__(self, name):
        self.name = name

class College:
    def __init__(self, student):
        self.student = student   # Aggregation

    def show_student(self):
        print(f"Student name: {self.student.name}")


s1 = Student("Ujjwal")
college = College(s1)

college.show_student()


"""
--------------------------------
IMPORTANT INTERVIEW POINTS
--------------------------------
- Aggregation is a HAS-A relationship
- Objects have separate lifecycles
- Implemented using object reference
- Promotes loose coupling
- Better than inheritance when behavior is not shared
"""


"""
--------------------------------
COMMON MISTAKE
--------------------------------
Thinking aggregation == inheritance ❌

NO.
Inheritance is IS-A
Aggregation is HAS-A
"""


"""
--------------------------------
TL;DR
--------------------------------
Aggregation = HAS-A relationship
Objects are independent
One class uses another class
Loose coupling
Real-world friendly
"""
