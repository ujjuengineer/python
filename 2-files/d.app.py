# json files
# json files are more like python dictionaries, the only difference is json file consist string
# when we read the json file, its all string, we ccan convert that into python dictionaries


# NOTE : json.load(), json.dump() 


import json # used to work with json files

file = open('json_data.txt', 'r')
file_content = json.load(file) # read file and turns it to dictionary 
file.close()



print(file_content['friends'][0]) # file_content is a dictionary, and friends is a key in that dictionary, which contains a list of friends, and we are accessing the first friend in that list using [0]


# we can also convert a dictionary to a json string using json.dump() method

# list of python dictionaries
cars = [
    {'make': 'ford', 'model': 'fiests'},
    {'make': 'Ford', 'model': 'Focus'}
]

# lets convert it into json and write it into newfile called 'json_car.txt'
file = open('json_car.txt', 'w')
json.dump(cars, file)
file.close()



# explore : json.loads(), json.dumps() -> they use to convert string into py dict and py dict into json formatted string respectively (may be), explore it !
