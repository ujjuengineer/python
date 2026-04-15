# ask the user for a list of 3 friends 
# for each friends, we'll tell the user whether they are nearby
# for each nearby friend, we'll save their name to 'nearby_friends.txt'

friends = input("enter 3 freinds, separeated by commas (no space please) : ").split(',')

# .split(',') -> this will split the string into a list of strings, using comma as the separator


people = open('people.txt', 'r')
people_nearby = people.readlines() # gives you the list of lines 
people.close()

# note : the lines will have a newline character at the end

# for an example if the line ends with 'ujjwal', it will have a new line character at the end, which is hidden, it will be 'ujjwal\n' so we need to remove that newline character

# we can use the .strip() method to remove the newline character from the end of the string
# the strip() method will remove any leading and trailing whitespace characters, including the newline character

people_nearby = [person.strip() for person in people_nearby] # this is a list compherension, it will iterate over each person in the people_nearby list, and apply the strip() method to remove the newline character, and then return a new list with the stripped names

friends_set = set(friends) 
people_nearby_set = set(people_nearby)



friends_nearby_set = friends_set.intersection(people_nearby_set) 

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f"{friend} is nearby! meet up with them")
    nearby_friends_file.write(f"{friend}\n") # writing the nearby friends to the file, each friend on a new line

nearby_friends_file.close() # closing the file after writing

