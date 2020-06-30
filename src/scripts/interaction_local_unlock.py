
'''
@Author: Zitian(Daniel) Tong
@Date: 2020-06-28 17:27:51
@LastEditTime: 2020-06-29 21:10:08
@LastEditors: Zitian(Daniel) Tong
@Description: a python script desgined for interacting with smart contracts
@FilePath: /Decentralized_Data_Storage/src/scripts/interaction_vm.py
'''

import os
import json
import numpy as np
from web3 import Web3

# assign test account's info
print("==================================== Loading ====================================")
infural_url = 'HTTP://127.0.0.1:7545'
wallet_address = '0xe72531CABdB31dE0E5F9F10292D26AA2F8b02996'
private_key = '4e59b04688f906db53d73d71485b1d959309a0d354072c7dba4e069ee393b325'
contract_abi = json.loads('[ { "constant": false, "inputs": [ { "name": "_category", "type": "uint256" }, { "name": "_data", "type": "string" } ], "name": "broadcastData", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "timeStamp", "type": "uint256" }, { "indexed": false, "name": "version", "type": "uint256" }, { "indexed": false, "name": "index", "type": "uint256" }, { "indexed": false, "name": "category", "type": "uint8" }, { "indexed": false, "name": "data", "type": "string" } ], "name": "broadcastDataEvent", "type": "event" }, { "constant": true, "inputs": [], "name": "contractVersion", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "currentTimeStamp", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "dappName", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "dataIndex", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "uint256" } ], "name": "DataStorageEvents", "outputs": [ { "name": "timeStamp", "type": "uint256" }, { "name": "version", "type": "uint256" }, { "name": "index", "type": "uint256" }, { "name": "category", "type": "uint8" }, { "name": "data", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')
contract_address = '0xAA04BD16de4BdE6Ae90F210DDB800d8F72468832'
print("Infura_API: {}".format(infural_url))
print("Private_Key: {}".format(private_key))
print("contract_address: {}".format(contract_address))


# connect to web3
print("=============================== Connect to Network ==============================")
web3 = Web3(Web3.HTTPProvider(infural_url))
try:
    web3.isConnected()
    web3.eth.defaultAccount = web3.eth.accounts[0]
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
).transact()

