"""
Proble 6: Union and Intersection
"""


class Node:

    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next

        return out_string

    def append(self, val):

        if self.head is None:
            self.head = Node(val)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(val)

    def size(self):

        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

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
    set_1 = set(first_list.to_list())
    set_2 = set(second_list.to_list())

    common = [el for el in set_1 if el in set_2]

    linked_list = LinkedList()
    for el in common:
        linked_list.append(el)

    return linked_list


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
print(intersection(linked_list_1, linked_list_2))

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
print(intersection(linked_list_3, linked_list_4))
