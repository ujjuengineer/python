class Atm : 
    def __init__(self, pin, balance): 
        self.__pin = pin
        self.__balance = balance

# when you create an object like this
xyz = Atm(3453,542452)

# here xyz is not an object, Atm() is an object and xyz is the reference variable which is storing the address of your object

# you can create object just like this
Atm()
# but since you have not stored its address in a referece variable, so you can't use it now

# therefore we use reference variable to store the objects referece for furthure use