light = "green"

if(light == "red") : 
    print("stop")
elif(light == "green") : 
    print("go")
else : 
    print("stop")

print()

# a varible defined inside of if,else can be used outside of it unlike of c++ or java

marks = 50
if(marks >90): 
    grade = 'A'
elif(marks > 80) : 
    grade = 'B'
elif(marks > 80) : 
    grade = 'C'
else : 
    grade = "fail"

print("the grade of the student is :",grade)
print()

# there is no {} used for combining 2 statements in python, we have to use indentetion to keep it proper
age = 35
if(age >= 18):
    if(age > 30): 
        print("he/she can drive a car")
    else:
        print("he/she can only drive bike")
else:
    print("he can't drive")
