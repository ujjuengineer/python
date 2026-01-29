"""
========================================
VARIABLE SCOPE & SCOPE RESOLUTION (LEGB)
========================================

VARIABLE SCOPE:
Scope means:
→ WHERE a variable is visible
→ WHERE it can be accessed 
→ WHERE Python is allowed to use it 

Python is VERY strict about scope.
If a variable is not in scope → Python says: ❌ NameError 
"""

# -----------------------------------------
# SCOPE RESOLUTION RULE – LEGB
# -----------------------------------------

"""
When Python encounters a variable name,
it searches for it in this exact order:

LEGB Rule:
L → Local
E → Enclosing
G → Global
B → Built-in

Python stops at the FIRST match it finds.
This search happens at RUNTIME.
"""

# -----------------------------------------
#  1. LOCAL SCOPE
# -----------------------------------------

"""
LOCAL SCOPE:
Variables created INSIDE a function.

Lifetime:
- Created when function is called
- Destroyed when function ends

Accessibility:
- ONLY inside that function
"""

def my_function():
    x = 10  # local variable
    print("Inside function, x =", x)

my_function()

# print(x)  # ❌ NameError: x is not defined

"""
WHY ERROR?

Because:
- x exists ONLY inside my_function
- Once function execution ends, x is gone

Local variables are memory-safe & temporary.
This prevents accidental misuse.
"""

# -----------------------------------------
#  2. ENCLOSING SCOPE
# -----------------------------------------

"""
ENCLOSING SCOPE:
Happens in NESTED FUNCTIONS. 

Definition:
Variables defined in an outer function 
but used inside an inner function. 

This is NOT global.
This is NOT local to inner.
This is ENCLOSING.
"""

def outer_function():
    y = 20  # enclosing variable

    def inner_function():
        print("Inside inner function, y =", y)

    inner_function()

outer_function()

# print(y)  # ❌ NameError


"""
IMPORTANT INSIGHT:

inner_function does NOT have y locally.
Python checks:
- Local? ❌
- Enclosing? ✅ FOUND
- Stops search.

This is how closures work in Python.
Closures are used heavily in decorators & callbacks.
"""

# -----------------------------------------
# ENCLOSING SCOPE IS READ-ONLY BY DEFAULT
# -----------------------------------------



"""
NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
Inner functions can READ enclosing variables,
but cannot MODIFY them unless declared using 'nonlocal'.
"""

def outer():
    count = 0

    def inner():
        # count += 1  # ❌ UnboundLocalError : NOTE THIS
        print(count)

        """
        WHY ERROR IF WE TRY TO MODIFY?
        Python assumes:
            - Any assignment creates a LOCAL variable 
            So count becomes local to inner 
        
        now you must be thinking if count become local to inner then it must print the count
        Right ?

        Before your code even runs, Python scans the function and says:
            “Oh, you are assigning to count inside this function?
            Cool, then count is a LOCAL variable here.”

        now count += 1 means => count = count + 1

        Python thinks:
            count is LOCAL (because of assignment)
            But you're trying to read it first (count + 1)
            That local count has no value yet
        
        So Python is like:
            “Bro… you're using a local variable before assigning it.”
            💥 UnboundLocalError

        if you do something like count = 6, then it creates a local count and it doesn't affect the value of outer count variable
        """
        
    inner()

outer()


"""
Python assumes:
- Any assignment creates a LOCAL variable
So count becomes local to inner → conflict.

Solution: nonlocal keyword.
"""

print(); print(); print()

def outer_fixed():
    count = 0

    def inner():
        nonlocal count 
        count += 1 # this changes the enclosing variable, not creates a new local variable
        print("Count =", count)

    inner() # print count = 1
    inner() # print count = 2
    inner() # print count = 3

outer_fixed()

"""
nonlocal tells Python:
"Hey, use enclosing scope variable, not local"
"""

print(); print(); print()
# -----------------------------------------
#  3. GLOBAL SCOPE
# -----------------------------------------

"""
GLOBAL SCOPE:
Variables defined outside all functions.

Accessible:
- Anywhere in the file
- Inside functions (READ-only by default)

Lifetime:
- Exists as long as program runs
"""

z = 30  # global variable

def show_global():
    print("Global z =", z)

show_global()

"""
READING global variables is allowed.
MODIFYING is NOT (unless declared global).
"""

def modify_global():
    # z += 1  # ❌ UnboundLocalError
    pass

"""
Why?
Same rule: assignment = local variable creation 
"""

def modify_global_fixed():
    global z
    z += 1 # z become 31
    print("Modified z =", z) # 31

modify_global_fixed()

show_global() # now z become 31 after modifying

"""
⚠️ PROFESSOR OPINION:
Using 'global' is usually BAD practice.

Why?
- Makes debugging harder
- Creates hidden dependencies 
- Breaks modular design

Use function parameters instead.
"""

# -----------------------------------------
#  4. BUILT-IN SCOPE
# -----------------------------------------

"""
BUILT-IN SCOPE: 
Names that Python provides by default. 

Examples:
print, len, sum, int, str, list, dict, etc.

These live in the builtins module.
"""

print(len("Python"))

"""
LEGB final step:
If Python doesn't find variable in:
Local → Enclosing → Global
It checks Built-in.

If not found → NameError
"""

# -----------------------------------------
# NAME SHADOWING (VERY IMPORTANT)
# -----------------------------------------

"""
If you create a variable with same name
as a built-in function, you SHADOW it.
"""

len = 10
# print(len("hello"))  # ❌ TypeError

"""
You just murdered len().
This is why naming matters.
"""

# -----------------------------------------
# LEGB SEARCH FLOW (MENTAL MODEL)
# -----------------------------------------

"""
Example:

x = 100

def outer():
    x = 200
    def inner():
        x = 300
        print(x)

    inner()

outer()

Search inside inner():
Local x → 300 ✅
Stops immediately.

Change print(x) to use nonlocal/global 
and behavior changes.
"""

# -----------------------------------------
# FINAL PROFESSOR TAKE 
# -----------------------------------------

"""
If you understand scope:
- You avoid silent bugs
- You write predictable code
- You understand closures & decorators
- You pass interviews confidently 

LEGB is NOT theory.
It runs every time Python executes your code.

Master this once → benefit forever.
"""
