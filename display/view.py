#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
from PIL.ImageFont import FreeTypeFont

from PIL import ImageFont, ImageDraw, Image

logging.basicConfig(level=logging.INFO)


class ViewController:
    _font32: FreeTypeFont
    _font16: FreeTypeFont
    _epd: any
    _image: Image
    _drawing: ImageDraw
    _bg_file: str

    def __init__(self,
                 bg_file: str,
                 font_file: str):
        self._bg_file = bg_file
        self._font32 = ImageFont.truetype(font_file, 32)
        self._font16 = ImageFont.truetype(font_file, 16)

        try:
            from display.waveshare_epd import epd7in3f
            self._epd = epd7in3f.EPD()
            self._epd.init()
        except RuntimeError as e:
            logging.warning("Error launching eink, skipping for now: {}".format(e))

    def clear_image(self):
        logging.info("Clearing Image")
        self._image = Image.open(self._bg_file)
        self._drawing = ImageDraw.Draw(self._image)
        try:
            if hasattr(self, '_epd'):
                self._epd.Clear()
        except RuntimeError as e:
            logging.warning("Error launching eink, skipping for now: {}".format(e))

    def load_image(self):
        logging.info("Loading Image")
        try:
            if hasattr(self, '_epd'):
                buff = self._epd.getbuffer(self._image)
                logging.debug("Loading Image to Display")
                self._epd.display(buff)
            else:
                self._image.show()
        except RuntimeError as e:
            logging.warning("Error launching eink, skipping for now: {}".format(e))
            self._image.show()

    def add_text_large(self, message, center_x, center_y):
        _, _, w, h = self._drawing.textbbox((0, 0), message, font=self._font32)
        self._drawing.text((center_x - w / 2, center_y - h / 2), message, font=self._font32, fill=(7, 138, 28, 255))

    def add_text(self, message, center_x, center_y):
        _, _, w, h = self._drawing.textbbox((0, 0), message, font=self._font16)
        self._drawing.text((center_x - w / 2, center_y - h / 2), message, font=self._font16, fill=(7, 138, 28, 255))

    def add_player(self, joined):
        self.add_text_large(joined, 117, 110)

    def add_guess_game(self, guesses):
        self.add_text_large(guesses, 305, 110)

    def add_jackpot(self, pool):
        self.add_text_large(pool, 493, 110)

    def add_reference(self, reference):
        self.add_text_large(reference, 683, 110)

    def add_game_id(self, gameId):
        self.add_text(gameId, 683, 260)

    def add_node_ip(self, nodeIp):
        self.add_text(nodeIp, 683, 350)

    def add_refresh_time(self, refreshTime):
        self.add_text(refreshTime, 683, 436)
