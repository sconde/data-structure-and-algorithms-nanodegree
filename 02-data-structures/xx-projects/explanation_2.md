# Problem 2: Explanation

I opted for a recursion process since we have to look through all folders and subfolders - walking the directory.
The `find_files` will recursively visit each folders/sub-folders, to find the matching pattern (with `.endswith` string method).
All files matching the patterns are stored in a list that is extended with each recursive calls.

## Time and Space complexity

The time complexity is __O(m)__ for each of the `os.listdir()` where __m__ is the number of directory, __O(n)__ to filter out files with matching patterns and add them to the result list - __O(mn)__
Extending to the list is __O(k)__ - __k__ is the number of elements.

There are additional stack space associated with a recursive algorithm for the funtion arguments, rewinding the stack, control flow, etc.
The space complexity is dependent on the number of recursive calls, __O(mn)__ - __m__ is the number of recursive calls and __n__ is space used for each calls.

## References

- [Python's string method complexity](https://stackoverflow.com/a/35220792/2943424)
