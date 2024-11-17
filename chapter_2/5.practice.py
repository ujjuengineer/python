# wap to check wether entered number is odd or even
a = int(input("enter a number:"))
if(a%2 == 0):
    print("even number")
else: 
    print("odd number")

print()

# wap to check if given number is multiple of 7 or not
if(a%7==0): print(a,"is multiple of 7")
else : print(a,"is not multiple of 7")
print()

# wap to find greates of 3 number
b = int(input("enter second number "))
c = int(input("enter 3rd number "))
if(a>b) :
    if(a>c) : greatest = a
    else : greatest = c
else: 
    if(b>c): greatest = b
    else: greatest = c

print("greatest of",a,b,c,"is",greatest)