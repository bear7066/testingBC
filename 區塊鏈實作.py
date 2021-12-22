import time
import hashlib


## 設定區塊內的內容
class Transaction:
    def __init__(self, gender, receiver, amounts, fee, message):
        self.gender = gender
        self.receiver = receiver
        self.amounts = amounts
        self.fee = fee
        self.message = message

class Block:
    def __init__(self, previous_hash, difficulty, miner, miner_rewards):
        self.previous_hash = previous_hash
        self.hash = ''
        self.difficulty = difficulty
        self.nounce = 0
        self.timestamp = int(time.time())
        self.transactions = []
        self.miner =miner
        self.miner_rewards = miner_rewards


#設定區塊鏈的一些限制，如區塊數、每多少個區塊調整一次難度等等
class BlockChain:
    def __init__(self):
        self.adjust_difficulty_blocks = 10
        self.difficulty = 1
        self.block_time = 30
        self.mining_rewards = 10
        self.block_limitaion = 32
        self.chain = []
        self.pending_transactions = []


#定義交易格式
def transaction_to_string(self, transaction):
    transaction_dict = {
        'sender': str(transaction.sender),
        'receiver': str(transaction.receiver),
        'amounts': transaction.amounts,
        'fee': transaction.fee,
        'message': transaction.message,
    }
    return str(transaction_dict)


##將transactions明細轉換成字串  
##get_transactions_string負責把區塊紀錄的所有交易明細轉換成一個字串
def get_transactions_string(self,block):
    transaction_str = ''
    for transaction in block.transactions:
        transaction_str += self.transaction_to_string(transaction)
    return transaction_str


##設定要用哪款hash及hash甚麼 
##h = s.hexdigest()為取得hash值 
def get_hash(self, block, nounce):
    s = hashlib.sha1()
    s.update(
        (
            block.previous_hash
            + str(block.timestamp)
            + self.get_transactions_string(block)
            + str(nounce)
        ).encode("utf-8")
    )
    h = s.hexdigest()
    return h


##建立第一個區塊並設定Block內的參數
def create_genesis_block(self):
    print("Generating genesis block...")
    new_block = Block('First Block', self.difficulty, 'User1', self.miner_rewards)
    new_block.hash = self.get_hash(new_block, 0)
    self.chain.append(new_block)


##此為放置交易紀錄的函式，能夠選擇手續費最高的交易優先加入，也就是gas fee 最高者。
##上述功能的啟動條件為區塊內的交易量超過乘載量的上限，若沒有超過則依序處理
def add_transaction_to_block(self, block):
    self.pending_T.sort(key=lambda x:x[1], reverse=True)
    if len(self.pending_T) > self.block_limitation:
        transaction_accepted = self.pending_T[:self.block_limitation]
        self.pending_T = self.pending_T[self.block_limitation:]
    else:
        transaction_accepted = self.pending_T
        self.pending_T = []
        block.transactions = transaction_accepted


##挖礦函式，啟動後會不停地尋找正確的nounce，一旦解出來，就可以為區塊鏈設置新的區塊
##以礦工的角度來看，就是得到一枚比特幣
def mine_block(self, miner):
    start = time.process_time()

    last_block = self.chain[-1]
    new_block = Block(last_block.hash, self.difficulty, miner, self.miner_rewards)
    
    self.add_transaction_to_block(new_block)
    new_block.previous_hash = last_block.hash
    new_block.difficulty = self.difficulty
    new_block.hash = self.get_hash(new_block,new_block.nounce)

    while new_block.hash[0:self.difficulty] != '0' * self.difficulty:
        new_block.nounce += 1
        new_block.hash = self.get_hash(new_block, new_block.nounce)

    time_consumed = round(time.process_time() - start, 5)
    print("Hash found: {new_block.hash} @ difficulty {self.difficulty}, time cost: {time_consumed}")
    self.chain.append(new_block)
