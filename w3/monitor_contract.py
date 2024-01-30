import asyncio

import w3.abi
from web3 import Web3
import logging

from web3.contract import Contract


class MonitorContract:
    _game_result: dict
    _game_contract: Contract
    _erc_contract: Contract
    _sleep_time: int
    _monitor: bool

    def __init__(self,
                 connection: Web3,
                 erc_contract_address: str,
                 game_contract_address: str,
                 sleep_time: int):
        self._sleep_time = sleep_time
        self._monitor = True
        self._game_result = {}
        self._game_contract = connection.eth.contract(address=game_contract_address, abi=w3.abi.abi_game_contract)
        self._erc_contract = connection.eth.contract(address=erc_contract_address, abi=w3.abi.abi_erc20)

    async def start(self):
        while self._monitor:
            try:
                currentGameId = self._game_contract.functions.currentGameId().call()
                for addr in self._game_contract.functions.getGamePlayers(currentGameId).call():
                    logging.info("Accessing balance for addr: {}".format(addr))
                    balance = self._erc_contract.functions.balanceOf(addr).call()
                    self._game_result[addr] = Web3.from_wei(balance, 'ether')
            except Exception as e:
                logging.error("Error while monitor address: {}".format(e))
            await asyncio.sleep(self._sleep_time)

    def monitor(self, monitor: bool):
        self._monitor = monitor

    def getGameResult(self):
        return self._game_result