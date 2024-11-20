
i = 1
while i<=5 :
    print("hello world", i)
    i += 1

print("loop ended") #loop ke bahar aa gya
print()

# search for a value x in the given tuple
tup = (1,4,9,16,25,36,49,64,81,100)


size = len(tup)
flag = None

x = int(input("enter the number : ")) # note input is always string, so don't forget to typecast it into int

i = size - 1
while i >= 0 :
    if tup[i] == x :
        print("target found at index",i)
        flag = 1
        break
    i-=1

if(flag == None) :
    print("target not found")