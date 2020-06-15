"""
Proble 6: Union and Intersection
"""

class Node(object):
    
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList(object):
    
    def __init__(self):
        self.head = None

    def append(self, val):
        
        if self.head is None:
            self.head = Node(val)
            return
        
        head = self.head
        while head.next:
            head = head.next

        head.next = Node(val)

    def size(self):
        
        size = 0
        head = self.head

        while head:
            size +=1
            head = head.next

        return size

    def to_list(self):
        
        this_list = []
        head = self.head

        while head:
            this_list.append(head.value)
            head = head.next

        return this_list


def union(first_list, second_list):

    big_list = list(
        set(
            first_list.to_list() + second_list.to_list()
        )
    )

    linked_list = LinkedList()
    for it in big_list:
        linked_list.append(it)

    return linked_list

def intersection(first_list, second_list):

    set_1 = set( first_list.to_list() )
    set_2 = set( second_list.to_list())

    common = [ el for el in set_1 if el in set_2 ]

    linked_list = LinkedList()
    for el in common:
        linked_list.append(el)

    return linked_list

if __name__ == "__main__":
    
    #%% Test Official
    # Normal Cases:
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
    print(intersection(linked_list_1, linked_list_2))
    # 4 -> 6 -> 21 ->

    # Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
    print(intersection(linked_list_3, linked_list_4))
    #

    # Test case 3
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [22, 7, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 65, 11, 21, 1]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print(union(linked_list_5, linked_list_6))
    # 65 -> 1 -> 35 -> 4 -> 3 -> 6 -> 7 -> 8 -> 11 -> 21 -> 22 -> 23 ->
    print(intersection(linked_list_5, linked_list_6))
    # 65 -> 7 ->


    # Edge Cases:
    # Test case 4
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = []
    element_2 = [1, 7, 8]

    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)

    print(union(linked_list_7, linked_list_8))
    # 8 -> 1 -> 7 ->
    print(intersection(linked_list_7, linked_list_8))
    #

    # Test case 5
    linked_list_9 = LinkedList()
    linked_list_10 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_9.append(i)

    for i in element_2:
        linked_list_10.append(i)

    print(union(linked_list_9, linked_list_10))
    #
    print(intersection(linked_list_9, linked_list_10))
    #