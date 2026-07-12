# scrapping information from the example.com
import requests
from bs4 import BeautifulSoup

import requests

# Send the request and capture the Response object
page = requests.get('http://www.example.com')


"""
page.status_code : Check if it was successful

page.text : Returns the page's source code as a Python string (automatically decoded into readable text like HTML, JSON, or XML). This is what you pass into Beautiful Soup.

page.content : Returns the raw, un-decoded bytes of the page. You use this when downloading non-text files like images, PDFs, or audio files.
"""
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

h1_content = soup.find('h1').string
print(h1_content)

p_content = soup.find('p').string
print(p_content)

p_link = soup.find('p a').attrs['href']
print(p_link)
