# wap to check if list contains palindrome of element or not

"""
we will make a copy of the list and then reverse it, now if original list and copied list are same then 
it's a palindrome otherwise not
"""

list = [1,2,3,2,1]

copyList = list.copy() # creating copy of list
copyList.reverse() # reversing the list

print(list == copyList) # we can compare 2 list directly, can't do in cpp