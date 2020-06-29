# Decentralized_Data_Storage [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome#readme)
> A Smart Contract Designed by Storing Data

Welcome to our project, this is one of the basic test smart contracts to demo interaction between blockchain network.

## Configuring your environment

1. [Install Node](https://nodejs.org/en/download/), which will also install NPM (you should be able to execute `node --version` and `npm --version` on the command line).

2. [Install Ganache](https://www.trufflesuite.com/ganache), or ganache-cli, a command line version of ganache.

Note: if your node version is V14+, use '--skipDryRun' detailed reason can be seen on [issue #1](https://github.com/Swarm-Hive/Decentralized_Data_Storage/issues/1)

## Quick Start

```shell
# Clone the repository
git clone git@github.com:Swarm-Hive/Decentralized_Data_Storage.git

# Go inside the directory
cd Decentralized_Data_Storage

# Install dependencies
npm install

# Go inside the directory for smart contract
cd src/Contracts

# Setup contract on Ethereum ropsten test network
truffle compile
truffle migrate --network ropsten --skipDryRun

# Back to root directory
cd ..

