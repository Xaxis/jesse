def difference(arr1=[], arr2=[]):
    findUnique = list(set(arr1) - set(arr2))
    return findUnique


print(difference([1, 2, 3, 4, 5], [5, 2, 10]))
