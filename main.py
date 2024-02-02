import asyncio

from display import view
from dotenv import load_dotenv
import logging

from datetime import datetime

now = datetime.now() # current date and time

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

import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

async def load_image(mc):
    try:
        imagePath = os.path.join(os.environ["IMG_DIR"], 'db1.gif')
        fontPath = os.path.join(os.environ["FONT_DIR"], 'SourceSans3-Regular.ttf')
        vc = view.ViewController(imagePath, fontPath)
        rez = mc.get_game_result()
        while True:
            vc.clear_image()
            vc.add_player(str(rez.players))
            vc.add_guess_game(str(rez.guesses))
            vc.add_jackpot(str(rez.jackpot))
            vc.add_reference("????")
            vc.add_game_id(str(rez.gameId))
            vc.add_node_ip(get_ip())
            vc.add_refresh_time(now.strftime("%b %d  %H:%M"))
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

