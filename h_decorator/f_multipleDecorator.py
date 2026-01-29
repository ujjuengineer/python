def deco1(func):
    def wrapper1():
        print("before deco1")
        func()
        print("after deco1")
    return wrapper1

def deco2(func):
    def wrapper2():
        print("before deco2")
        func()
        print("after deco2")
    return wrapper2


@deco1
@deco2
def say_hi():
    print("hi")

say_hi()

# simple analogy : uper se niche padhna start kro and iss trike se likh do 
# wrapper1(wrapper2(say_hi))

"""
line 16, 17, 18 => say_hi = deco1( deco2(say_hi) )
                -> say_hi = deco1(wrapper2) , wrapper2 "func" = original say_hi()
                -> say_hi = wrapper1    ,,,,    wrapper1 "func" = wrapper2

so at line 21 when you execute say_hi() -> you are executing wrapper1()

output : 
    "before deco1"
    -> here func == wrapper2 , wrapper 2 executed
        "before deco2"
        -> here func == original function, original function executed
            "hi"
        "after deco2"
    "after deco1"


    
"""
