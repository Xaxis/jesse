### Code Challenge: without

One of the fundamental cornerstones of any programming language is having
a firm grasp on arrays and how to manipulate them. This first challenge
will get you started by developing a common utility function that is often
included in many array manipulation libraries.

#### The Challenge

Write a function named `without`. `without` returns a copy of the array with all instances of the values removed.
The functions arguments should look like:

````
def without(array, *values)
    # Your code goes here
````

The function would be used like the following example demonstrates:

````
nums = [1, 2, 1, 0, 3, 1, 4]
without(nums, (0,1)) # [2, 3, 4]
````

Note that no libraries of any kind should be used for this challenge.