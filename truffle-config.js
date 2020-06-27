/*
 * @Author: Zitian(Daniel) Tong
 * @Date: 2020-06-24 16:03:03
 * @LastEditTime: 2020-06-26 18:29:24
 * @LastEditors: Zitian(Daniel) Tong
 * @Description:  configuration setting for deploy and set smart contract
 * @FilePath: /Decentralized_Data_Storage/truffle-config.js
 */ 

require('babel-register');
require('babel-polyfill');
require('dotenv').config();

const HDWalletProvider = require("truffle-hdwallet-provider");

module.exports = {
  networks: {
    ropsten: {
      provider: function(){
        return new HDWalletProvider(
          process.env.MNEMONIC,
          process.env.INFURA_API_KEY
        )
      },
      gasPrice: 25000000000,
      network_id: 3
    },
    development: {
      host: "127.0.0.1",
      port: 7545,
      network_id: "*" // Match any network id
    },
  },
  contracts_directory: './src/contracts/',
  contracts_build_directory: './src/abis/',

  compilers: {
    solc: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  }
}
