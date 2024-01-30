abi_erc20 = '''[    {
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

abi_game_contract = '''
[{"inputs":[{"internalType":"address","name":"tokenContract","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":false,"internalType":"bytes32","name":"hash","type":"bytes32"},{"indexed":false,"internalType":"uint64","name":"startUnixTime","type":"uint64"},{"indexed":false,"internalType":"uint64","name":"endUnixTime","type":"uint64"},{"indexed":false,"internalType":"uint256","name":"fundPerGuessing","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"rewardPercentage","type":"uint256"}],"name":"GameCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"gameId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"number","type":"uint256"},{"indexed":false,"internalType":"string","name":"greeting","type":"string"},{"indexed":false,"internalType":"uint256","name":"rewardPerWinner","type":"uint256"}],"name":"GameRevealed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"gameId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"number","type":"uint256"}],"name":"PlayerGuessed","type":"event"},{"inputs":[],"name":"currentGameId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fundTokenContract","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"gameId","type":"uint256"}],"name":"gameExists","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"games","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"targetNumber","type":"uint256"},{"internalType":"string","name":"greeting","type":"string"},{"internalType":"bytes32","name":"hash","type":"bytes32"},{"internalType":"uint64","name":"startUnixTime","type":"uint64"},{"internalType":"uint64","name":"endUnixTime","type":"uint64"},{"internalType":"uint256","name":"fundPerGuessing","type":"uint256"},{"internalType":"uint256","name":"totalFund","type":"uint256"},{"internalType":"bool","name":"revealed","type":"bool"},{"internalType":"uint256","name":"rewardPercentage","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"targetNumber","type":"uint256"},{"internalType":"string","name":"greeting","type":"string"}],"name":"generateGameHash","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"gameId","type":"uint256"},{"internalType":"uint256","name":"number","type":"uint256"}],"name":"getGameNumberGuesses","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"gameId","type":"uint256"},{"internalType":"address","name":"player","type":"address"}],"name":"getGamePlayerGuess","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"gameId","type":"uint256"}],"name":"getGamePlayers","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"gameId","type":"uint256"}],"name":"getGameWinNumbers","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"gameId","type":"uint256"},{"internalType":"uint256","name":"number","type":"uint256"}],"name":"guess","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"maxTargetNumber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minTargetNumber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"bytes32","name":"hash","type":"bytes32"},{"internalType":"uint64","name":"startUnixTime","type":"uint64"},{"internalType":"uint64","name":"endUnixTime","type":"uint64"},{"internalType":"uint256","name":"fundPerGuessing","type":"uint256"},{"internalType":"uint256","name":"rewardPercentage","type":"uint256"}],"name":"newGame","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"gameId","type":"uint256"},{"internalType":"uint256","name":"number","type":"uint256"},{"internalType":"string","name":"greeting","type":"string"}],"name":"revealTargetNumber","outputs":[],"stateMutability":"nonpayable","type":"function"}]
'''