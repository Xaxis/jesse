# defining the variable "cars" as an array
cars = ["Ford", "Volvo", "BMW", "Mercedes", "Toyota", "Chevrolet"]
#comment
def first(arr, n=0):
    if n is first.__defaults__[0]:
        return arr[n]
    else:
        return arr[0:n]


print(first(cars))
print(first(cars,2))

if first(cars) == "Ford":
    print("Yep")