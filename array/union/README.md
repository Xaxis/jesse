### Code Challenge: union

One of the fundamental cornerstones of any programming language is having
a firm grasp on arrays and how to manipulate them. This challenge
will get you started by developing a common utility function that is often
included in many array manipulation libraries.

#### The Challenge

Write a function named `union`.`union` should Compute the union of the passed-in arrays:
the list of unique items, in order, that are present in one or more of the arrays.
The functions arguments should look like:

````
def union(arr, *manyarrs):
    # Your code goes here
````

The function would be used like the following example demonstrates:

````
union([1, 2, 3], [101, 2, 1, 10], [2, 1])
$ [1, 2, 3, 101, 10]
````

Note that no libraries of any kind should be used for this challenge.