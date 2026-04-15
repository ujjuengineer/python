
# opening the file for reading
my_file = open('data.txt', 'r') # r -> for reading

# this will read entire file content 
file_content = my_file.read() 

my_file.close() # always remember to clsoe the file after the use

print(file_content)



# NOTE : always try to open and then close the file as quick as possible 


user_name = input("enter the name : ")

my_file_writing = open('data.txt', 'w') # this will open the file for writing
# the prev content will be deleted and whatever we write it will be overwritten to this file

my_file_writing.write(user_name) # overwritting the file content
my_file_writing.close() # closing the file