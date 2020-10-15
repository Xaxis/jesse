nums = [5, 4, 3, 2, 1]

def rest(arr, index=0):
    if index is rest.__defaults__[0]:
        return arr[1:]
    else:
        return arr[index:]

print(rest(nums))
print(rest(nums, 2))
