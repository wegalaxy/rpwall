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
    jackpot: int
    players_bid_count: dict


class MonitorContract:
    _prev_game_result: ContractResult
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
                gameId = self._game_contract.functions.currentGameId().call()
                self._game_result = self._getContractResult(gameId)
                self._prev_game_result = self._getContractResult(gameId-1)

                for addr in self._game_contract.functions.getPlayers(gameId).call():
                    self._game_result.players_bid_count[addr] = len(self._game_contract.functions.getRatesByPlayer(gameId, addr).call())

            except Exception as e:
                logging.error("Error while monitor address: {}".format(e))
            await asyncio.sleep(self._sleep_time)

    def _getContractResult(self, gameId):
        c = ContractResult()
        c.gameId = gameId
        game_rez = self._game_contract.functions.games(c.gameId).call()
        c.guesses = game_rez[9]
        c.players = self._game_contract.functions.getPlayerCount(c.gameId).call()
        c.jackpot = Web3.from_wei(game_rez[6], 'ether')
        c.players_bid_count = {}
        return c
    def monitor(self, monitor: bool):
        self._monitor = monitor

    def get_game_result(self):
        return self._game_result

    def get_prev_game_result(self):
        return self._prev_game_result