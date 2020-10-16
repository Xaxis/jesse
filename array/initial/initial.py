# imported the array
cars = ["Ford", "Volvo", "BMW", "Mercedes", "Toyota", "Chevrolet"]


def initial(arr, n=0):
    if n is initial.__defaults__[0]:
        return arr[0:-1]
    else:
        return arr[0:-n]


print(initial(cars))ls
print(initial(cars, 2))
