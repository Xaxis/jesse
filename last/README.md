### Code Challenge: first

One of the fundamental cornerstones of any programming language is having
a firm grasp on arrays and how to manipulate them. This challenge
will get you started by developing a common utility function that is often
included in many array manipulation libraries.

#### The Challenge

Write a function named `last`. `last` should return the last element
of an array that is passed to it. Passing `n` will return the last
`n` elements of the array. The functions arguments should look like:

````
def last(array, [n])
    # Your code goes here
````

The function would be used like the following example demonstrates:

````
cars = ["Ford", "Volvo", "BMW", "Mercedes", "Toyota", "Chevrolet"]
last(cars) # Returns "Chevrolet"
last(cars, 2) # Returns ["Toyota", "Chevrolet"] as an array.
````

Note that no libraries of any kind should be used for this challenge.