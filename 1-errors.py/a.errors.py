# IndexError : when you access index out of range 
# KeyError : when you access a key which doesn't exist
# NameError : when you try to access or print unknown/undefined variable
# AttributeError : when you try to access an attribute of any class which doesn't exist
# NotImplementedError : you can use this error when you are in development phase 

# RuntimeError : this is base error, and other errors inherit from this, its basically error when you are running your program. so it can be anything

# SyntaxError : when you write wrong syntax of python
# IndentationError : more like a syntax error, when you write loop or funciton

# TabError : if you are using tab for indentation inside a one funciotn then stick to that, don't use spacebar for the indentation in another function, it may cause this error

# TypeError : when you try to add 2 different classes, like when you add str and int 
# ValueError : when you pass invalid input, see the example

# ImportError : when you import a file "x" into file "y" and file "y" is also been imported to file "x"
                # this will cause importerror

# DeprecationWarning : you can raise a deprecationwarning for something which still works but it's not a proper way do that !!



# example of not implemented error

class User : 
    def __init__ (self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        raise NotImplementedError("this feature has not been implemented yet.")
    
user = User('ujju', 'don')
# user.login() # this will raise the unimplemented error




# value error 
a = int(7.6)
print(a)

a = int('45')
print(a)

a = int('3.4') # this will give the value error
print(a) 