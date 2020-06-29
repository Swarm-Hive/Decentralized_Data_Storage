'''
@Author: Zitian(Daniel) Tong
@Date: 2020-06-28 17:27:51
@LastEditTime: 2020-06-28 22:20:03
@LastEditors: Zitian(Daniel) Tong
@Description: a python script desgined for interacting with smart contracts
@FilePath: /Decentralized_Data_Storage/src/scripts/interation.py
'''

import os
import json
from web3 import Web3
from dotenv import find_dotenv,load_dotenv

# find & load the .env file
load_dotenv(find_dotenv())

# import netowrk url
infural_url = os.environ.get('INFURA_API_KEY_ROPSTEN_HTTPS')
menemonic = os.environ.get('MNEMONIC')
contract_abi = json.loads(os.environ.get('ABI'))
contract_address = os.environ.get('CONTRACT_ADDRESS') 

# connect to web3
web3 = Web3(Web3.HTTPProvider(infural_url))
try:
    web3.isConnected()
except:
    raise Exception('web3 did not successfully connected to the network')

