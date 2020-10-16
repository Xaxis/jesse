def difference(arr1=[], arr2=[]):
    findUnique = list(set(arr1) - set(arr2))
    return findUnique

print(difference([1,[1,2,3],3,4,5,6,6], [[1,2,3unb],5,4,6]))