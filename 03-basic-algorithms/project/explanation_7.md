# Problem 7: Request Routing in a Web Server with a Trie

Time complexity: __O(n)__ since we have to traverse the children to find the path.
Space complexity: __O(n)__ as we have to split and store the individual parts of the strings and a new `TrieNode` is created for each part of the path in adding a handler method. The space complexity in the lookup is __O(1)__
