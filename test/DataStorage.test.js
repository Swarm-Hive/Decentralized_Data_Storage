const { assert } = require('chai');

const DataStorage = artifacts.require("DataStorage");
require('chai')
.use(require('chai-as-promised'))
.should();

contract(DataStorage,([deployer, sender_1, sender_2, sender_3])=>{
    let datastorage;
    before(async() =>{
        datastorage = await DataStorage.deployed();
    });

    // test 1 - deployment test
    describe("Test 1 - Smart Contract Deployment", async()=>{
        it("deploys successully", async() => {
            const address = await datastorage.address;
            assert.notEqual(address, 0x0);
            assert.notEqual(address, '');
        })
        
        
        it("deploys correct dapp name", async() => {
            const name = await datastorage.dappName();
            assert.equal(name, "Data Storage - V1");
        })
    });

    // test 2 - broadcast test
    describe("Test 2 - Broadcast Data Tests", async() => {
        let result, numData, version, timeStamp;

        // submit a data to the network
        before(async() => {
            result = await datastorage.broadcastData(1, "test-test-test");
            numData = await datastorage.dataIndex();
            version = await datastorage.contractVersion();
            timeStamp = await datastorage.lastCalledTimeStamp();
        })
        
        // check the submitted data is correct
        it("Checking the broadcasted Data", async() => {
            assert.equal(numData, 1);   // only one data now
            assert.equal(version, 1);   // version equals to 1
            const event = result.logs[0].args;
            assert.equal(event.data, "test-test-test") ;    // check the broadcasted data is correct  
        })

        // check the submitted time is within couple seconds
        it("Checking the submitted timestamp", async() => {
            // Date.now returns the millseconds, and timeStamp from solidity returns seconds
            assert.closeTo(timeStamp.toNumber(), Date.now()/1000, 2, "comparing time"); // if within 2 secs, then ok
        })

    });
    

});