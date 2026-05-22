# read files
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
# write into file
def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)
        
print(__name__)