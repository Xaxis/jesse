cars = ["Ford", "Volvo", "BMW", "Mercedes", "Toyota", "Chevrolet"]
#
def last(arr, n=0):
    if n is last.__defaults__[0]:
        return arr[-1]
    else:
        return arr[-n:]

print(last(cars))
print(last(cars, 2))

