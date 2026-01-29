# alising 
a = 5
b = 5

print(id(a))
print(id(b))

"""

Topic:
- Why id(a) == id(b) even when a and b are different variables
- Object identity vs value equality
- Python integer caching & optimizations

------------------------------------------------
1. VARIABLES VS OBJECTS
------------------------------------------------
In Python:
- Variables do NOT store values
- Variables store REFERENCES to objects

Example:
    a = 10

'a' is just a label pointing to an integer object (10) in memory.

------------------------------------------------
2. WHAT DOES id() DO?
------------------------------------------------
id(x) returns:
- The memory address (identity) of the object x refers to

Example:
    id(a)  -> memory location of object referenced by 'a'

If two variables point to the same object:
    id(a) == id(b)

------------------------------------------------
3. WHY id(a) == id(b) FOR THIS CODE?
------------------------------------------------
Code:
    a = 999999
    b = 999999

Explanation:
- Integers are IMMUTABLE in Python
- Python may REUSE existing immutable objects to save memory
- Both 'a' and 'b' point to the SAME integer object

Memory view:
        999999  (single object)
         ↑   ↑
         a   b

Hence:
    id(a) == id(b)

------------------------------------------------
4. INTEGER CACHING RULE (IMPORTANT)
------------------------------------------------
Python GUARANTEES caching only for:
    integers from -5 to 256

Example:
    a = 100
    b = 100
    id(a) == id(b)   # Always True

For numbers OUTSIDE this range (like 999999):
- Caching is NOT guaranteed
- Depends on:
    - Python version
    - Interpreter (CPython)
    - Execution context

But CPython often still reuses them as an optimization.

------------------------------------------------
5. FORCING A NEW INTEGER OBJECT
------------------------------------------------
Example:
    a = 999999
    b = int("999999")

Here:
- a is a constant
- b is created at runtime

Result:
    id(a) != id(b)

------------------------------------------------
6. == VS is  (VERY IMPORTANT)
------------------------------------------------
==  → compares VALUES
is  → compares MEMORY ADDRESSES (identity)

Example:
    a = 999999
    b = 999999

    a == b   # True  (same value)
    a is b   # May be True or False (same object or not)

RULE:
 Never use `is` for numbers or strings
 Use `==` for value comparison

------------------------------------------------
7. WHY PYTHON DOES THIS?
------------------------------------------------
- Memory efficient
- Faster execution
- Better garbage collection
- Safe because integers are immutable

Python basically says:
"Why create the same number again if I already have it?"

------------------------------------------------
8. FINAL TAKEAWAYS
------------------------------------------------
✔ Variables are references, not containers
✔ id() shows object identity, not value
✔ Python may reuse immutable objects
✔ Same id == same object
✔ This behavior is normal and intentional

------------------------------------------------
END OF NOTES
------------------------------------------------
"""
