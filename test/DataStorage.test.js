/*
 * @Author: Zitian(Daniel) Tong
 * @Date: 2020-06-24 16:03:03
 * @LastEditTime: 2020-07-02 22:07:03
 * @LastEditors: Zitian(Daniel) Tong
 * @Description: 
 * @FilePath: /Decentralized_Data_Storage/test/DataStorage.test.js
 */ 
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
        it("checks the broadcasted data", async() => {
            assert.equal(numData, 1);   // only one data now
            assert.equal(version, 1);   // version equals to 1
            const event = result.logs[0].args;
            assert.equal(event.data, "test-test-test") ;    // check the broadcasted data is correct  
        })

        // check the submitted time is within couple seconds
        it("checks the submitted timestamp", async() => {
            // Date.now returns the millseconds, and timeStamp from solidity returns seconds
            assert.closeTo(timeStamp.toNumber(), Date.now()/1000, 2, "comparing time"); // if within 2 secs, then ok
        })

    });

    // test 3 - retrive data test
    describe("Test 3 - Retrive the Data Tests", async() => {
        let result, numData, version, timeStamp;

        // submit a data to the network
        before(async() => {
            result = await datastorage.broadcastData(1, "test-from-task3");
            numData = await datastorage.dataIndex();
            version = await datastorage.contractVersion();
            timeStamp = await datastorage.lastCalledTimeStamp();
            retrived_first_test = await datastorage.retrieveData(1);
            retrived_second_test = await datastorage.retrieveData(2);
        })

        it("checks the broadcasted data", async() => {
            assert.equal(numData, 2); // two data set now
            assert.equal(version, 1);   // version equals to 1
        })

        it("checks the retrived data", async() => {
            assert.equal(retrived_first_test.data, "test-test-test");    // check 1st data
            assert.equal(retrived_second_test.data, "test-from-task3");  // check 2nd data
        })

        it("checks to retrived the wrong index", async() => {
            // test if retived from number larger than numData
            await datastorage.retrieveData(3).should.be.rejected;
            await datastorage.retrieveData(1000).should.be.rejected;
        })
        

    })
    

});