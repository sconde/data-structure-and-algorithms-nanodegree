# # Rotated array search

I opted for an iterative solution based on binary search and not a recursive solution mainly for the benefit of a constant memory.

Time complexity: __O(log n)__

Space complexity: "space complexity of recursive algorithm is proportinal to maximum depth of recursion tree generated. If each function call of recursive algorithm takes O(m) space and if the maximum depth of recursion tree is 'n' then space complexity of recursive algorithm would be O(nm).
In the case of this problem, each call uses O(1) space, the maximum depth of the recursive tree is O(logn) so the space complexity is O(logn)"
