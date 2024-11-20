
collection = ("ujj","ram","mum")

for el in collection :
    print(el)

# it is more like for each loop of cpp

# we can traverse on string as well
str = "ujjwal"

for ch in str : 
    print(ch)

print()

"""
in cpp we use to write for loop like : for (i = 0;  i<n; i++), similarly in python we can write like : for i in range(0,n,1)
"""

# print even number
for x in range(0,10,2) :
    print(x)  # 0,2,4,8

print()

for x in range(10) : 
    print(x) # print 0 to 9


# using for loop to search in a list
list = [1,2,3,4,5,5,6,7,8,8,9]

# searching for x
x = int(input("enter the target : "))
flag = None
for i in range(0,len(list),1) :
    if x == list[i] :
        print("target found at index",i)
        flag = True
        break

if flag == None : 
    print("target not found")


# how range function works
num = range(10) # now we can traverse through num and get all 0 to <10
for el in num : 
    print(el)

# range (start, stop, steps)
# range (start, stop) , then default step is 1

# print number from 10 to 1 using for loop
for i in range (10, 0, -1) : 
    print(i)


