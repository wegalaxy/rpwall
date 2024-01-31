import asyncio

from display import view
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


async def load_image(mc):
    try:
        imagePath = os.path.join(os.environ["IMG_DIR"], 'db1.jpg')
        fontPath = os.path.join(os.environ["FONT_DIR"], 'SourceSans3-Regular.ttf')
        vc = view.ViewController(imagePath, fontPath)
        while True:
            vc.clear_image()
            vc.add_player("100")
            vc.add_guess_game("40")
            vc.add_jackpot("500000")
            vc.add_reference("534534")
            vc.add_game_id("1004")
            vc.add_node_ip("1.1.1.1")
            vc.add_refresh_time("now")
            vc.load_image()
            await asyncio.sleep(180)
    except RuntimeError as e:
        logging.warning("Error launching eink, skipping for now: {}".format(e))


async def start():
    w3conn = connection.initiate_connection(os.environ["NODE_PROVIDER"])
    mc = monitor_contract.MonitorContract(
                w3conn,
                os.environ["ERC20_CONTRACT"],
                os.environ["GAME_CONTRACT"],180)

    t1 = asyncio.create_task(mc.start())
    t2 = asyncio.create_task(load_image(mc))

    await t1
    await t2

if __name__ == '__main__':
    asyncio.run(start())

