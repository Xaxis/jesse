def difference(arr1=[], arr2=[]):
    findUnique = list(set(arr1) - set(arr2))
    return findUnique

print(difference([1,2,3,4,5], [2,5,10]))


# def without(arr1, arr2=[]):
#     subtract = list(set(arr1) - set(arr2))
#     return subtract