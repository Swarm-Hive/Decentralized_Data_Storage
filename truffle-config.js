/*
 * @Author: Zitian(Daniel) Tong
 * @Date: 2020-06-24 16:03:03
 * @LastEditTime: 2020-06-28 17:17:54
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
    // ropsten netowrk
    ropsten: {
      provider: function(){
        return new HDWalletProvider(
          process.env.MNEMONIC,
          process.env.INFURA_API_KEY_ROPSTEN_HTTPS
        )
      },
      gasPrice: 25000000000,
      network_id: 3
    },
    // kovan network
    kovan: {
      provider: function(){
        return new HDWalletProvider(
          process.env.MNEMONIC,
          process.env.INFURA_API_KEY_KOVAN_HTTPS
        )
      },
      gasPrice: 25000000000,
      network_id: 42
    },
    // rinkeby network
    rinkeby: {
      provider: function(){
        return new HDWalletProvider(
          process.env.MNEMONIC,
          process.env.INFURA_API_KEY_RINKEBY_HTTPS
        )
      },
      gasPrice: 25000000000,
      network_id: 4
    },
    // goerli network
    goerli: {
      provider: function(){
        return new HDWalletProvider(
          process.env.MNEMONIC,
          process.env.INFURA_API_KEY_GOERLI_HTTPS
        )
      },
      gasPrice: 25000000000,
      network_id: 5
    },
    // local development
    development: {
      host: "127.0.0.1",
      port: 7545,
      network_id: "*" // Match any network id
    },
  },

  // relative address
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
