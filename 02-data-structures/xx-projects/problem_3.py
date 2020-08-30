"""
Problem 3: Huffman Coding
"""

import sys
from collections import (Counter, )
import queue


# import pprint


class HuffmanNode:

    def __init__(self, left=None, right=None, frequency=None, element=None):
        self.left = left
        self.right = right
        self.frequency = frequency
        self.element = element

    # for priority queue
    def __str__(self):
        return str(f"HuffmanNode({self.element}: {self.frequency})")

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency


def make_tree(frequencies):
    # initialize a priority queue
    priority_queue = queue.PriorityQueue()

    if len(frequencies) == 1:
        root_node = HuffmanNode(frequency=0)
        priority_queue.put(root_node)

    for (el, fq) in frequencies:
        node = HuffmanNode(element=el, frequency=fq)
        priority_queue.put(node)

    while priority_queue.qsize() > 1:
        # first two highest priority
        right = priority_queue.get()
        left = priority_queue.get()

        root = HuffmanNode(left=left, right=right,
                           frequency=(left.frequency + right.frequency)
                           )
        priority_queue.put(root)

    return priority_queue.get()


def encode_recursive(root, bits):
    huffman_codes = {}

    # base case
    if root is None:
        return {}

    if root.element is not None:
        huffman_codes[root.element] = bits

    huffman_codes.update(
        encode_recursive(root.left, bits + '0')
    )
    huffman_codes.update(
        encode_recursive(root.right, bits + '1')
    )

    return huffman_codes


def encode(huffman_tree):
    if huffman_tree.left is None and huffman_tree.right is None:
        return {huffman_tree.element: '0'}

    return encode_recursive(huffman_tree, '')


def huffman_encoding(data):
    # non-empty string
    if len(data) < 1:
        return False
    # compute the frequency of each character
    freq = Counter(data).items()

    huffman_tree = make_tree(freq)

    # encoding
    encoded_map = encode(huffman_tree)

    encoded_message = ''.join(
        [
            encoded_map[letter] for letter in data
        ]
    )

    return encoded_message, huffman_tree


def huffman_decoding(encoded_string, root):

    node = root
    output = ''

    for char in encoded_string:

        if node.left is None and node.right is None:
            # a left - add to the output
            output += node.element
            node = root

        if char == '0':
            node = node.left
        else:
            node = node.right

    # get the final node element
    output += node.element
    return output


def test_encode_decode(a_great_sentence):

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

if __name__ == "__main__":
    codes = {}

    print('Case 0:')
    a_great_sentence = "a fast runner need never be afraid of the dark"
    test_encode_decode(a_great_sentence)

    print('Case 1:')
    a_great_sentence = "The bird is the word"
    test_encode_decode(a_great_sentence)

    # Case 2
    print('Case 2:')
    a_great_sentence = "I just want to have fun coding"
    test_encode_decode(a_great_sentence)

    # Case 3
    print('Case 3:')
    a_great_sentence = "The sun shines and I go to the beach"
    test_encode_decode(a_great_sentence)

    # Edge Cases
    # Case 4
    print('Edge Cases:')
    print('Case 4:')
    a_not_so_great_sentence = "aaa"
    test_encode_decode(a_great_sentence)

    # Case 5
    print('Case 5:')
    a_not_so_great_sentence = ""
    test_encode_decode(a_great_sentence)