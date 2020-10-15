nums = [1, 2, 1, 0, 3, 1, 4]

def without(arr, n=0):

    if n is without.__defaults__[0]:
        return arr[n:]
    else:
        for i in range(len(arr)):
            arr.remove(n)
            return arr
print(without(nums))
print(without(nums, 1))