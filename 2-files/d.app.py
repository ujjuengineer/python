import json # used to work with json files

file = open('json_data.txt', 'r')
file_content = json.load(file) # read file and turns it to dictionary 
file.close()



print(file_content['friends'][0]) # file_content is a dictionary, and friends is a key in that dictionary, which contains a list of friends, and we are accessing the first friend in that list using [0]


# we can also convert a dictionary to a json string using json.dumps() method
# note that 