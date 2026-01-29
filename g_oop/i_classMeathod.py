# static method and class method in OOP 

# static method : a method that belongs to the class rather than any specific instance of the class
#                 usually used for general utility function 

# instance method : best for operations that require access to instance-specific data
# static method : best for utility functions that don't need access to instance or class data

class Employee: 
    def _init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}")

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer", "Intern"]
        return position in valid_positions
    

# using the static method
print(Employee.is_valid_position("Developer"))  # Output: True
print(Employee.is_valid_position("CEO"))        # Output: False 
# you don't need to create an object to use static method



print(); print()
# class method : a method that belongs to the class rather than any specific instance of the class
#                it takes cls as the first parameter instead of self

class Student:
    school_name = "ABC High School"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name


# you can directly call class method without creating an object
print(Student.school_name)  # Output: ABC High School
Student.change_school_name("XYZ High School")
print(Student.school_name)  # Output: XYZ High School