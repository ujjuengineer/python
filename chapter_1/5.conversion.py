# type conversion and type casting is 2 different thing, conversion is automatic process which compiler performs, whereas type casting is done by users manually

# type concersion
a,b = 1,3.5

sum = a + b # here compiler automatic convert int a into float and add to b
print("sum :",sum)

"""
a = "2"
b = 4.69
and if we add a + b, this will show error, so we can first typecaste a and then add to b

"""

print()
a = "2"
b = 4.69
print("type of a before conversion",type(a))
a = int(a) # c++ me c = (int)a krte hai

'''
note that in cpp we can't convert string into integer using (int)str, we have to use stoi(str) to convert a string into an integer
'''

print("type of a after conversion",type(a))
print()

print(a)



