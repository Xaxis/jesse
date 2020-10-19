# def union(arr, *manyarrs):
#     print(arr)
#     print(manyarrs)
#     return
#
# union([1, 2, 3], [101, 2, 1, 10], [2, 1],['1','2'])

#test

# def union(*manyarrs):
#     # print(len(manyarrs))
#     # print(type(manyarrs))
#     one = set(manyarrs[0])
#     two = set(manyarrs[1])
#     three = set(manyarrs[2])
#     unique_items = list((one ^ two) ^ (three))
#     return unique_items
#
# print(union([1, 2, 3], [101, 2, 1, 10], [2, 1]))

# for loop to iterate over the tuple

def union(*foo):
    for i in enumerate(foo):
        print(i)pu
    return

print(union([1, 2, 3], [101, 2, 1, 10], [2, 1]))
