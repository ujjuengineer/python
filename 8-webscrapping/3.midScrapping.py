from bs4 import BeautifulSoup

ITEM_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
        <article class="product_pod">
            <div class="image_container">
                <a href="catalogue/a-light-in-the-attic_1000/index.html">
                    <img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail">
                </a>
            </div>

            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>

            <h3>
                <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>
            </h3>

            <div class="product_price">
                <p class="price_color">£51.77</p>
                
                <p class="instock availability">
                    <i class="icon-ok"></i> In stock
                </p>

                <form>
                    <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">
                        Add to basket
                    </button>
                </form>
            </div>
        </article>
    </li>
</body>
</html>"""

# NOTE : IMPORTANT
"""
Difference between select_one and find
.find() uses specific Python arguments (tags and attributes), 
while .select_one() uses CSS Selectors (the same syntax used to style websites or target elements in JavaScript).

Objective	    Using .find()	                    Using .select_one()
By Tag Name	    soup.find('p')	                    soup.select_one('p')
By Class	    soup.find('p', class_='price')	    soup.select_one('p.price')
By ID	        soup.find('div', id='main')	        soup.select_one('div#main')
By Attribute	soup.find('img', alt='A Light')	    soup.select_one('img[alt="A Light"]')

"""
soup = BeautifulSoup(ITEM_HTML, 'html.parser')

class ParsedItem:
    """
    A class to take in an HTML page, and find properties of an item in it
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def find_item_name(self):
        selector = 'article h3 a' # css selector
        # select the tag
        ele = self.soup.select_one(selector) # it will selct the anchor tag
        # get the attribute value form the selected ele
        name = ele.attrs.get('title')
        print(name)

    def find_item_link(self):
        selector = 'article h3 a'
        link = self.soup.select_one(selector).attrs.get('href')
        print(link)

    def find_item_price(self):
        selector = 'article div.product_price p.price_color'
        price = float(self.soup.select_one(selector).string[1:])
        print(price)

    def find_item_rating(self):
        selector = 'article p.star-rating'
        all_classes = self.soup.select_one(selector).attrs.get('class') # list of all classes
        rating = [c for c in all_classes if c != 'star-rating'][0]
        print(rating)

obj = ParsedItem(ITEM_HTML)
obj.find_item_name()
obj.find_item_link()
obj.find_item_price()
obj.find_item_rating()