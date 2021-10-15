from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

# if w3.isConnected():
#     This line will mess with our autograders, but might be useful when debugging
    # print( "Connected to Ethereum node" )
# else:
#     print( "Failed to connect to Ethereum node!" )

def get_transaction(tx):
    w3.eth.get_transaction(tx)
    return tx

# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    return get_transaction(tx).gasPrice

def get_gas(tx):
    return w3.eth.get_transaction_receipt(tx)

def get_transaction_cost(tx):
    return get_gas_price(tx) * get_gas(tx)

def get_block_cost(block_num):
    transactions = w3.eth.get_block(block_num, full_transactions=False).transactions
    result = 0
    for t in transactions:
        result += get_transaction_cost(t)
    return result

# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    transactions = w3.eth.get_block(block_num, full_transactions=False).transactions
    result = 0
    for t in transactions:
        result = max(result, get_transaction_cost(t))
    return result
