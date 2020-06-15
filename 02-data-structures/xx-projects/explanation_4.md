# Problem 4: Explanation

The requirement to create an efficient algorithm that searches into this encapsulated structure, like a [_Matryoshka dolls_](https://en.wikipedia.org/wiki/Matryoshka_doll), as been satisfied by a __recursive algorithm__.

## Time/Space complexity

The time complexity of this algorithm is dependant on the number of iterations that are launched. 
Being in this case dependent on __encapsulation of groups__ and __number of users__ of folders, resulting in a __O(g*u)__. 
As for the _space complexity_, it is directly dependent on the number of returns the function does, hence, in this case __O(1)__.
