import asyncio

import w3.abi
from web3 import Web3
import logging

from web3.contract import Contract


class ContractResult:
    gameId: int
    guesses: int
    players: int
    game_result: dict


class MonitorContract:
    _game_result: ContractResult
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
        self._game_result = ContractResult()
        self._game_contract = connection.eth.contract(address=game_contract_address, abi=w3.abi.abi_game_contract)
        self._erc_contract = connection.eth.contract(address=erc_contract_address, abi=w3.abi.abi_erc20)

    async def start(self):
        while self._monitor:
            try:
                c = ContractResult()
                self._game_result = c
                c.gameId = self._game_contract.functions.currentGameId().call()
                c.guesses = len(self._game_contract.functions.getRates(c.gameId).call())
                c.players = self._game_contract.functions.getPlayerCount(c.gameId).call()
                '''
                    for addr in self._game_contract.functions.getPlayers(c.gameId).call():
                    logging.info("Accessing balance for addr: {}".format(addr))
                    balance = self._erc_contract.functions.balanceOf(addr).call()
                    c.game_result[addr] = Web3.from_wei(balance, 'ether')
                '''
            except Exception as e:
                logging.error("Error while monitor address: {}".format(e))
            await asyncio.sleep(self._sleep_time)

    def monitor(self, monitor: bool):
        self._monitor = monitor

    def get_game_result(self):
        return self._game_result