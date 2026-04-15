print() 

file = open('csv_data.txt', 'r') 
lines = file.readlines() # list of lines in the file 
file.close()

# we don't want the first line because it contains the column names

lines = lines[1:] # slicing the list to get all the lines except the first one 

# now each line is something like : 'ujjwal,22,mit,computer science\n'

# we can use the split() method to split the line across the commas 

lines = [line.strip().split(',') for line in lines] # this is a list comprehension, it will iterate over each line in the lines list, and apply the strip() method to remove the newline character, and then apply the split(',') method to split the line into a list of strings, using comma as the separator, and then return a new list with the splitted lines

# so basically it is returning us a list of lists, where each inner list contains the values of the columns for that line 



for line in lines:
    name = line[0].title()
    age = line[1]
    college = line[2].capitalize() 
    degree = line[3].title()

    print(f"{name} is {age} studying {degree.capitalize()} at {college}")

# differene between .title() and .capitalize() is that .title() will capitalize the first letter of each word, while .capitalize() will only capitalize the first letter of the first word and make the rest of the letters lowercase.


print()
print('sample output : ')
sample_output = ",".join(lines[0]) # this will join the first line of the lines list into a single string, using comma as the separator
print(sample_output)

print()