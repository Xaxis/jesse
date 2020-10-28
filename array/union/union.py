
def union(arg1, *arg2):
    '''
    Checks to see if a value is already in the first [array]
    given. If the value is not in the [array] it appends that
    that value at the end of the first [array].
    '''
    unionList = arg1
    for i in arg2:
        # 'i' should be each array given in arg2
        for number in i:
            # 'number' should be each value inside of each array given in arg2
            if number not in unionList:
            # if the number is not already in the unionList then is should add that number at the end of the list
                unionList.append(number)
    return unionList


print(union([1, 2, 3], [101, 2, 1, 10], [2, 1]))