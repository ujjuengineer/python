from utils_dir import file1
print(__name__)

"""
__name__ == __main__ if we run any file directly

but if we import any modules and run that modules from this file, then the modules __name__ is no longer __main__ 

in the case of modules __name__ = absolute path from the root directory

so in case of file1.__name__ -> utils_dir.file1
and in case of file.__name__ -> utils_dir.common.file 

"""

"""
one line summary is that, 
if you are importing any modules 'a' inside modules 'b' then use relative path
and for importing modules inside the script(files that are run through the root dir), use absolute path

"""



"""
what is import error ? 
when a module 'a' is importing module 'b' and module 'b' is importing module 'a' then it will cause import error !
"""