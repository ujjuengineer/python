# arithematic operators in Python 
# + : addition
# - : subtraction
# * : multiplication
# / : division
# % : modulus (returns the remainder)
# ** : exponentiation (power)
# // : floor division (returns the largest integer less than or equal to the division result)


a = 10
b = 3

# +  Addition
print(a + b)      # 13

# -  Subtraction
print(a - b)      # 7

# *  Multiplication
print(a * b)      # 30

# /  Division (ALWAYS gives float)
print(a / b)      # 3.3333333333333335

# %  Modulus (remainder)
print(a % b)      # 1

# ** Exponentiation (power)
print(a ** b)     # 1000

# // Floor 
print(a // b)     # 3


# IMPORTANT NOTE:
# // does FLOOR division, not truncation
print(-7 // 2)    # -4 (not -3)


#  Augmented Assignment Operators

x = 5

x += 2    # x = x + 2
print(x)  # 7

# similarly we can do with other operators


# Built-in Math Functions

# round()
# Rounds to nearest integer
print(round(3.14))   # 3
print(round(3.67))   # 4

# Banker’s rounding (IMPORTANT) : When the number is exactly .5, Python rounds to the NEAREST EVEN number
print(round(2.5))    # 2
print(round(3.5))    # 4

# Round till decimal places
print(round(3.14159, 2))  # 3.14


# abs()
# Absolute value (distance from 0)
print(abs(-5.8))     # 5.8
print(abs(5))        # 5


# pow()
# Same as ** but more powerful
print(pow(2, 3))        # 8
print(pow(2, 3, 5))     # (2^3) % 5 = 3  -> very useful in DSA


# max()
# Returns largest value
print(max(3, 7, 2))                 # 7
print(max([10, 20, 5, 8]))          # 20


# min()
# Returns smallest value
print(min(3, 7, 2))                 # 2
print(min([10, 20, 5, 8]))          # 5



# 1. Use // carefully with negative numbers
# 2. pow(a, b, mod) avoids overflow in large exponentiation 
# 3. / gives float, // gives int (floor)


