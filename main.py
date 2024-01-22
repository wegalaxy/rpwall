import eink_load
import sys
import os

picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'img')

def load_image():
    eink_load.load_image(os.path.join(picdir, '7in3f1.bmp'))


if __name__ == '__main__':
    load_image()

