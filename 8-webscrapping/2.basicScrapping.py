# you can create functin for finding the particular ele
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

from bs4 import BeautifulSoup

def find_title():
    simple_soup = BeautifulSoup(SIMPLE_HTML, "html.parser")
    return simple_soup.find('h1').string

print(find_title())

print()
###########################################################


def find_list():
    simple_soup = BeautifulSoup(SIMPLE_HTML, "html.parser")
    return [e.string for e in simple_soup.find_all('li')]

print(find_list())

print()
###########################################################


