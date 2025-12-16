# typecasting 
# typecasting is the process of converting one data type to another
# int() - converts to integer
# float() - converts to float
# str() - converts to string
# bool() - converts to boolean

# example of typecasting
a = "123"
b = int(a)
print(b)
print(type(b))

c = 123
d = str(c)
print(d)
print(type(d))

e = 123.45
f = int(e)
print(f)
print(type(f))

g = 0
h = bool(g)
print(h)
print(type(h))

# how stirng works with boolean typecasting
str1 = ""
str2 = "Hello"
bool1 = bool(str1)  # empty string converts to False
bool2 = bool(str2)  # non-empty string converts to True
print(bool1)
print(bool2)
print(type(bool1))
print(type(bool2))