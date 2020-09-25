# Dutch National Flag Problem

This is a 3-way partitioning problem. I first traverse the list to count the number of 0, 1, and 2. Then loop a second time around filling the output array with 0's first, then 1's, and finally 2's with their respective counts.

Time complexity: __O(n)__ since I'm only looping through the array twice.
Space complexity: __O(n)__ as I have used another list to store the result. If I can change the input list and return it as a result, I would not need to construct the `output_list` and I can do the sorting in place which would result in a __O(1)__ space complexity.
