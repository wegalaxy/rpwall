import asyncio

from PIL import Image
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

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'font')

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def get_monitor_addresses():
    return urllib.request.urlopen(os.environ["MONITOR_ACCOUNT_PATH"], context=ssl_context).read().decode('utf-8').splitlines()


async def load_image(mc):
    try:
        imagePath = os.path.join(picdir, 'framebg.jpg')
        logging.info("Loading Image @ %s", imagePath)
        fontPath = os.path.join(fontdir, 'SourceSans3-Regular.ttf')
        logging.info("Loading Font @ %s", fontPath)
        from display import eink_load
        while True:
            eink_load.load_leaderboard(mc.getAddressBalance(), imagePath, fontPath)
            await asyncio.sleep(10)
    except RuntimeError as e:
        logging.warning("Error launching eink, skipping for now: {}".format(e))


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
    load_image()
    asyncio.run(start())

