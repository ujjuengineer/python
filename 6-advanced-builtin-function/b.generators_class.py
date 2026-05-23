# you can create your own generator class 

class FirstTenGenerator:
    def __init__(self):
        self.i = 0

    def __next__(self): # it helps you to call next(object) which behaves as self.__next__()
        if self.i < 10:
            curr_num = self.i
            self.i += 1
            return curr_num
        else :
            raise StopIteration() # stop the iteration 
        

# create generator
g = FirstTenGenerator()

print(next(g)) # 0, next(g) -> g.__next__() calling this function 
print(next(g)) # 1

# note that these generators are not iteratable, 
# you can't do like 
# for in in g : 
#    pass

