/*
 * @Author: Zitian(Daniel) Tong
 * @Date: 2020-06-24 16:03:03
 * @LastEditTime: 2020-06-28 17:23:22
 * @LastEditors: Zitian(Daniel) Tong
 * @Description: Smart Contract Code
 * @FilePath: /Decentralized_Data_Storage/src/contracts/DataStorage.sol
 */

pragma solidity ^0.5.0;

// contract code
contract DataStorage {
    string public dappName;         // name of dapp
    uint256 public contractVersion = 1; // contract version
    uint256 public dataIndex = 0;       // index of data
    uint256 public lastCalledTimeStamp;

    // define category enum
    enum dataCategory { normal, traffic_data, incident}

    // define the data structure
    struct DataStorageEvent {
        uint256 timeStamp;
        uint256 version;
        uint256 index;
        dataCategory category;
        string data;
    }

    // mapping address to DataStorageEvents
    mapping(uint256 => DataStorageEvent) public DataStorageEvents;

    // contract constractor
    constructor() public {
        dappName = "Data Storage - V1";
    }

    // broadcast datastruct
    event broadcastDataEvent(
        uint256 timeStamp,
        uint256 version,
        uint256 index,
        dataCategory category,
        string data
    );

    function broadcastData(
        uint256 _category,  // category of data
        string memory _data             // data string
    ) public {
        // some requirements before executing the function
        require(_category >= 0 && _category <= 2, "The category should be in the correct range!" );
        require(bytes(_data).length > 0, "The data should not be empty!");

        // accumulate the dataIndex
        dataIndex++;
        // get current timestamp
        lastCalledTimeStamp = now;

        // save info to the local datastruct
        DataStorageEvents[dataIndex] = DataStorageEvent(
            lastCalledTimeStamp,
            contractVersion,
            dataIndex,
            dataCategory(_category),
            _data
        );

        // broadcast to the network
        emit broadcastDataEvent(
            DataStorageEvents[dataIndex].timeStamp,
            DataStorageEvents[dataIndex].version,
            DataStorageEvents[dataIndex].index,
            DataStorageEvents[dataIndex].category,
            DataStorageEvents[dataIndex].data
        );
    }

}