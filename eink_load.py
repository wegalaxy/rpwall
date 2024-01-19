#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

import logging
from waveshare_epd import epd7in3f
import time
from PIL import Image
import traceback

logging.basicConfig(level=logging.DEBUG)

epd = epd7in3f.EPD()


def load_image(imagePath):
    logging.debug("Clearing Image")
    epd.Clear()
    logging.info("Loading Image @ %s", imagePath)
    image = Image.open(imagePath)
    logging.debug("Loading Image Buffer")
    buff = epd.getbuffer(image)
    logging.debug("Loading Image to Display")
    epd.display(buff)

