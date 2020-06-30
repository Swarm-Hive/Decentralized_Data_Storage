'''
@Author: Zitian(Daniel) Tong
@Date: 2020-06-29 21:11:46
@LastEditTime: 2020-06-29 22:34:36
@LastEditors: Zitian(Daniel) Tong
@Description: 
@FilePath: /Decentralized_Data_Storage/src/scripts/interaction_local_with_privatekey.py
'''

import os
import json
import numpy as np
from web3 import Web3

# assign test account's info
print("==================================== Loading ====================================")
# replace the following to ur ganache setting
ganache_url = 'HTTP://127.0.0.1:7545'
wallet_address = '0xe72531CABdB31dE0E5F9F10292D26AA2F8b02996'
private_key = '4e59b04688f906db53d73d71485b1d959309a0d354072c7dba4e069ee393b325'
contract_abi = json.loads('[ { "constant": false, "inputs": [ { "name": "_category", "type": "uint256" }, { "name": "_data", "type": "string" } ], "name": "broadcastData", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "timeStamp", "type": "uint256" }, { "indexed": false, "name": "version", "type": "uint256" }, { "indexed": false, "name": "index", "type": "uint256" }, { "indexed": false, "name": "category", "type": "uint8" }, { "indexed": false, "name": "data", "type": "string" } ], "name": "broadcastDataEvent", "type": "event" }, { "constant": true, "inputs": [], "name": "contractVersion", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "currentTimeStamp", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "dappName", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "dataIndex", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "uint256" } ], "name": "DataStorageEvents", "outputs": [ { "name": "timeStamp", "type": "uint256" }, { "name": "version", "type": "uint256" }, { "name": "index", "type": "uint256" }, { "name": "category", "type": "uint8" }, { "name": "data", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')
contract_address = '0xAA04BD16de4BdE6Ae90F210DDB800d8F72468832'
print("Infura_API: {}".format(ganache_url))
print("Private_Key: {}".format(private_key))
print("contract_address: {}".format(contract_address))


# connect to web3
print("=============================== Connect to Network ==============================")
web3 = Web3(Web3.HTTPProvider(ganache_url))
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
