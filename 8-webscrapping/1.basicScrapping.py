from bs4 import BeautifulSoup

SIMPLE_HTML = """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>this is h1 content</h1>
    <p class="subtitle">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolore, officia!</p>
    <p>this is an another paragraph !</p>
    <ul>
        <li>Ujjwal</li>
        <li>Bhindi</li>
        <li>Musehra</li>
        <li>Bhadru</li>
    </ul>
</body>
</html>"""
print()


# create the class of simple soup
# takes 2 argument, html doc and doc type which tells it is html doc
simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

h1 = simple_soup.find('h1') # find method use to give you the tag
content = simple_soup.find('h1').string # .string will gives you the content of the particular tag

print(h1)
print(content)


print()
#################################################################



# you can use .find_all to find all the matching elee
# find_all gives you list of the all matching ele

li = simple_soup.find_all('li')
print(li)
print([e.string for e in li ])


print()
#################################################################


# find method take dictionary as an argument, you can search for specific tag using class or id

p = simple_soup.find('p', {'class' : 'subtitle'})
print(p.string)


print()
#################################################################


# excluding a specific paragraph from all

all_para = simple_soup.find_all('p')
exclude = [e.string for e in all_para if 'subtitle' not in e.attrs.get('class', [])]
print(exclude)

"""
[e.string for e in all_para if 'subtitle' not in e.attrs.get('class', [])]

This is basically list comprehension [.......]
e.attrs : gives a dictionary of all the classes and ids of the current ele 'e'
.get method is accessing the 'class' and checking if value of 'class' is not 'subtitle'

by default .get method returns none if no attribute 'class' found
but if you check 'not in' none, then it will cause error, so we are returning an empyt list if no attribute 'class' is found !

"""

print()

