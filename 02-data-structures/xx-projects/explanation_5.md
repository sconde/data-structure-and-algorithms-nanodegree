# Problem 5: Explanation

This project is based on the creation of a linked list, though, in this case the list is __traversed backwards__ and has the attribute of __inmutability__. 
This has provoked, that some of the methods developed during the course for _linked list_ are not available for the _Blockchain list_:

- prepend
- remove
- pop
- insert

## Time/Space complexity

As for the time complexity, being a __linked list__ in its core structure, it has:

- append: __O(1)__
- search: __O(n)__
- size: __O(n)__
- to_list: __O(n)__

In respect to _space complexity_, it is directly dependant on the number of __nodes__ our BlockChain incorporates, resulting in __O(n)__.
