# r+ : read and overwrite, no truncate, pointer at start
# w+ : read and overwrite, truncate i.e., clear all data 
# a+ : write and append, no truncate, pointer at end

f = open("chapter_7/temp.txt", "r+")
f.write("hello world")
f.close()

# with syntax : better way to handel file, we don't need to close the file by command, it will do for us by own

with open("chapter_7/temp.txt","w+") as f :
    f.write("good morning")