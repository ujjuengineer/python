# we can use with syntax so that we don't always explicitly open and close the file

# file = open('people.txt', 'r')
# content = file.read()
# file.close()

with open('people.txt', 'r') as file:
    content = file.read() 

# that is it, we don;t need to worry about closing the file and all !