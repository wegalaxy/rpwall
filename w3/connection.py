from web3 import Web3


def initiate_connection(node_provider: str):
    return Web3(Web3.HTTPProvider(node_provider))

