pragma solidity ^0.4.17;

contract Payment {
  address transferFrom;
  address transferTo1;
  address transferTo2;
  address transferTo3;

  constructor() public {
    transferFrom = msg.sender;
  }

  event TransferFund(address _transferTo1, address _transferTo2, address _transferTo3, address _transferFrom, uint amount);

  function transferFund( address _transferTo1, address _transferTo2, address _transferTo3 ) public payable returns (bool){
      transferTo1 = _transferTo1;
      transferTo2 = _transferTo2;
      transferTo3 = _transferTo3;

      transferTo1.transfer(msg.value/3);
      transferTo2.transfer(msg.value/3);
      transferTo3.transfer(msg.value/3);

      emit TransferFund(transferTo1, transferTo2, transferTo3, transferFrom, msg.value/3);

      return true;
  }

  function getBalanceOfCurrentAccount() public payable returns (uint) {
    return transferFrom.balance;
  }

}
