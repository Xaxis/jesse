### Code Challenge: first

One of the fundamental cornerstones of any programming language is having
a firm grasp on arrays and how to manipulate them. This first challenge
will get you started by developing a common utility function that is often
included in many array manipulation libraries.

#### The Challenge

Write a function named `first`. `first` should return the first element
of an array (or list) that is passed to it. Passing `n` will return the first
`n` elements of the array. The functions arguments should look like:

````
def first(array, [n])
    # Your code goes here
````

The function would be used like the following example demonstrates:

````
cars = ["Ford", "Volvo", "BMW", "Mercedes", "Toyota", "Chevrolet"]
first(cars) # Returns "Ford"
first(cars, 2) # Returns ["Ford", "Volvo"] as an array.
````

Note that no libraries of any kind should be used for this challenge.