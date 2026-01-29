"""
===========================================================
        PYTHON CONCEPT - MODULES (DEEP NOTES)
===========================================================

CORE IDEA:
----------
A module is simply a Python file (.py) that contains:
- functions
- variables
- classes
- executable code

Modules exist for ONE BIG REASON:
👉 Code organization + code reuse

If your codebase grows and everything stays in one file,
you're not programming — you're creating chaos.
"""

# =========================================================
# WHY MODULES EXIST (REAL TALK)
# =========================================================
"""
Imagine:
- One file
- 5,000 lines
- No separation
- Debugging nightmare

Modules solve:
- Readability
- Maintainability
- Reusability
- Team collaboration

Industry rule:
"One responsibility → One module"
"""


# =========================================================
# WHAT HAPPENS WHEN YOU IMPORT A MODULE?
# =========================================================
"""
VERY IMPORTANT (INTERVIEW QUESTION):

When you do:
    import math

Python does:
1. Searches for math module 
2. Loads it into memory
3. Executes ALL top-level code in math.py ONCE
4. Creates a module object
5. Binds name 'math' to that object

Important:
- Importing same module again does NOT reload it
- Python caches modules in sys.modules
"""

"""
More Explanation:
=============================================================================
WHEN YOU WRITE import module_name:

1. Python SEARCHES for the module
    Python asks:
        “Bro… where is math?”
    It looks in a fixed order (this is interview gold):
        1. Current file's directory
        2. Paths in PYTHONPATH
        3. Standard library directory
        4. site-packages (third-party libs)
    You can literally SEE this list: 
        import sys
        print(sys.path)

💀 Big mistake people make
If you create a file called math.py, Python will import your file, not the real math module.

-------------------------------------------------------------------------------

2. Python LOADS the module into memory 
    Once Python finds math:
    -> It reads the module file (or C-extension for built-ins)
    -> Allocates memory for it
    -> Prepares a namespace (a box to store stuff)
        Think of it like:
        “Okay, I'll reserve RAM for this thing.”

⚠️ Important:
This does NOT mean your code can use it yet
It's just loaded, not connected

-------------------------------------------------------------------------------

3. Python EXECUTES all top-level code in the module

Top-level code = any code that runs immediately when the file is read

In a Python file, there are two kinds of code:

    1. Top-level code ✅ (runs on import)
        print() statements
        variable assignments
        function definitions (not execution)
        class definitions 
        loops written directly in the file
    2. Non top-level code ❌ (does NOT run on import)
        code inside functions
        code inside methods (methods = functions inside classes)
    Python only executes top-level code automatically.

Let's see this with a simple file

Imagine a file called demo.py:

        print("I am top-level")
        x = 10
        def func():
            print("Inside function")
        class Test:
            print("Inside class")

Now in another file:
import demo

What prints?
    I am top-level
    Inside class (classes run at import time)

What DOES NOT print?
    Inside function

WHY did this happen? 🤔
    Because Python did this during import:
    -> Read demo.py from top to bottom
    -> Execute everything that is NOT inside a function
    -> Define functions (but don't run them)
    -> Define classes (⚠️ class body does run)

NOTE 
Class bodies execute at import time
This shocks people.
    class A:
        print("Hello")
This prints during import, because: A class body is executed to create the class
Only methods inside it are delayed
So:
    import file_with_class 
    ➡️ class body runs
    ➡️ methods don't


🔥 Important bombshell:

Python executes top-level code only the FIRST time a module is imported.

Why?
    Because Python caches modules.

Internally:
    sys.modules["demo"] = <module object>

Next time Python sees:
    import demo
It says:
    “Already loaded. Not running that again.”

-------------------------------------------------------------------------------

4. Python CREATES a module object
    After executing top-level code,
    Python creates a module object in memory.
    This object holds:
        - All functions
        - All variables
        - All classes defined in the module

    for math module: its like 
    math = {
        'sqrt': <function object>,
        'pi': 3.14159,
        ...
    }
    NOTE the object contains are like above are in C for built-in modules

-------------------------------------------------------------------------------

5. Python BINDS the module name to that object, like math for the math module
    This is why you can do:
        import math
        print(math.pi), its literaly saying: <module object>['pi']

-------------------------------------------------------------------------------

SUMMARY:
- When a module is imported, Python runs all the code in that module.
- This means any top-level statements (not inside functions/classes) will execute.
- This is why we use the `if __name__ == "__main__":` guard
  to prevent certain code from running on import.
"""


# =========================================================
# TYPES OF MODULES 
# =========================================================
"""
1. Built-in modules  
   - math, random, sys, os, time 

2. Standard Library modules 
   - collections, itertools, functools

3. User-defined modules
   - your own .py files

4. Third-party modules
   - numpy, pandas, flask (installed via pip)
"""


# =========================================================
# BASIC IMPORT
# =========================================================
import math

print("Square root:", math.sqrt(16))
print("Pi:", math.pi)
print("Euler's number:", math.e)


# =========================================================
# IMPORT WITH ALIAS (as keyword) 
# =========================================================
"""
Why aliasing?
- Shorter names
- Cleaner code
- Avoid long prefixes
"""

import math as m

print("sqrt:", m.sqrt(25))
print("pi:", m.pi)


# =========================================================
# FROM ... IMPORT (SELECTIVE IMPORT)
# =========================================================
"""
from module import name

Pros:
- Less typing
- Cleaner syntax

Cons:
- Namespace pollution
- Name conflicts
"""

# what is namespace pollution?
"""
First: what is a namespace?
    A namespace is just a fancy word for:
    “The place where names live.”

example:
    x = 10
    print(x)
Here, x lives in your current namespace.
and print lives in python's built-in namespace.

Think of a namespace like a room full of labeled boxes.
Each label (name) points to something (function, variable, class).

so what is namespace pollution?
Your namespace gets cluttered with too many names,
and some names start colliding, overwriting, or confusing each other.

This can lead to:
- Confusion: Which 'sqrt' are we using?
- Conflicts: Two names clash
- Harder debugging

"""

from math import factorial, pow, e

print("5! =", factorial(5))
print("2^3 =", pow(2, 3))
print("e =", e)


# =========================================================
# NAME CONFLICT PROBLEM (VERY IMPORTANT)
# =========================================================
"""
If two modules have same function name:
- One import can overwrite another
- Debugging becomes painful

Example:
math.pow vs built-in pow
"""

# Solution → aliasing
from math import sqrt as square_root
from math import pi as PI_VALUE

print(square_root(36))
print(PI_VALUE)


# =========================================================
# HOW PYTHON FINDS MODULES (INTERVIEW FAVORITE)
# =========================================================
"""
Python searches modules in this order:

1. Current directory
2. PYTHONPATH
3. Standard library directories 
4. Site-packages (third-party)

You can inspect this using:
"""

import sys
# print(sys.path)


# =========================================================
# help() AND introspection
# =========================================================
"""
help("modules"):
- Lists all available modules

help(module):
- Shows documentation
- Lists functions & classes
"""

# help(math)


# =========================================================
# BEST PRACTICES 
# =========================================================
"""
1. Prefer:
   import module
   module.function()

2. Avoid:
   from module import *

3. Use aliases only when standard (np, pd, plt)

4. One module = one responsibility

5. Keep imports at TOP of file 
"""


# =========================================================
# REAL-WORLD EXAMPLE
# =========================================================
"""
Project structure:

project/
│
├── main.py
├── utils.py
├── math_helpers.py
├── data_loader.py

This is how real software is written. 
"""


# =========================================================
# COMMON MISTAKES (EXAM GOLD)
# =========================================================
"""
1. Importing inside loops ❌
2. Using wildcard imports ❌
3. Circular imports ❌
4. Confusing module with package ❌
5. Naming your file same as built-in module ❌ (math.py 😭)
"""


# =========================================================
# MODULE vs PACKAGE (BONUS)
# =========================================================
"""
Module:
- Single .py file

Package:
- Folder containing __init__.py
- Can contain multiple modules
"""


print("END OF MODULES CONCEPTS")
