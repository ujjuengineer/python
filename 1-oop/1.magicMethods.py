# magic methods are special methods which are automatically called when a certain crateria is satisfied

# for an example __init__ : this is a constructor, it is a magic method, when we create an object it automatically called by the object when an object is created

# similarly we have many magic methods

# 1. __str__(self) : this function is automatically called when you print any object

class Fraction:

    def __init__(self, n, d):
        self.nume = n
        self.denume = d

    def __str__ (self) :
        return("haa bhai tu __str__ function ko call kr diya")

    
fraction_num = Fraction(3,5)
print(fraction_num) # since you are printing the object, __str__ will automatically called



# 2. __add__ (self, other): automatiaclly truggred when you try to add 2 objects
# 3. __sub__ (self, other): 
# 4. __mul__ (self, other): 




