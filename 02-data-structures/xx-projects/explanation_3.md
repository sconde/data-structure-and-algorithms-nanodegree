# Problem 3: Explanation

*Huffman codes* is one of the simpler compression algorithms that uses a greedy strategy and can be applued to any data that is represented using bits.
The bais idea of Huffmann codes is to use few bits for letters that occur more frequently in the text you are compressing and more bits for letters that occur less often.

We can use a dictionary with the characters as keys mapping to their frequency. I use the `Counter` from `collections`.
Next we want to create a tree node for each frequency tand store them in order.
A binary heap or priority queue is the exact data structure we need to efficiently implement the algorithm.
The amount of work is constant since a fixed number of items are being inserted and removed from the heap.
In the worst case, the sorting takes __O(n log n) for the inserting/removing the __n__ items from the heap where __n__ is the unique number of different charaters in the file.

We can use the tree to determine the bit code for each character on its location in the tree.
The running time for this is linear in terms of the number of nodes in the tree.

Again, each iteration of the `while` loop in Huffman's algorithm can be implemented in __O(log d)__ time using a priority queue represented with a heap.
Each iteration takes two nodes out of `Q` and adds one in, a processes that will be repeated `d-1` times before exactly one node left in `Q`.
Thus the runtime is __O(n + d log d)__ time, __n__ is the string length with __d__ distinct characters.

