# Problem 4: Explanation

Using sets and not lists. Assuming the groups and users are unique and cannot be duplicated.
And decided on using recursion.

## Time/Space complexity

Time complexity:
`is_user_in_group()` searching over a set is __O(1)__ while worst case is O(n).

space complexity: 
The space complexity is at most __O(g * u)__ the number of unique users/groups if a user is allowed to be part of multiple groups.
