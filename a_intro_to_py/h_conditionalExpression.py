# conditional expression : one line short-cut for the if-else statement, similar to ternary operator
# syntax : value_if_true if condition else value_if_false

# example 1
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult      

# example 2
num = 15
parity = "Even" if num % 2 == 0 else "Odd"
print(parity)  # Output: Odd