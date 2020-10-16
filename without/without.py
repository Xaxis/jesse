nums = [1, 2, 1, 0, 3, 1, 4]
# the function 'without' wont allow for multiple arugments
def without(arr1, arr2=[]):
    diff = list(set(arr1) - set(arr2))
    return diff

#print(without(nums))
print(without(nums, [1,2,3]))