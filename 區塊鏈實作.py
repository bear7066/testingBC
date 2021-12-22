## 設定區塊內的內容
import time

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


##引入hash function 加密機制
import hashlib

def transaction_to_string(self, transaction):
    transaction_dict = {
        'sender': str(transaction.sender),
        'receiver': str(transaction.receiver),
        'amounts': transaction.amounts,
        'fee': transaction.fee,
        'message': transaction.message,
    }
    return str(transaction_dict)

##將transactions明細轉換成字串  ##get_transactions_string負責把區塊紀錄的所有交易明細轉換成一個字串
def get_transactions_string(self,block):
    transaction_str = ''
    for transaction in block.transactions:
        transaction_str += self.transaction_to_string(transaction)
    return transaction_str

##設定要用哪款hash及hash甚麼 ## h = s.hexdigest()為取得hash值 ## .encode("utf-8")將存入的資料轉為str
## update內皆須為字串
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


     