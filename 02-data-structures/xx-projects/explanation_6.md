# Problem 6: Explanation

For the union and intersection, I used the builtin `set` in python, leveraging that `set` only stores unique elements.

Time complexity:
    - `append` and `size` are __O(n)__ and __O(m)__, where __n__ and __m__ are length of the two lists, respectively.
    
Space complexity:
    - Storing the content of both list, should they be unique, leads to __O(n + m)__
    - If the one list is a subset of the larger list, then with clever re-ordering, the storage could be reduced to __O(n)__, where __n > m__

