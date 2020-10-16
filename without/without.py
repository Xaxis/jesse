nums = [1, 2, 1, 0, 3, 1, 4]
# fixed the function to work with muliple values and renamed the `diff` variable
def without(arr1, arr2=[]):
    subtract = list(set(arr1) - set(arr2))
    return subtract

# prints the subtract value
print(without(nums, [1,2,3]))