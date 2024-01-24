import asyncio

from dotenv import load_dotenv
import logging
from w3 import connection, monitor_contract
import os
import urllib.request
import ssl
import certifi
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())

load_dotenv()

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

async def print(mc):
    while True:
        for a, b in sorted(mc.getAddressBalance().items(), key=lambda x:x[1], reverse=True):
            logging.info("{}: {}".format(a, b))
        await asyncio.sleep(10)


def get_monitor_addresses():
    return urllib.request.urlopen(os.environ["MONITOR_ACCOUNT_PATH"], context=ssl_context).read().decode('utf-8').splitlines()


async def start():
    w3conn = connection.initiate_connection(os.environ["NODE_PROVIDER"])
    mc = monitor_contract.MonitorContract(
                w3conn,
                os.environ["MONITOR_CONTRACT"],
                get_monitor_addresses(),60)
    t1 = asyncio.create_task(mc.start())
    t2 = asyncio.create_task(print(mc))

    await t1
    await t2

if __name__ == '__main__':
    asyncio.run(start())

