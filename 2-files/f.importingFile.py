# you can import modules and use the code written over there in current script

# modules are frequently saved in 'utils' directory which consist a file called __init__.py

# __init__.py tells python that current directory is an utils directory which consist modules

# lets create a utils directory under which we will create file_operation module

import utils.file_operations as fl

print(fl.read_file('data.txt'))

