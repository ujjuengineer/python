"""

What is __name__?
__name__ is a special built-in variable that Python automatically creates for every module (file). Its value depends on how the file is being used:

-> If the file is run directly: __name__ is set to "__main__"
-> If the file is imported: __name__ is set to the module's name (the filename without .py)

more presicesly 
if we execute any code or function of this file directly then value of __name__ = __main__ 
and if we import this file to another file and execute the function of this file through another file then the value of __name__ become 'script1'

"""

def greet() :
    print(f"the value of __name__ is {__name__}")


# if we directly execute this file then this if condition satisfy and it will execute the greet() and print value of name as main

if __name__ == "__main__" :
    greet()

# but if we import this file to script2 and from there execute greet() then it will print value 'script1'


"""
The pattern:
    if __name__ == "__main__":
        # Code here only runs when file is executed directly
        # Does NOT run when file is imported

This is a CONDITIONAL CHECK that asks:
"Am I the main program being run, or am I being imported?"

"""