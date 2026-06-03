# how default arguments are evaluated in python 

"""
In Python, default arguments are evaluated only once, at the exact moment the function is defined, not when the function is called.

This causes a legendary behavior (and frequent bug) when you use a mutable object—like a list or a dictionary—as a default argument. 
Because that list is created only once, every single function call shares that exact same list in memory.
"""

def add_to_checklist(item, checklist=[]):
    checklist.append(item)
    return checklist

# Call 1: Looks completely normal
print(add_to_checklist("Buy milk"))  
# Output: ['Buy milk']

# Call 2: Wait, where did milk come from?
print(add_to_checklist("Wash car"))  
# Output: ['Buy milk', 'Wash car']

# Call 3: It keeps growing!
print(add_to_checklist("Pay bills")) 
# Output: ['Buy milk', 'Wash car', 'Pay bills']

"""
When Python compiled your code and saw checklist=[], it created one list hidden away in your system memory.

On Call 1, you didn't pass a custom checklist, so Python pointed to that hidden list and appended "Buy milk".

On Call 2, you didn't pass a custom checklist again. Python pointed to that same hidden list. It already contained "Buy milk", so "Wash car" was simply tacked onto the end.
"""


"""
If you want a fresh, clean, empty list created every single time the function is invoked, the universal best practice in Python is to set the default argument to None
"""