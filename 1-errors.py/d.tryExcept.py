class User : 
    def __init__ (self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        raise NotImplementedError("this feature has not been implemented yet.")
    
user = User('ujju', 'don')


# if you try to directly run this block of code, then it will raise the error and crash your program
# user.login() # this will raise the unimplemented error

# so we use try and except block, so that if any error occured then instead of crashing the code it will show the error

try :
    user.login()
except NotImplementedError :
    print("This feature is not been implemented yet !")

# this will only catch the specified error, if any other error occurred then it will crash the code base

print()

# you can extend the try and except block with various errors
try :
    user.login()
except NotImplementedError:
    print("this features is not implemented !")
except ValueError:
    print("Invalid value !")
finally:
    print("code execution finished !")

# the except blcok may or may not run but the finally block will always run, no matter error catched or not

print() 



# if you want to raise the error through the except block, you can do something like this
"""
try : 
    user.login()
except NotImplementedError:
    print("Not implimented !")
    raise

"""
# this will show the error 


# if you want to execute somehting only if error doesn't happen, then you can use else
try:
    print("hello world")
except NotImplementedError:
    print("not executed")
else:
    print("executed successfully !")
# else block only runs if try block will execute otherwise it will not run 