from script1 import *

greet() # this will execute the greet function in script1 and print the value of name as script1

"""
                         HOW __name__ WORKS4071163 
================================================================================

Python sets __name__ to different values based on execution context:

CASE 1: File is RUN DIRECTLY (as a script)
    → __name__ is set to the string "__main__"
    
CASE 2: File is IMPORTED as a module
    → __name__ is set to the module's name (filename without .py)



This mechanism allows Python files to have DUAL FUNCTIONALITY:
1. Work as a reusable module (when imported)
2. Work as a standalone script (when run directly)

"""