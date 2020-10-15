### Code Challenge: rest

One of the fundamental cornerstones of any programming language is having
a firm grasp on arrays and how to manipulate them. This first challenge
will get you started by developing a common utility function that is often
included in many array manipulation libraries.

#### The Challenge

Write a function named `rest`. `rest` should return the rest of the elements
in an array. Passing an `index` to return the values of the array from that index
onward:

````
def rest(array, [index])
    # Your code goes here
````

The function would be used like the following example demonstrates:

````
nums = [5, 4, 3, 2, 1]
rest(nums) # [4, 3, 2, 1]
rest(nums, 2) # [3, 2, 1].
````

Note that no libraries of any kind should be used for this challenge.