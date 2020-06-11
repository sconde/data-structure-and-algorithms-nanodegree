"""
Problem 3: Huffman Coding
"""

import sys
import collections

class Node(object):
    
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    @staticmethod
    def fusion_nodes(first, second):

        fused_node = Node(
            freq=(first.freq + second.freq)
            )
        
        if first.freq <= second.freq:
            fused_node.left = first
            fused_node.right = second
        else:
            fused_node.left = second
            fused_node.right = first

        return fused_node

class Queue(object):
    def __init__(self, string):
        c = collections.Counter(string)
        self.arr = [
            Node(char=ltr, freq=c[ltr]) for ltr in c
        ]

        self.sort()

    def sort(self):
        self.arr = sorted(
            self.arr,
            key=lambda x: x.freq,
            reverse=True
        )

    def fused_step(self):
        low_node_1 = self.arr.pop()
        low_node_2 = self.arr.pop()

        self.arr.append(
            Node.fusion_nodes(first=low_node_1, second=low_node_2)
        )
        self.sort()

class Tree(object):
    def __init__(self, queue):
        while len(queue.arr) > 1:
            queue.fused_step()
        
        self.root = queue.arr[0]

    def binaryze(self):
        self.root = self._add_binary_code(self.root)
        self.root.freq = 0

    @staticmethod
    def _add_binary_code(node):
        if (node.left is Node) and (node.right is None):
            return node
        
        if node.left is not None:
            node.left.freq = 1
            node.left = Tree._add_binary_code(node.left)

        if node.right is not None:
            node.right.freq = 0
            node.right = Tree._add_binary_code(node.right)

        return node

class HuffmanEncoder(object):
    
    def __init__(self, tree):
        self.table = self._create_encoding_table(
            base_code="",
            node=tree.root
        )

        self.encode_dict = None
        self.decode_dict = None

        self._create_encoder()
        self._create_decoder()

    def _create_encoder(self):
        encode_dict = {}
        #TODO: no need for enumerate here
        for el in self.table:
            encode_dict[el[0]] = el[1]
        
        self.encode_dict = encode_dict

    def _create_decoder(self):
        decoder_dict = {}

        for el in self.table:
            decoder_dict[el[1]] = el[0]

        self.decode_dict = decoder_dict

    def encode(self, text):
        coded_text = ""
        for c in text:
            coded_text += self.encode_dict[c]
        
        return coded_text

    def decode(self, encoded_text):
        decoded_text = ""
        
        while len(encoded_text) > 0:
            i_decoder = 1
            while True:
                if encoded_text[:i_decoder] in self.decode_dict.keys():
                    decoded_text += self.decode_dict[encoded_text[:i_decoder]]
                    encoded_text = encoded_text[i_decoder:]
                    break
                i_decoder += 1
        
        return decoded_text

    @staticmethod
    def _create_encoding_table(base_code, node):
        
        if (node.left is None) and (node.right is Node):
            return [
                (node.char, base_code+str(node.freq))
            ]

        if node.freq == -1:
            current_code = ""
        else:
            current_code = base_code + str(node.freq)

        coding_dict = []

        if node.char is not None:
            coding_dict.append(
                (node.char, current_code+str(node.freq))
            )
        
        if node.left is not None:
            coding_dict.extend(
                HuffmanEncoder._create_encoding_table(
                    current_code, node.left
                )
            )
        
        if node.right is not None:
            coding_dict.extend(
                HuffmanEncoder._create_encoding_table(
                    current_code, node.right
                )
            )

        return coding_dict

def huffman_encoding(data):
    
    if len(data) == 0:
        return

    temp_quue = Queue(string=data)
    temp_tree = Tree(queue=temp_quue)
    temp_tree.binaryze()
    temp_encoder = HuffmanEncoder(temp_tree)

    return (
        temp_encoder.encode(data),
        temp_encoder
    )

def huffman_decoding(data,encoder):
    
    return encoder.decode(data)

if __name__ == "__main__":

    # Normal Cases:
    # Case 1
    print('Case 1:')

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 69
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 36
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 0001011011101000111001010010011000000001000011101110100110001111010010

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 69
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The bird is the word

    # Case 2
    print('Case 2:')

    a_great_sentence = "I just want to have fun coding"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 79
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The size of the data is: 79

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 40
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 00110110011100010010010111001011000000010111101100111010101000010110100
    # 0110100100010000110111010010111101100000001101

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 79
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: I just want to have fun coding

    # Case 3
    print('Case 3:')

    a_great_sentence = "The sun shines and I go to the beach"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 85
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The sun shines and I go to the beach

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 44
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 1001011011101000110011001001000111010000001011100010100110010100010110110
    # 01101110000001000010000001000011101110110100111001110101110

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 85
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The sun shines and I go to the beach

    # Edge Cases
    # Case 4
    print('Edge Cases:')
    print('Case 4:')

    a_not_so_great_sentence = "aaa"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_not_so_great_sentence)))
    # The size of the data is: 52
    print("The content of the data is: {}\n".format(a_not_so_great_sentence))
    # The content of the data is: aaa

    encoded_data, tree = huffman_encoding(a_not_so_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 24
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 000

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 52
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: aaa

    # Case 5
    print('Case 5:')
    a_not_so_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(a_not_so_great_sentence)))
    # The size of the data is: 49
    print("The content of the data is: {}\n".format(a_not_so_great_sentence))
    # The content of the data is:

    huffman_encoding(a_not_so_great_sentence)
    # Please introduce a non null string