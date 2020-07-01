'''
@Author: Zitian(Daniel) Tong
@Date: 2020-06-28 17:27:51
@LastEditTime: 2020-06-30 18:32:53
@LastEditors: Zitian(Daniel) Tong
@Description: a python script desgined for interacting with smart contracts
@FilePath: /Decentralized_Data_Storage/src/scripts/interaction.py
'''

import os
import json
import numpy as np
from web3 import Web3
from termcolor import colored
from dotenv import find_dotenv,load_dotenv


# contrat interaction class
class SmartContractInteraction:
    def __init__(self, url, privatekey, menemonic, contractaddress, walletaddress, abi):
        self.url = url
        self.privatekey = privatekey
        self.menemonic = menemonic
        self.contractaddress = contractaddress
        self.contractabi = abi
        self.walletaddress = walletaddress

    # load contract abi
    def load_contract_abi(self):
        try:
            with open('../abis/DataStorage.json') as f:
                self.contractabi = json.load(f)['abi']
                print( colored('{status}'.format(status = 'ABI.STATUS: SUCCESS!' ), 'grey', 'on_green'), 
                       'ABI LOADED SUCCESSFULLY FROM ABIS FOLDER')
        except:
            raise Exception( colored('{status}'.format(status = 'ABI.STATUS: FAIL!' ), 'grey', 'on_red'), 
                             'ABI FOLDER CANNOT BE FOUND OR OTHER ERROES!!!!')

    # check web3 connection
    def check_web3_connection(self):
        web3 = Web3(Web3.HTTPProvider(self.url))
        try:
            web3.isConnected()
            # prinnt network status if passed the previous
            print(colored('{status}'.format(status = 'Network.STATUS: SUCCESS!' ), 'grey', 'on_green'), 
                       'CONNECTED TO ETHREUM NETWORK SUCCESSFULLY!')
            acount_balance = web3.eth.getBalance(self.walletaddress)
            # print balance
            print(colored('{status}'.format(status = 'ACCOUNT.BALANCE:' ), 'grey', 'on_green'), 
                  colored('{balance} Ether'.format(balance=acount_balance), 'grey', 'on_yellow'))
        except:
            raise Exception(colored('{status}'.format(status = 'Network.STATUS: FAIL!' ), 'grey', 'on_red'), 
                       'Error Occured! NETWORK CONNECTION FAILED!')
    
    # contract interaction
    def contract_interaction(self, msg, networkID):
        web3 = Web3(Web3.HTTPProvider(self.url))
        contract = web3.eth.contract(address=self.contractaddress, abi=self.contractabi)

        # get nonce
        nonce = web3.eth.getTransactionCount(self.walletaddress)

        # build a transaction that invokes contract's function
        contract_tnx = contract.functions.broadcastData(
            1, 
            msg,
        ).buildTransaction({
            'chainId': networkID,
            'gas': 3000000,
            'gasPrice': web3.toWei(1, 'gwei'),
            'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(contract_tnx, private_key=self.privatekey)
        signed_hash = signed_txn.hash
        signed_rawTransaction = signed_txn.rawTransaction
        signed_r = signed_txn.r
        signed_s = signed_txn.s
        signed_v = signed_txn.v
        print(colored('============================= Contract Transaction Summuary =============================', 'grey', 'on_green'))
        print(colored('Signed Transaction Hash:', 'grey', 'on_green'),signed_hash)
        print(colored('Signed Transaction Raw:', 'grey', 'on_green'),signed_rawTransaction)
        print(colored('Signed Transaction r:', 'grey', 'on_green'),signed_r)
        print(colored('Signed Transaction s:', 'grey', 'on_green'),signed_s)
        print(colored('Signed Transaction v:', 'grey', 'on_green'),signed_v)

        # send transaction
        result_txn = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        # When you run sendRawTransaction, you get the same result as the hash of the transaction:
        hash_txn = web3.toHex(web3.keccak(signed_txn.rawTransaction))
        print(colored('Transaction Hash:', 'grey', 'on_green'),hash_txn)
    



if __name__ == '__main__':
    
     # find & load the .env file
    load_dotenv(find_dotenv())

    infural_url = os.environ.get('INFURA_API_KEY_RINKEBY_HTTPS')    # load rinkeby testnet
    wallet_address = os.environ.get('WALLET_PUBLIC_ADDRESS')        # load wallet address
    menemonic = os.environ.get('MNEMONIC')                          # load mnemonic
    private_key = os.environ.get('WALLET_PRIVATE_KEY')              # load private key
    contract_address = os.environ.get('CONTRACT_ADDRESS')           # load cntract address

    # call class to interact with smart contract
    dataStorage = SmartContractInteraction(infural_url, private_key, menemonic, contract_address, wallet_address, 'test')
    dataStorage.check_web3_connection()
    dataStorage.load_contract_abi()
    dataStorage.contract_interaction('test-test-test', 4)

    