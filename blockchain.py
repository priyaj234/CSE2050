from hashmap import Hashmap
class Transaction():
    def __init__(self, from_user, to_user, amount):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount
    def __hash__(self):
        hash((self.from_user, self.to_user, self.amount))
    
class Block():
    def __init__(self, transactions=None):
        self.prev_hash = None
        if transactions == None:
            self.transactions = list()
        else:
            self.transactions = transactions
    def update_prevhash(self, ph):
        self.prev_hash = ph
    def __hash__(self):
        hash((tuple(self.transactions), self.prev_hash))
    def add_transaction(self, trans):
        self.transactions.append(trans)

class Ledger():
    def __init__(self):
        self.hashmap = Hashmap()
    
    def has_funds(self, user, amount):
        if user not in self.hashmap:
             return False
        balance = self.hashmap.get(user)
        return balance >= amount

    def deposit(self, user, amount):
        x = self.hashmap._dict[user]
        self.hashmap._dict[user] = x + amount 
    def withdrawl(self, user, amount):
        x = self.hashmap._dict[user]
        if x >= amount:
            self.hashmap._dict[user] = x - amount 

class Blockchain():
    '''Contains the chain of blocks.'''

    #########################
    # Do not use these three values in any code that you write. 
    _ROOT_BC_USER = "ROOT"            # Name of root user account.  
    _BLOCK_REWARD = 1000              # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = 999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    #########################

    def __init__(self):
        self._blockchain = list()     # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()    # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()

    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        '''Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users'''
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        '''
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        (In the Bitcoin network, users compete to solve a meaningless mathmatical puzzle.
        Solving the puzzle takes a tremendious amount of copmputing power and consuming a lot
        of energy. The first node to solve the puzzle is given a certain amount of Bitcoin.)
        In this assigment, you do not need to understand "mining." Just use this method to 
        provide initial balances to one or more users.'''
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block([trans])
        self.add_block(block)

    # TODO - add the rest of the code for the class here
    def add_block(self, block):
        x = hash(self._blockchain[-1])
        block.update_prevhash(x)
        transx = True

        for i in block.trans:
            if not self._bc_ledger.has_funds(i.from_user, i.amount):
                transx = False

        if transx:
           for i in block.trans:
                self._bc_ledger.transfer(i.from_user, i.amount)
                self._bc_ledger.deposit(i.to_user, i.amount)
            
           self._blockchain.append(block)    
           return True
        
        else:
            return False
    def validate_chain():
        tampered = []
        for i in range(1, len(self._blockchain)):
            prev_hash = hash(self._blockchain[i-1])
            if prev_hash != self._blockchain[i].prev_hash:
                tampered.append(self._blockchain[i])
        return tampered