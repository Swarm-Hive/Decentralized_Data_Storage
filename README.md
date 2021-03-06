# Decentralized_Data_Storage [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome#readme)
> A Smart Contract Designed by Storing Data

Welcome to our project, this is one of the basic test smart contracts to demo interaction between blockchain network.

## Configuring your environment

1. [Install Node](https://nodejs.org/en/download/), which will also install NPM (you should be able to execute `node --version` and `npm --version` on the command line).

2. [Install Ganache](https://www.trufflesuite.com/ganache), or ganache-cli, a command line version of ganache.

3. Create your own .env file (name .env), and fill the API key and Mnemonic in .env. 
   - To get an API key, go to [Infura](https://infura.io/)
   - To get an wallet mnemonic, install chrome extension [metamask](https://metamask.io/)

Note: if your node version is V14+, use '--skipDryRun' detailed reason can be seen on [issue #1](https://github.com/Swarm-Hive/Decentralized_Data_Storage/issues/1)

## User Guide - Ethereum Part

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
```

## User Guide - Interaction with Blockcain Part

you need to install web3.py in order to run python scripts

```shell
# Install pip if it is not available:
which pip || curl https://bootstrap.pypa.io/get-pip.py | python

# Install virtualenv if it is not available:
which virtualenv || pip install --upgrade virtualenv

# *If* the above command displays an error, you can try installing as root:
sudo pip install virtualenv

# Create a virtual environment:
virtualenv -p python3 ~/.venv-py3

# Activate your new virtual environment:
source ~/.venv-py3/bin/activate

# With virtualenv active, make sure you have the latest packaging tools
pip install --upgrade pip setuptools

# Now we can install web3.py...
pip install --upgrade web3
```
