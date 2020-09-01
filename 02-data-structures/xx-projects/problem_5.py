"""
Problem 5: Blockchain
"""

import hashlib
import time
import pprint


class Block(object):

    def __init__(self, data, timestamp, previous_hash=0):
        self.timestamp = timestamp
        self.data = data
        self.prev = None
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)


    @staticmethod
    def calc_hash(data, encoding='utf-8'):
        """
        calculate the hash

        @param data:
        @param encoding:
        @return:
        """
        sha = hashlib.sha256()
        sha.update(
            data.encode(encoding)
        )
        return sha.hexdigest()


class BlockChain(object):

    def __init__(self):
        self.tail = None

    def append(self, data, timestamp):
        """
        Append block to the end of the list

        @param timestamp:
        @param data:
        @return:
        """

        if self.tail is None:
            self.tail = Block(data, timestamp)
            return

        new_block = Block(data, self.tail.timestamp, previous_hash=self.tail.hash)
        new_block.prev = self.tail
        self.tail = new_block

    def size(self):

        this_block = self.tail
        this_size = 0

        while this_block:
            this_size += 1
            this_block = this_block.prev

        return this_size

    def to_list(self):

        this_list = []
        this_block = self.tail

        while this_block:
            this_list.append(
                [
                    this_block.data, this_block.timestamp, this_block.previous_hash
                ]
            )

            this_block = this_block.prev

        return this_list


blockchain = BlockChain()

print(blockchain.size())  # 0
pprint.pprint(blockchain.to_list())  # []

blockchain.append('1st Block', time.time())
print(blockchain.size())
# 1
pprint.pprint(blockchain.to_list())
# [['my balance: 0 | cash flow: +10 | final balance: 10', 1564306421.0008988, '5e5a93abe59f9e92b38e00ebc7a50c50f902f5a8
# 210d327590a36ffb25a831d9']]

blockchain.append('second block', time.time())
blockchain.append('third block', time.time())
blockchain.append('fourth block', time.time())
blockchain.append('final block', time.time())
print(blockchain.size())
# 5
pprint.pprint(blockchain.to_list())
# [['my balance: 145 | cash flow: +5 | final balance: 150', 1564306378.6235423, '43841086a72ab23dacc07ac04341357ed73
# 51a07f8c8f0df92056cd439f49302'], ['my balance: 20 | cash flow: +125 | final balance: 145', 1564306378.6235056, '597f
# 549af039dbb1c79d5e4ae5c347189cf7b8bafc12011f44b0cc06692ade9e'], ['my balance: 35 | cash flow: -15 | final balance: 20'
# , 1564306378.623468, '6da8edd2d3d03bfa69810f7390ce55a64bab5102b79e37c973a4bed4be303e77'], ['my balance: 10 |
# cash flow: +25 | final balance: 35', 1564306378.6234293, 'ed240a001a354b3ee5f36db5ccdbcac1235806a106907feaedd9db02c
# 6ee7dfc'], ['my balance: 0 | cash flow: +10 | final balance: 10', 1564306378.6233213, '5e5a93abe59f9e92b38e00ebc7a50
# c50f902f5a8210d327590a36ffb25a831d9']]
