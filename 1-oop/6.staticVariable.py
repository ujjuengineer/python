"""
STATIC VARIABLE & STATIC METHOD IN PYTHON
=========================================

FIRST — IMPORTANT CLARITY 🚨
----------------------------
Python DOES NOT have "static" keyword like C++ / Java.

But Python SUPPORTS:
1. Static Variables  → Class Variables
2. Static Methods    → @staticmethod

------------------------------------------------
1. STATIC VARIABLE (CLASS VARIABLE)
------------------------------------------------
Definition:
- A variable that belongs to the CLASS
- NOT to individual objects
- Shared by ALL instances

Syntax:
    class ClassName:
        variable_name = value

Example:
    class Student:
        college = "IIT Bombay"   # static variable

        def __init__(self, name):
            self.name = name     # instance variable

Usage:
    s1 = Student("A")
    s2 = Student("B")

    print(s1.college)  # IIT Bombay
    print(s2.college)  # IIT Bombay

WHY?
- Only ONE copy exists in memory
- All objects refer to the same variable

------------------------------------------------
2. INSTANCE VARIABLE vs STATIC VARIABLE
------------------------------------------------
Instance Variable:
- Created using self
- Different for each object

Static Variable:
- Created inside class
- Same for all objects

Example:
    class Test:
        x = 10        # static

        def __init__(self):
            self.y = 20   # instance

------------------------------------------------
3. MODIFYING STATIC VARIABLE ⚠️ (VERY IMPORTANT)
------------------------------------------------
WRONG way:
    obj.x = 100

WHY WRONG?
- This creates a NEW instance variable
- Does NOT change class variable

RIGHT way:
    ClassName.x = 100

Example:
    Student.college = "IIT Delhi"

------------------------------------------------
4. WHEN TO USE STATIC VARIABLE
------------------------------------------------
Use static variables when:
✔ Data is COMMON for all objects
✔ Constants
✔ Counters
✔ Configuration values

Examples:
- total_students
- company_name
- interest_rate

------------------------------------------------
5. STATIC METHOD
------------------------------------------------
Definition:
- A method that DOES NOT depend on object
- DOES NOT use self
- DOES NOT use class data (usually)

Syntax:
    @staticmethod
    def method_name():
        pass

Example:
    class MathUtils:

        @staticmethod
        def add(a, b):
            return a + b

Usage:
    MathUtils.add(3, 4)

------------------------------------------------
6. WHY STATIC METHOD EXISTS
------------------------------------------------
Static method is used when:
✔ Logic is RELATED to class
✔ But does NOT need instance data
✔ Utility / helper function

Think of it as:
"Function kept inside a class for organization"

------------------------------------------------
7. STATIC METHOD vs INSTANCE METHOD
------------------------------------------------
Instance Method:
- Uses self
- Works on object data

Static Method:
- No self
- No object required

Example:
    class Demo:

        def instance_method(self):
            print("Uses object")

        @staticmethod
        def static_method():
            print("No object needed")

------------------------------------------------
8. STATIC METHOD vs CLASS METHOD (INTERVIEW TRAP ⚠️)
------------------------------------------------
Static Method:
- @staticmethod
- No self, no cls
- Independent logic

Class Method:
- @classmethod
- Uses cls
- Accesses class variables

Example:
    class Test:
        x = 10

        @classmethod
        def show(cls):
            print(cls.x)

------------------------------------------------
9. CAN STATIC METHOD ACCESS STATIC VARIABLE?
------------------------------------------------
YES ✅ (but using class name)

Example:
    class Test:
        x = 10

        @staticmethod
        def show():
            print(Test.x)

------------------------------------------------
10. REAL INTERVIEW ONE-LINERS 🚀
------------------------------------------------
Static Variable:
"Shared among all objects of a class"

Static Method:
"Utility method that does not depend on object state"

------------------------------------------------
11. COMMON MISTAKES ❌
------------------------------------------------
❌ Using self in static method
❌ Modifying static variable via object
❌ Thinking static method has access to instance data

------------------------------------------------
12. TL;DR (BRAIN SAVE MODE 🧠)
------------------------------------------------
✔ Static variable = class variable
✔ One copy shared by all objects
✔ Static method = no self, no cls
✔ Used for utility logic
✔ Access static variable using ClassName

------------------------------------------------
END OF NOTES
------------------------------------------------
"""
