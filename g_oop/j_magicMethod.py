# magic method : special methods which have double underscores at the beginning and end of their names
#                also known as dunder methods (double underscore methods)
#                they are automatically called by many of python's built-in operators
#                they allow you to define or customise the behavior of objects 
print("=================================================================================") 


class Book :
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages


book1 = Book("kalu badmosh", "George Orwell", 328)
book2 = Book("billu badmosh", "Harper Lee", 281)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)

# if you print the object print(book1), by default it will show the memory address of the object
# but you can change this behavior by defining the __str__ method in the class
print(book1)  # Output: 'kalu badmosh' by George Orwell
print(book2)  # Output: 'billu badmosh' by Harper Lee



print("=================================================================================") 


# if you try to book1 == book2, by default it will compare the memory addresses of the objects
# but you can change this behavior by defining the __eq__ method in the class
print(book1 == book2)  # Output: False
print(book1 == book1)  # Output: True

print("=================================================================================")


# if you try to compare two objects using <
# by default it will raise an error
# but you can change this behavior by defining the __lt__ method in the class
print(book2 < book1)  # Output: True (281 < 328)
print(book2 < book3)  # Output: True (180 < 281)

# similarly for > you can define __gt__ method
# for <= you can define __le__ method
# for >= you can define __ge__ method
# for + you can define __add__ method
# for - you can define __sub__ method
# and many more magic methods are available in python 