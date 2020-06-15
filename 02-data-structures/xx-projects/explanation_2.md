# Problem 2: Explanation

The recursion process, is based on the visit of each folder, on each folder we keep the files that match the desired pattern and we keep on going deeper on the folder structure by launching subsequent calls to the function. 
The  decision not to use the provided assistance to detect if it was a __file__ or a __folder__, has been decided after not being able to properly use it (and also seeing the facility of coding my own solutions).

## Time and Space complexity

In therms of __time complexity__, trying to be guided by the [Master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)), tough not being able to  quantify the size of _n/b_ (as it's a folders depth and it needs not to be splitted proportionally). 
Thus, using another approach, the time complexity is dependant on the number of iterations that are launched. 
Being in this case dependent on __depth__ and __width__ of folders, resulting in a __O(d*w)__. 
As for the space complexity, in this case,  it is directly dependent on the number of returns the function does, hence, the number of found files __f__, __O(f)__.
