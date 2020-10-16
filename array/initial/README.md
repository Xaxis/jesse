### Code Challenge: initial

One of the fundamental cornerstones of any programming language is having
a firm grasp on arrays and how to manipulate them. This first challenge
will get you started by developing a common utility function that is often
included in many array manipulation libraries.

#### The Challenge

Write a function named `initial`. `initial` should return everything but the last 
entry of the array that is passed to it. Passing `n` will exclude the last
`n` elements of the array. The functions arguments should look like:

````
def initial(array, [n])
    # Your code goes here
````

The function would be used like the following example demonstrates:

````
cars = ["Ford", "Volvo", "BMW", "Mercedes", "Toyota", "Chevrolet"]
initial(cars) # ["Ford", "Volvo", "BMW", "Mercedes", "Toyota"]
initial(cars, 2) # ["Ford", "Volvo", "BMW", "Mercedes"].
````

Note that no libraries of any kind should be used for this challenge.