# this is a seprate module named car.py to store the Car class

class Car:
    def __init__(self, model, color, year, for_sale):
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale

    # methods are the functions defined inside a class
    def display_info(self):
        print(f"Model: {self.model}, Color: {self.color}, Year: {self.year}, For Sale: {self.for_sale}")
    
    