nums = [1, 2, 1, 0, 3, 1, 4]
# the function 'without' wont allow for multiple arugments
def without(arr, n=0):

    if n is without.__defaults__[0]:
        return arr[n:]
    else:
        while n in arr:
            arr.remove(n)
        return arr
print(without(nums))
print(without(nums, 1))