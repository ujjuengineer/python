# python can used to perform operation on file (read and write data)

"""
open, read and close file
# before reading or writing any file, we have to open it, we open any file usign follow
    f = open("file_name", "mode"), mode can be : 
                                        r : for read mode
                                        w : for write mode
    now we can the file in "f" variable, so we can access it using f 
"""

# we have created a txt file, let access this !!

f = open("/Users/ujjwalkumar/Desktop/git-hub-clone/python/chapter_7/temp.txt", "r") # if we didn't pass the mode, then python will take default value i.e., read mode "r";

data = f.read()
print(data)
f.close()


"""
few modes are ; 
r : open for reading (default)
w : open for writing, (pehle ka sara data delete ho jaaega, uske baad new data overwrite krega)
x : create a new file and open it for writing
a : open for writing, and appending the new data at the end of the prev data(if exist)
b : when we are opening binary files
t : when we are opening text files (by default hota hai)

# we can combine 2 modes like
f = open("temp.txt", "wt") meand write text file, if we ignore "t" it will take it as default value, but for opening binary file, we must implicitly mention "b"

+ : open for updating (reading and writing)                                         
"""

# we can pass argument in the read function, to read any particular set of text

f = open("/Users/ujjwalkumar/Desktop/git-hub-clone/python/chapter_7/temp.txt", "r") 
new_data = f.read(6) # read only 6 characters
print(new_data)
print()
f.close()



# we can even read the data line by line 
f = open("/Users/ujjwalkumar/Desktop/git-hub-clone/python/chapter_7/temp.txt", "r") 
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()
