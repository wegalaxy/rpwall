#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
from display.waveshare_epd import epd7in3f
from PIL import Image

logging.basicConfig(level=logging.INFO)

epd = epd7in3f.EPD()
epd.init()


def load_image(imagePath):
    logging.debug("Clearing Image")
    epd.Clear()
    logging.info("Loading Image @ %s", imagePath)
    image = Image.open(imagePath)
    logging.debug("Loading Image Buffer")
    buff = epd.getbuffer(image)
    logging.debug("Loading Image to Display")
    epd.display(buff)

