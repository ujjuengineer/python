# type hinting : use for specify the data type, it is not stricly implemented, it's just for developer reference

from typing import List # you need to import complex data type like list, tuple for using it as typehinting !

def fun (a:int, b:int) -> int :
    return a + b


ans = fun(4,5)
print(ans)



def listOfNum() -> List:
    li = []
    for i in range(10):
        li.append(i)
    return li

li = listOfNum()
print(li)