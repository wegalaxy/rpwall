#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
import os

from display.waveshare_epd import epd7in3f
from PIL import ImageFont, ImageDraw, Image

logging.basicConfig(level=logging.INFO)

epd = epd7in3f.EPD()
epd.init()


def load_leaderboard(kv: dict, bg_file, font_file):
    logging.info("Clearing Image")
    epd.Clear()
    font = ImageFont.truetype(font_file, 16)
    logging.info("Loading Image @ %s", bg_file)
    image = Image.open(bg_file)
    draw = ImageDraw.Draw(image)

    initial_y = 90
    for a, b in sorted(kv.items(), key=lambda x: x[1], reverse=True):
        logging.info("{}: {}".format(a, b))
        draw.text((190, initial_y), "{}: {}".format(a, b), font = font)
        initial_y = initial_y + 30
    logging.debug("Loading Image Buffer")
    buff = epd.getbuffer(image)
    logging.debug("Loading Image to Display")
    epd.display(buff)
