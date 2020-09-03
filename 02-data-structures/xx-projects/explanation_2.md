# Problem 2: Explanation

I opted for a recursion process since we have to look through all folders and subfolders - walking the directory.
The `find_files` will recursively visit each folders/sub-folders, to find the matching pattern (with `.endswith` string method).
All files matching the patterns are stored in a list that is extended with each recursive calls.

## Time and Space complexity

The time/space complexity is __O(n)__ for the number of files present in the directory.


## References

- [Python's string method complexity](https://stackoverflow.com/a/35220792/2943424)
