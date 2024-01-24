import asyncio

from web3 import Web3
import logging

from web3.contract import Contract

abi = '''[    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }]'''


class MonitorContract:
    _address_balance: dict
    _contract_address: str
    _monitor_addresses: []
    _contract: Contract
    _sleep_time: int
    _monitor: bool

    def __init__(self,
                 connection: Web3,
                 contract_address: str,
                 monitor_addresses: [],
                 sleep_time: int):
        self._conn = connection
        self._monitor_addresses = monitor_addresses
        self._contract_address = contract_address
        self._sleep_time = sleep_time
        self._monitor = True
        self._address_balance = {}
        self._contract = self._conn.eth.contract(address=self._contract_address, abi=abi)

    async def start(self):
        while self._monitor:
            try:
                for addr in self._monitor_addresses:
                    logging.info("Accessing balance for addr: {}".format(addr))
                    balance = self._contract.functions.balanceOf(addr).call()
                    self._address_balance[addr] = Web3.from_wei(balance, 'ether')
            except Exception as e:
                logging.error("Error while monitor address: {}".format(e))
            await asyncio.sleep(self._sleep_time)

    def monitor(self, monitor: bool):
        self._monitor = monitor

    def getAddressBalance(self):
        return self._address_balance