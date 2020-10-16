### Code Challenge: difference

One of the fundamental cornerstones of any programming language is having
a firm grasp on arrays and how to manipulate them. This first challenge
will get you started by developing a common utility function that is often
included in many array manipulation libraries.

#### The Challenge

Write a function named `difference`. `difference` takes the difference between one array and a number of other arrays.
Only the elements present in just the first array will remain.
The functions arguments should look like:

````
def difference(array, *others)
    # Your code goes here
````

The function would be used like the following example demonstrates:

````
difference([1, 2, 3, 4, 5], [5, 2, 10])
$ [1, 3, 4]
````

Note that no libraries of any kind should be used for this challenge.