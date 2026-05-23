# you can make your generators iterable, i.e., you can do something like this 
# for items in generator : 
    # pass


# you can do this using __iter__ method

class FirstTenGenerator:
    def __init__(self):
        self.i = 0

    def __next__(self): # it helps you to call next(object) which behaves similarly
        if self.i < 10:
            curr_num = self.i
            self.i += 1
            return curr_num
        else :
            raise StopIteration() # stop the iteration 
    
    def __iter__(self): # this will make your generator iteratable
        return self 
    

g = FirstTenGenerator()

for num in g:
    print(num)

# see the image of this file for understanding the flow








# just like list compherension you an also use generator compherension

my_numbers = [x for x in range(10)] # list of 0 o 9
my_numbers_gen = (x for x in range(10)) # this is generator 
# you can call next(my_numbers_gen)
print("next on compherension generator is : ", next(my_numbers_gen))








# besides __iter__, you can also use __getitem__(self, idx) to make the object iteratable, but it used index to iterate through 

class AnotherIterable:
    def __init__(self):
        self.cars = ['bmw', 'mercedies', 'fortuner', 'ferrari']

    def __getitem__(self, key):
        return self.cars[key]

for car in AnotherIterable():
    print(car)