def unique(array1):
    uniqueList = []
    # runs a loop on the given array, and checkes each item inside that array
    for item in array1:
        #checks if each item is not already in the new list "uniqueList"
        if item not in uniqueList:
            #if the item is not found in the "uniqueList" then it adds that item to the list
            uniqueList.append(item)
    #returns the now populated "uniquelist"
    return uniqueList

print(unique([1]))