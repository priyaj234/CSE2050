import unittest
from blockchain import Transaction, Block, Ledger, Blockchain
from hashmap import Hashmap

class Tests(unittest.TestCase):
    def test_transaction(self):
        test = Transaction(1, 2, 30)
        test_hashing = Transaction(1, 2, 30)
        self.assertEqual(test.from_user, 1)
        self.assertEqual(test.to_user, 2)
        self.assertEqual(test.amount,  30)
        
        #self.assertEqual(hash(test), hash(test_hashing))
    def test_block_init(self):
        blockone = Block(None)
        blocktwo = Block([4, 32, 3, 10])

        blockone_hash = Block(None)
        blocktwo_hash = Block([4, 32, 3, 10])
        blocktwo_hash.update_prevhash(3)

        self.assertEqual(blockone.transactions, [])
        self.assertEqual(blocktwo.transactions, [4, 32, 3, 10])
        self.assertEqual(blockone.prev_hash, None)
        self.assertEqual(blocktwo_hash.prev_hash, 3)

        #self.assertEqual(hash(blockone), hash(blockone_hash))
        #self.assertEqual(hash(blocktwo), hash(blocktwo_hash))

    def test_block_add_transactions(self):
        blockone = Block(None)
        self.assertEqual(blockone.add_transaction(2), blockone.transactions.append(2))

        

    def test_ledger(self):
        ledge = Ledger()
        self.assertEqual(ledge.hashmap._dict, {})
        
        ledge = Ledger()
        ledge.hashmap._dict = {'Priya':3}
        self.assertEqual(ledge.has_funds('Naomi', 3), False)
        self.assertEqual(ledge.has_funds('Priya', 2), True)
        self.assertEqual(ledge.has_funds('Tam', 4), False)

        self.assertEqual(ledge.hashmap._dict, {'Priya':3})
        ledge.deposit('Priya', 4 )
        self.assertEqual(ledge.hashmap._dict, {'Priya':7})

        ledge.withdrawl('Priya', 3)
        self.assertEqual(ledge.hashmap._dict, {'Priya':4})
        
    def test_blockchain_add_block(self):
        b1 = Blockchain()
        list1 =  [Transaction('Priya', 'Naomi', 4) , Transaction('Naomi', 'Priya', 4)]
        b2 = Block(list1)

        self.assertEqual(b1.add_block(b2), True) 
        self.assertEqual(b1.add_block(b2), False)

        ledger = Ledger()
        ledger.deposit('Priya', 150)
       
        trans1 = [Transaction('Priya', 'Naomi', 100)]
        trans1_block = Block(trans1)
        self.assertEqual(b1.add_block(trans1_block), True) # should evaluate to true

        trans2 = [Transaction('Naomi', 'Priya', 200)] 
        trans2_block = Block(trans2)
        self.assertEqual(b1.add_block(trans2_block), False) # should evaluate to false as fei does not have enough money


        x = b1._blockchain[0]
        self.assertEqual[hash(x), b1._blockchain[1].prev_hash]

        trans3 = [Transaction('Priya', 'Naomi', 100)]
        trans4 = [Transaction('Naomi', 'Priya', 200)] 
        
        block = Block(trans3)
        b1.add_block(block)
        
        block2 = Block(trans4)
        b1.add_block(block2)
        
        tampered_blocks = b1.validate_chain()

        if tampered_blocks:
            for i in tampered_blocks:
                print(i)
        else: print("No Tamp!")

    


unittest.main()