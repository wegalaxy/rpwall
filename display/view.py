#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
from PIL.ImageFont import FreeTypeFont

from PIL import ImageFont, ImageDraw, Image

logging.basicConfig(level=logging.INFO)


class ViewController:
    _font40: FreeTypeFont
    _font26: FreeTypeFont
    _font16: FreeTypeFont
    _font12: FreeTypeFont
    _epd: any
    _image: Image
    _drawing: ImageDraw
    _bg_file: str

    def __init__(self,
                 bg_file: str,
                 font_file: str):
        self._bg_file = bg_file
        self._font26 = ImageFont.truetype(font_file, 26)
        self._font40 = ImageFont.truetype(font_file, 40)
        self._font16 = ImageFont.truetype(font_file, 16)
        self._font12 = ImageFont.truetype(font_file, 12)

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
                self._image.convert('RGB').show()
        except RuntimeError as e:
            logging.warning("Error launching eink, skipping for now: {}".format(e))
            self._image.show()

    def add_text_xlarge(self, message, center_x, center_y):
        _, _, w, h = self._drawing.textbbox((0, 0), message, font=self._font40)
        self._drawing.text((center_x - w / 2, center_y - h / 2), message, font=self._font40, fill=(7, 138, 28, 255))

    def add_text_large(self, message, center_x, center_y):
        _, _, w, h = self._drawing.textbbox((0, 0), message, font=self._font26)
        self._drawing.text((center_x - w / 2, center_y - h / 2), message, font=self._font26, fill=(7, 138, 28, 255))

    def add_text(self, message, center_x, center_y):
        _, _, w, h = self._drawing.textbbox((0, 0), message, font=self._font16)
        self._drawing.text((center_x - w / 2, center_y - h / 2), message, font=self._font16, fill=(7, 138, 28, 255))

    def add_text_small(self, message, center_x, center_y):
        _, _, w, h = self._drawing.textbbox((0, 0), message, font=self._font12)
        self._drawing.text((center_x - w / 2, center_y - h / 2), message, font=self._font12, fill=(7, 138, 28, 255))

    def add_player(self, joined):
        self.add_text_xlarge(joined, 100, 145)

    def add_player_last(self, joined):
        self.add_text_small(joined, 100, 210)

    def add_guess_game(self, guesses):
        self.add_text_xlarge(guesses, 300, 145)

    def add_guess_game_last(self, guesses):
        self.add_text_small(guesses, 300, 210)

    def add_jackpot(self, pool):
        self.add_text_xlarge(pool, 500, 145)

    def add_jackpot_last(self, pool):
        self.add_text_small(pool, 500, 210)

    def add_reference(self, reference):
        self.add_text_large(reference, 700, 145)

    def add_reference_last(self, reference):
        self.add_text_small(reference, 700, 210)

    def add_bottom(self, text):
        self.add_text_small(text, 400, 470)
