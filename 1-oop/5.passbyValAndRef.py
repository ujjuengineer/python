"""
PASS BY VALUE vs PASS BY REFERENCE IN PYTHON
===========================================

IMPORTANT TRUTH (READ THIS FIRST)
-----------------------------------
Python is NEITHER pass by value NOR pass by reference.

Python is:
👉 PASS BY OBJECT REFERENCE
(also called: Call by Sharing)

------------------------------------------------
1. WHAT ACTUALLY HAPPENS WHEN YOU PASS A VARIABLE
------------------------------------------------
When you pass a variable to a function:
- Python passes the REFERENCE to the OBJECT
- NOT a copy of the value
- NOT the original variable itself

So:
- The function gets access to the SAME OBJECT
- But it CANNOT rebind the caller's variable

------------------------------------------------
2. IMMUTABLE OBJECTS (Behaves like Pass by Value)
------------------------------------------------
Immutable objects:
- int
- float
- str
- tuple
- bool

Example:
    def change(x):
        x = x + 1

    a = 10
    change(a)
    print(a)   # 10

WHY?
- x initially points to the SAME object as a
- x + 1 creates a NEW object
- x now points to a new object
- a is untouched

Memory view:
    a  → 10
    x  → 10  → reassigned to 11 (new object)

This LOOKS like pass by value
BUT it's not — it's object reference + immutability.

------------------------------------------------
3. MUTABLE OBJECTS (Behaves like Pass by Reference)
------------------------------------------------
Mutable objects:
- list
- dict
- set
- custom objects (most of the time)

Example:
    def change(lst):
        lst.append(100)

    a = [1, 2, 3]
    change(a)
    print(a)   # [1, 2, 3, 100]

WHY?
- lst and a refer to the SAME list object
- append() mutates the object
- change is visible outside the function

Memory view:
    a  → [1, 2, 3]
    lst → SAME object → modified

This LOOKS like pass by reference.

------------------------------------------------
4. REBINDING vs MUTATING (KEY DIFFERENCE ⭐)
------------------------------------------------
Rebinding:
    x = new_object
    ❌ does NOT affect caller

Mutating:
    x.append(), x[key] = value
    ✅ affects caller

Example:
    def test(lst):
        lst = [9, 9, 9]   # rebinding
    a = [1, 2]
    test(a)
    print(a)   # [1, 2]

But:
    def test(lst):
        lst.append(9)    # mutation
    a = [1, 2]
    test(a)
    print(a)   # [1, 2, 9]

------------------------------------------------
5. PASS BY VALUE? PASS BY REFERENCE? FINAL ANSWER
------------------------------------------------
Python:
❌ NOT pass by value
❌ NOT pass by reference
✅ PASS BY OBJECT REFERENCE

The behavior depends on:
- Whether the object is mutable
- Whether you mutate or reassign

------------------------------------------------
6. REAL INTERVIEW ONE-LINER 🚀
------------------------------------------------
"Python uses pass by object reference.
Mutable object changes persist, reassignment does not."

Say this and move on 😤

------------------------------------------------
7. HOW TO AVOID SIDE EFFECTS
------------------------------------------------
If you DON'T want changes:
- Pass a copy

Examples:
    change(a.copy())
    change(list(a))
    change(dict(a))

------------------------------------------------
8. COMMON CONFUSION TRAP ⚠️
------------------------------------------------
Example:
    def change(x):
        x += 1

    a = 10
    change(a)
    print(a)  # 10

+= behaves like:
- mutation for mutable
- rebinding for immutable

------------------------------------------------
9. TL;DR (SAVE THIS IN BRAIN 🧠)
------------------------------------------------
✔ Functions receive object references
✔ Immutable → safe
✔ Mutable → dangerous
✔ Reassignment ≠ mutation
✔ Python = Call by Sharing

------------------------------------------------
END OF NOTES
------------------------------------------------
"""


# when you create a custom object of yourself, it is always mutable, i.e,. if you pass it in function and make changes in it from there, it will affect in your original object