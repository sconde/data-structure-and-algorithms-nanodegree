# Problem 5: Explanation

Used two classes: `Block` and `BlockChain`. Here the `BlockChain` class is really just a LinkedList.

## Time/Space complexity

The code is build on a LinkedList:

    - append: __O(1)__
    - search: __O(n)__
    - size: __O(n)__
    - to_list: __O(n)__

Space complexity is __O(n)__ for storing each of the __n__ blocks in the LinkedList.
