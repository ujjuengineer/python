# write a recursive function to print all the elements in the list

def printElement(list, idx) : 
    # base case
    if(idx == len(list)) : 
        return
    # kaam
    print(list[idx], end = ", ")
    # call
    printElement(list, idx+1)


# creating list
list = ["ujjwal", "ram", "mum", "ras"]

# calling the above function to print this list
printElement(list,0)