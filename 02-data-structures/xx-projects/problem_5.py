"""
Problem 5: Blockchain
"""

import hashlib
import time

class Block(object):
    
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    @staticmethod
    def calc_hash(data, encoding='utf-8'):
        
        sha = hashlib.sha256()
        sha.update(data.encode(encoding))

        return sha.hexdigest()


class BlockChain(object):
    
    def __init__(self):
        self.tail = None

    def append(self, data):

        if self.tail is None:
            self.tail = Block(data, None)
        else:
            self.tail = Block(data, self.tail)

    def search(self, data):
        
        if self.tail is None:
            return
        
        head = self.tail

        while head.previous_hash:
            if head.data == data:
                return head
            head = head.previous_hash
        
        return None

    def size(self):
        
        head = self.tail
        this_size = 0

        while head is not None:
            this_size += 1
            head = head.previous_hash
        
        return this_size

    def to_list(self):
        
        this_list = []
        
        head = self.tail

        while head:
            this_list.append(
                [
                    head.data, head.timestamp, head.hash
                ]
            )

            head = head.previous_hash

        return this_list

if __name__ == "__main__":

    #%% Testing official
    blockchain = BlockChain()

    print(blockchain.size())
    # 0
    print(blockchain.to_list())
    # []

    blockchain.append('my balance: 0 | cash flow: +10 | final balance: 10')
    print(blockchain.size())
    # 1
    print(blockchain.to_list())
    # [['my balance: 0 | cash flow: +10 | final balance: 10', 1564306421.0008988, '5e5a93abe59f9e92b38e00ebc7a50c50f902f5a8
    # 210d327590a36ffb25a831d9']]

    blockchain.append('my balance: 10 | cash flow: +25 | final balance: 35')
    blockchain.append('my balance: 35 | cash flow: -15 | final balance: 20')
    blockchain.append('my balance: 20 | cash flow: +125 | final balance: 145')
    blockchain.append('my balance: 145 | cash flow: +5 | final balance: 150')
    print(blockchain.size())
    # 5
    print(blockchain.to_list())
    # [['my balance: 145 | cash flow: +5 | final balance: 150', 1564306378.6235423, '43841086a72ab23dacc07ac04341357ed73
    # 51a07f8c8f0df92056cd439f49302'], ['my balance: 20 | cash flow: +125 | final balance: 145', 1564306378.6235056, '597f
    # 549af039dbb1c79d5e4ae5c347189cf7b8bafc12011f44b0cc06692ade9e'], ['my balance: 35 | cash flow: -15 | final balance: 20'
    # , 1564306378.623468, '6da8edd2d3d03bfa69810f7390ce55a64bab5102b79e37c973a4bed4be303e77'], ['my balance: 10 |
    # cash flow: +25 | final balance: 35', 1564306378.6234293, 'ed240a001a354b3ee5f36db5ccdbcac1235806a106907feaedd9db02c
    # 6ee7dfc'], ['my balance: 0 | cash flow: +10 | final balance: 10', 1564306378.6233213, '5e5a93abe59f9e92b38e00ebc7a50
    # c50f902f5a8210d327590a36ffb25a831d9']]

    # Testing the "search function"
    print(blockchain.search('my balance: 20 | cash flow: +125 | final balance: 145'))
    # Block is:
    # Data: my balance: 20 | cash flow: +125 | final balance: 145
    # Timestamp: 1564305924.884146
    # Hash: 597f549af039dbb1c79d5e4ae5c347189cf7b8bafc12011f44b0cc06692ade9e


    # Edge Cases:
    print(blockchain.search('my balance: 1000 | cash flow: +100 | final balance: 1100'))
    # None

    blockchain = BlockChain()
    print(blockchain.search('my balance: 20 | cash flow: +125 | final balance: 145'))
    # Please 'append' data on the BlockChain before searching for it