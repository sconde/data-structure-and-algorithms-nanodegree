"""
File: problem7_route_trie.py
Author: Sidafa Conde
Email: sconde@umassd.edu
Github: sconde
Description: 
"""


class RouteTrieNode:
    """
    A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
    """

    def __init__(self, handler=None):
        """
        Initialize the node with children as before, plus a handler

        @param handler:
        """
        self.children = dict()
        self.handler = handler

    def insert(self, path, handler=None):
        """
        Insert the node as before

        @param path:
        @param handler:
        @return:
        """
        if path not in self.children:
            self.children[path] = RouteTrieNode(handler)


class RouteTrie:
    """
    A RouteTrie will store our routes and their associated handlers
    """

    def __init__(self, handler):
        """
        Initialize the trie with an root node and a handler, this is the root path or home page node

        @param handler:
        """
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, path, handler):
        """
        Similar to our previous example you will want to recursively add nodes
        Make sure you assign the handler to only the leaf (deepest) node of this path

        @param path:
        @param handler:
        @return:
        """

        node = self.root
        for pth in path:
            node.insert(pth)
            node = node.children[pth]

        node.handler = handler

    def find(self, path):
        """
        Starting at the root, navigate the Trie to find a match for this path
        Return the handler for a match, or None for no match

        @param path:
        @return:
        """

        node = self.root

        for pth in path:
            if pth not in node.children:
                return None
            node = node.children[pth]
        return node.handler


def split_path(path):
    """
    # you need to split the path into parts for
    # both the add_handler and loopup functions,
    # so it should be placed in a function here

    @param path:
    @return:
    """

    results = [
        el for el in path.strip('/') if el != ''
    ]
    return results


class Router:
    """
    The Router class will wrap the Trie and handle

    """

    def __init__(self, handler=None, not_found=None):
        """
        Create a new RouteTrie for holding our routes
        You could also add a handler for 404 page not found responses as well!

        @param handler:
        @param not_found:
        """

        self.router = RouteTrie(handler=handler)
        self.handler = handler
        self.not_found = not_found

    def add_handler(self, path, handler):
        """
        Add a handler for a path
        You will need to split the path and pass the pass parts
        as a list to the RouteTrie

        @param path:
        @param handler:
        @return:
        """
        self.router.insert(
            path=split_path(path),
            handler=handler
        )

    def lookup(self, path):
        """
        lookup path (by parts) and return the associated handler
        you can return None if it's not found or
        return the "not found" handler if you added one
        bonus points if a path works with and without a trailing slash
        e.g. /about and /about/ both return the /about handler

        @param path:
        @return:
        """

        split_pth = split_path(path)

        if len(split_pth) == 0:
            return self.router.handler

        handler = self.router.find(
            path=split_pth
        )

        if handler is None:
            return self.not_found

        return handler


## Test Cases
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler",
                "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup(
    "/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
