const DataStorage = artifacts.require("DataStorage");
require('chai')
.use(require('chai-as-promised'))
.should();

contract(DataStorage,([deployer, sender_1, sender_2, sender_3])=>{
    let datastorage;
    before(async () =>{
        datastorage = await DataStorage.deployed();
    });

    // deployment test
    describe('Deployment', async()=>{
        it("deploys successully", async() => {
            const address = await datastorage.address;
            assert.notEqual(address, 0x0);
            assert.notEqual(address, '');
        })
        
        
        it("deploys correct name", async() => {
            const name = await datastorage.dappName();
            assert.equal(name, "Data Storage - V1");
        })
        
    });

});