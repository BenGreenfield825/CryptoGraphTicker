import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789
import adafruit_rgb_display.hx8357 as hx8357
import adafruit_rgb_display.st7735 as st7735
import adafruit_rgb_display.ssd1351 as ssd1351
import adafruit_rgb_display.ssd1331 as ssd1331
from matplotlib import pyplot as plt

""" This module will handle creating graphics and controlling the display """

SCREEN_SIZE = (320, 240)  # change pixel size of screen here


class GenerateImage:
    def __init__(self, coin_name, coin_price, coin_df):
        self.coin_name = coin_name
        self.coin_price = coin_price
        self.coin_df = coin_df
        self.formatted_graph = self.format_graph()

        self.make_image()

    def format_graph(self):
        ax = self.coin_df.plot(x='date', y='high', legend=False)  # turn off legend
        # ax.set_facecolor('black')
        plt.axis('off')  # remove axes
        # plt.show()
        ax.figure.savefig('temp_graph.png', transparent=True)  # save graph with a transparent background
        graph = Image.open(r"temp_graph.png")
        graph = graph.resize((240, 240))
        graph.save("resized.png")
        return graph

    def make_image(self):
        img = Image.new('RGB', SCREEN_SIZE, 0)  # make a new black canvas of 320x240 (screen size)
        # img.show()
        img2 = Image.new('RGB', (80, 240), 'blue')  # placeholder box for info
        img.paste(img2, (0, 0))
        img.paste(self.formatted_graph, (80, 0))
        # img.show()
        img.save(self.coin_name + "_screen" + ".png")
