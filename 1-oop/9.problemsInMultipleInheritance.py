"""
========================================
MULTIPLE INHERITANCE IN PYTHON (OOP)
========================================

Multiple inheritance means:
----------------------------
A class inherits from MORE THAN ONE parent class.

Syntax:
-------
class Child(Parent1, Parent2):
    pass
"""


"""
----------------------------------------
WHY MULTIPLE INHERITANCE IS DANGEROUS
----------------------------------------
Although powerful, multiple inheritance introduces
conflicts and ambiguity if not handled properly.

Python allows it, but DOES NOT mean it is always a good idea.
"""


"""
========================================
1. METHOD NAME CONFLICT
========================================
When two parent classes define the SAME method name.
"""

class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

c = C()
c.show()   # Output: A


"""
Explanation:
------------
Python follows Method Resolution Order (MRO).
It checks classes from LEFT to RIGHT.

MRO:
----
C → A → B → object
"""


"""
========================================
2. DIAMOND PROBLEM (MOST IMPORTANT 🔥)
========================================

Structure:
----------
        A
       / \
      B   C
       \ /
        D
"""

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()   # Output: B


"""
Explanation:
------------
Python resolves this using C3 Linearization (MRO).

MRO:
----
D → B → C → A → object

Without MRO, method selection would be ambiguous.
"""


"""
========================================
3. CONSTRUCTOR (__init__) CONFLICT
========================================
Only ONE parent constructor runs by default.
"""

class A:
    def __init__(self):
        print("A init")

class B:
    def __init__(self):
        print("B init")

class C(A, B):
    def __init__(self):
        super().__init__()

c = C()


"""
Output:
-------
A init

Issue:
------
B.__init__() is NEVER called.
This causes partial initialization bugs.
"""


"""
========================================
4. WRONG USE OF super() (COMMON BUG)
========================================
Using super() in only ONE class breaks the chain.
"""

class A:
    def __init__(self):
        print("A init")

class B:
    def __init__(self):
        print("B init")

class C(A, B):
    def __init__(self):
        super().__init__()

"""
Problem:
--------
B is skipped completely.
"""


"""
========================================
5. CORRECT WAY (COOPERATIVE MULTIPLE INHERITANCE)
========================================
Every class MUST call super().
"""

class A:
    def __init__(self):
        print("A init")
        super().__init__()

class B:
    def __init__(self):
        print("B init")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()

c = C()


"""
Output:
-------
C init
A init
B init

Explanation:
------------
super() follows MRO and ensures ALL constructors run.
"""


"""
========================================
6. ATTRIBUTE CONFLICT
========================================
Same variable name in multiple parents.
"""

class A:
    x = 10

class B:
    x = 20

class C(A, B):
    pass

print(C.x)   # Output: 10


"""
Reason:
-------
Left-to-right MRO resolution.
"""


"""
========================================
7. DESIGN-LEVEL CONFLICT (LOGIC AMBIGUITY)
========================================
Even if code works, logic may be unclear.
"""

class Logger:
    def process(self):
        print("Logging")

class Validator:
    def process(self):
        print("Validating")

class Service(Logger, Validator):
    pass

s = Service()
s.process()   # Output: Logging


"""
Issue:
------
What does process() actually mean?
Bad design even if Python resolves it.
"""


"""
========================================
8. METHOD RESOLUTION ORDER (MRO)
========================================
Python resolves conflicts using MRO.

Check MRO:
----------
print(ClassName.mro())
"""

# Example:
# print(C.mro())


"""
========================================
9. WHEN MULTIPLE INHERITANCE IS BAD ❌
========================================
- Business logic inheritance
- Stateful parent classes
- Django models
- Large class hierarchies
- Overlapping method names
"""


"""
========================================
10. WHEN MULTIPLE INHERITANCE IS OK ✅
========================================
Use MIXINS (stateless behavior helpers)
"""

class Flyable:
    def fly(self):
        print("Flying")

class Swimmable:
    def swim(self):
        print("Swimming")

class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.fly()
d.swim()


"""
========================================
INTERVIEW TRUTH 💣
========================================
"Multiple inheritance is powerful but dangerous.
Use it only with mixins and stateless behavior."
"""


"""
========================================
TL;DR
========================================
- Multiple inheritance causes conflicts
- Diamond problem is the biggest risk
- Python uses MRO (C3 linearization)
- super() must be used in ALL classes
- Best used with mixins
- Allowed ≠ recommended
"""
