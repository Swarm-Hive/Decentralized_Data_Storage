'''
@Author: Zitian(Daniel) Tong
@Date: 2020-06-28 17:27:51
@LastEditTime: 2020-06-29 20:29:30
@LastEditors: Zitian(Daniel) Tong
@Description: a python script desgined for interacting with smart contracts
@FilePath: /Decentralized_Data_Storage/src/scripts/interation.py
'''

import os
import json
import numpy as np
from web3 import Web3
from dotenv import find_dotenv,load_dotenv

# find & load the .env file
load_dotenv(find_dotenv())

# import .env variables
print("==================================== Loading ====================================")
infural_url = os.environ.get('INFURA_API_KEY_ROPSTEN_HTTPS')
wallet_address = os.environ.get('WALLET_PUBLIC_ADDRESS')
menemonic = os.environ.get('MNEMONIC')
private_key = os.environ.get('WALLET_PRIVATE_KEY')
contract_abi = json.loads(os.environ.get('ABI'))
contract_address = os.environ.get('CONTRACT_ADDRESS') 
print("Infura_API: {}".format(infural_url))
print("Menemonic: {}".format(menemonic))
print("Private_Key: {}".format(private_key))
print("contract_address: {}".format(contract_address))


# connect to web3
print("=============================== Connect to Network ==============================")
web3 = Web3(Web3.HTTPProvider(infural_url))
try:
    web3.isConnected()
    print('Network connected successfully!')
    acount_balance = web3.eth.getBalance(wallet_address)
    print('Account Balance: {} Ether'.format(web3.fromWei(acount_balance, 'ether')))
except:
    raise Exception('Did not successfully connected to the network!')

# smart contract interaction
print("=========================== Smart Contract Interaction ==========================")

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# get nonce
nonce = web3.eth.getTransactionCount(wallet_address)
print('Nonce Index:',nonce)

# build a transaction that invokes contract's function
contract_tnx = contract.functions.broadcastData(
    1, 
    'test again',
).buildTransaction({
    'chainId': 3,
    'gas': 3000000,
    'gasPrice': web3.toWei(1, 'gwei'),
    'nonce': nonce,
})

signed_txn = web3.eth.account.sign_transaction(contract_tnx, private_key=private_key)
signed_hash = signed_txn.hash
signed_rawTransaction = signed_txn.rawTransaction
signed_r = signed_txn.r
signed_s = signed_txn.s
signed_v = signed_txn.v
print('Signed Transaction Hash:',signed_hash)
print('Signed Transaction Raw:',signed_rawTransaction)
print('Signed Transaction r:',signed_r)
print('Signed Transaction s:',signed_s)
print('Signed Transaction v:',signed_v)

# send transaction
result_txn = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(result_txn)
# When you run sendRawTransaction, you get the same result as the hash of the transaction:
hash_txn = web3.toHex(web3.keccak(signed_txn.rawTransaction))
print(hash_txn)
