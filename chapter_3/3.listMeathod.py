list = [4,5,3,7,2,1,6]
print("list before appending :",list)
print()

list.append(8) # add 8 in the list
print("list after appending :",list)
print()


# to sort any list , note that they do changes in original string

list.sort() # sort in accending order
print("list after sorting in accending order :",list)

list.sort(reverse = True) # sort the list in decending order
print("list after soring in decending order :", list)
print()


# sorting in string list are done according to ascii value
stringList = ["Ujjw", "rass", "ujjw", "Ras"]
print(stringList.sort()) # this will return none, because list.sort() don't have any return value
print(stringList)
print()


# reverse the list, changes are done in original list
print("list before reversing :",list)
list.reverse()
print("list after reversing :",list)


# inserting any value in the middle of the list
newList = [0,1,2,4,5,6]
newList.insert(3,99) # 3rd index pe 99 insert kr dega
print(newList)