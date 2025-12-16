# indexing : accessing elements of a sequence using [] (index operator)
# [start : end : step] 

# example string

my_string = "Hello, World!"

# 1. accessing individual characters using positive indexing
first_char = my_string[0]  # 'H'
fifth_char = my_string[4]  # 'o'
print(first_char)
print(fifth_char)   

# 2. accessing individual characters using negative indexing
last_char = my_string[-1]   # '!'
second_last_char = my_string[-2]  # 'd'
print(last_char)
print(second_last_char)

# 3. slicing strings using [start : end]
substring1 = my_string[0:5]    # 'Hello'
# you can omit start or end
substring2 = my_string[:5]      # 'Hello'
substring3 = my_string[7:]      # 'World!'
print(substring1)
print(substring2)
print(substring3)

# 4. slicing with step
every_second_char = my_string[::2]  # 'Hlo ol!'
reversed_string = my_string[::-1]    # '!dlroW ,olleH'
print(every_second_char)
print(reversed_string)


# reverse the character of a string
str = "ujjwal"
rev_str = str[::-1]
print(rev_str)  # Output: "lawjju"


# print the last 4 digit of a number
num = "3453-7637-1234-5678"
last_four_digits = num[-4:]
print(last_four_digits)  # Output: "5678"