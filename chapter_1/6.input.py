input("enter your fav fruits : ")

# we can store the input
name = input("enter your name: ")
print("welcome", name)
print()

# note that the input value is always a string, so we have to type caste according to your use
age = input("enter your age: ")
print("type of input age before typecaste: ",type(age)) # string
age = int(age)
print("type of input age after typecaste: ", type(age))
