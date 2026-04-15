# instance variable : jo v variable ko aap constructor ke andar define krte ho 
# -> inka value har object ke liye alag hota hai


# you know you can access your instance variable from outside the class
# but this is not a good practice
# so you can put __ infront of your variable name to make it private, now it wont be visible form outside the class

class Atm : 
    def __init__(self, pin, balance): 
        self.__pin = pin
        self.__balance = balance

    # use getter setter to set and get your private member :NOTE: this is called encapsulation



hdfc = Atm(6969,436346)

# print(hdfc.__balance) # error

# you can even hide your method by adding __ infront of your function name

"""

HOW THIS IS WORKING INTERNALLY ? 

jese hi tum __pin define kiye
python internally convert your variable as : _Atm__pin (_objName__variablename)


"""

# to confirm that you can print
print(hdfc._Atm__pin) # 6969
# so you can say NOTE : NOTHING IN PYTHON IS TRULY PRIVATE



# NOTE : 
# if you try to do something like hdfc.__pin = 345 , then will it work ?
hdfc.__pin = 345    # surprise , this works , but why ? 


# EXPLANATION : 
# since there is no actually __pin variable in your class, (it's actually _Atm__pin)
# so if you do hdfc.__pin = 345
# it created a new variable __pin in your object and this variavle is puclic that you can access this variabl from outside the class as 
print(hdfc.__pin) # 345
