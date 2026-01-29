# instance variables : variables that are unique to each instance of a class, they are defined inside the constructor using self



# class variables : variables that are shared among all instances of a class, they are defined outside the constructor 
# you can access class variables using objects but it is recommended to access them using the class name



class Student:

    # class variable
    school_name = "ABC High School" # this variable is shared among all objects of the Student class 
    num_students = 0 # to keep track of number of students created

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
        Student.num_students += 1 # incrementing the class variable whenever a new student is created



student1 = Student("Alice", 16)
student2 = Student("Bob", 17)


# accessing the class varibale
print(student1.school_name)  # Output: ABC High School
print(student2.school_name)  # Output: ABC High School

# but it is recommended to access class variables using the class name
print(Student.school_name)    # Output: ABC High School
print(Student.num_students)  # Output: 2