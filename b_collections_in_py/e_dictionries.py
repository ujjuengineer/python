"""
===========================================================
        PYTHON COLLECTIONS : DICTIONARY 
===========================================================

CORE IDEA:
----------
A dictionary is a collection of key : value pairs.

Think of it as:
- A real-world dictionary (word -> meaning)
- A database row (primary_key -> data)
- A hash table (THIS IS IMPORTANT)

-----------------------------------------------------------
BASIC PROPERTIES 
-----------------------------------------------------------

Dictionary:
- Written using {}
- Structure: {key: value}

Properties:
- Mutable (can add, remove, update)
- Keys must be UNIQUE
- Keys must be IMMUTABLE
- Values can be anything (mutable or immutable)
- Insertion ordered (Python 3.7+)

Internally:
- Dictionary is implemented using a HASH TABLE
"""

# =========================================================
# WHY KEYS MUST BE IMMUTABLE?
# =========================================================
"""
Keys are hashed internally.

Hash table logic:
    key --hash()--> index in memory

If a key changes after insertion:
- Hash value changes
- Dictionary breaks
- Data becomes unreachable

Hence:
- Allowed keys: int, float, str, tuple (if immutable)
- NOT allowed: list, set, dict
"""

# =========================================================
# CREATING A DICTIONARY
# =========================================================

capitals = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin"
}

print(capitals)
print(type(capitals))

print()

# =========================================================
# ACCESSING VALUES
# =========================================================
"""
Two ways to access values:

1. dict[key]
   - Fast
   - Raises KeyError if key not found

2. dict.get(key)
   - Safe
   - Returns None (or default) if key not found
   - you can provide a default value so that in case key not found, it returns default value instead of none

BEST PRACTICE:
Use get() when key may not exist
"""

print(capitals["India"])
print(capitals.get("USA"))
print(capitals.get("Italy"))          # None
print(capitals.get("Italy", "N/A"))   # Default value

print()
# =========================================================
# ADDING & UPDATING KEY-VALUE PAIRS
# =========================================================
"""
Assignment method:
- Adds new key if not present
- Updates value if key exists
"""

capitals["Italy"] = "Rome"

"""
update():
- Can add multiple key-value pairs
- Accepts dict or iterable of pairs 
"""

capitals.update({"Spain": "Madrid"})
capitals.update([("Portugal", "Lisbon")])

print("capital after updating : ",capitals)

print()

# =========================================================
# REMOVING ELEMENTS
# =========================================================
"""
pop(key):
- Removes specified key
- Returns its value
- Raises KeyError if key not found, so better to check using 'in' before using pop
"""

removed = capitals.pop("France")
print("Removed:", removed)

"""
popitem():
- Removes LAST inserted key-value pair (Python 3.7+)
- Earlier versions removed arbitrary element
- Useful for stack-like behavior
"""

capitals.popitem()

"""
clear():
- Empties dictionary
- Keeps same object reference
"""

capitals.clear() 
print(capitals)

print()
# =========================================================
# RECREATING FOR ITERATION EXAMPLES
# =========================================================

capitals = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin"
}


# =========================================================
# ACCESSING KEYS, VALUES, ITEMS
# =========================================================
"""
keys(), values(), items():
- Return VIEW objects (not lists)
- Views are dynamic (auto-update)
"""

keys = capitals.keys()
values = capitals.values()
items = capitals.items()

print(keys)
print(values)
print(items)

print()
# =========================================================
# ITERATING OVER DICTIONARY
# =========================================================
"""
Iterating over keys (default behavior):
"""

for key in capitals:
    print(key)

print()

"""
Iterating explicitly over keys:
"""

for key in capitals.keys():
    print(key)

print()

"""
Iterating over values:
"""

for value in capitals.values():
    print(value)

print()

"""
Iterating over key-value pairs:
"""

for item in capitals.items():
    print(item)   # tuple (key, value)

print()

"""
Unpacking key-value pairs (MOST USED):
"""

for key, value in capitals.items():
    print(f"Key: {key}, Value: {value}")


# =========================================================
# TIME COMPLEXITY (INTERVIEW FAV)
# =========================================================
"""
Average Case:
- Insert: O(1)
- Delete: O(1)
- Search: O(1)

Worst Case (hash collision):
- O(n)

This is why dictionaries are insanely powerful.
"""


# =========================================================
# COMMON MISTAKES (VERY IMPORTANT)
# =========================================================
"""
1. Using mutable objects as keys ❌
2. Expecting dict to be sorted by value ❌
3. Using [] instead of get() blindly ❌
4. Assuming popitem() removes random element in modern Python ❌
5. Modifying dict while iterating ❌
"""


# =========================================================
# WHEN TO USE DICTIONARY?
# =========================================================
"""
Use dictionaries when:
- You need fast lookups
- Data is mapped (key -> value)
- Uniqueness of keys matters
- Performance is critical
"""

print("END OF DICTIONARY")
