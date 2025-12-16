# logical operators : and , or , not
# or : returns True if at least one operand is True
# and : returns True only if both operands are True
# not : returns the opposite boolean value of the operand

a = True
b = False

# or operator
print(a or b)  # True
print(b or b)  # False

# and operator
print(a and b) # False
print(a and a) # True

# not operator
print(not a)   # False
print(not b)   # True