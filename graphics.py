from PIL import Image, ImageDraw, ImageFont
from matplotlib import pyplot as plt

""" This module will handle creating graphics and controlling the display """

SCREEN_SIZE = (320, 240)  # change pixel size of screen here
square_w = 152.5  # might change later

# TODO: Need a restructure overhaul for adaptability
# TODO: Graph screen needs design work - looks lame. Maybe info on a top banner and graph underneath
# TODO: Add automatic x offset for price in graph screen - make one from 4 coins into a function


class GenerateImage:
    def __init__(self, coin_name, coin_price, coin_df):
        self.coin_name = coin_name
        self.coin_price = coin_price
        self.coin_df = coin_df
        self.formatted_graph = self.format_graph()

        self.make_graph_text_image()

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

    def make_graph_text_image(self):
        name_fnt = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 20)
        price_fnt = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 22)
        pl_fnt = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 25)  # smaller font for p&l

        img = Image.new('RGB', SCREEN_SIZE, 0)  # make a new black canvas of 320x240 (screen size)
        img.paste(self.formatted_graph, (95, 0))
        img2 = Image.new('RGB', (110, 240), 'SteelBlue')  # placeholder box for info
        img.paste(img2, (0, 0))

        d = ImageDraw.Draw(img)
        d.text((15, 10), self.coin_name, font=name_fnt, fill="white")
        d.text((0, 40), "$" + self.coin_price, font=price_fnt, fill="white")

        img.save(self.coin_name + "_graph+text" + ".png")


def four_boxes_image(coins):  # pass in 4 prices and names to be displayed (list of tuples -> (coin_name, coin_price) )
    if len(coins) > 4:
        print("ERROR: Too many coin pairs! Only using the first four...")

    img = Image.new('RGB', SCREEN_SIZE, 0)
    d = ImageDraw.Draw(img)
    d.line((0, 0, 0, 240), fill="white", width=10)
    d.line((0, 0, 320, 0), fill="white", width=10)
    d.line((320, 0, 320, 240), fill="white", width=10)
    d.line((320, 240, 0, 240), fill="white", width=10)
    d.line((160, 0, 160, 240), fill="white", width=5)
    d.line((0, 120, 320, 120), fill="white", width=5)
    fnt = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 30)
    pl_fnt = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 25)  # smaller font for p&l

    for coin in coins:
        coin_name = coin[0]
        price = "$" + coin[1]
        if "." not in price:
            price = price + ".00"
        if coin[2] >= 0:
            pl = "+" + str(coin[2]) + "%"
            pl_color = "green"
        else:
            pl = str(coin[2]) + "%"
            pl_color = "red"

        # --- Draw the four coins --- #
        x_offset = 160
        y_offset = 120
        if coin == coins[0]:
            d.text((48, 10), coin_name, font=fnt, fill="white")  # coin name
            d.text((set_price_x(price), 45), price, font=fnt, fill="white")  # price
            d.text((40, 80), pl, font=pl_fnt, fill=pl_color)  # p&l
        if coin == coins[1]:
            d.text((48 + x_offset, 10), coin_name, font=fnt, fill="white")  # coin name
            d.text((set_price_x(price) + x_offset, 45), price, font=fnt, fill="white")  # price
            d.text((40 + x_offset, 80), pl, font=pl_fnt, fill=pl_color)  # p&l
        if coin == coins[2]:
            d.text((48, 10 + y_offset), coin_name, font=fnt, fill="white")  # coin name
            d.text((set_price_x(price), 45 + y_offset), price, font=fnt, fill="white")  # price
            d.text((40, 80 + y_offset), pl, font=pl_fnt, fill=pl_color)  # p&l
        if coin == coins[3]:
            d.text((48 + x_offset, 10 + y_offset), coin_name, font=fnt, fill="white")  # coin name
            d.text((set_price_x(price) + x_offset, 45 + y_offset), price, font=fnt, fill="white")  # price
            d.text((40 + x_offset, 80 + y_offset), pl, font=pl_fnt, fill=pl_color)  # p&l

    img.save("4coins.png")


def set_price_x(price):  # TODO: add this feature for p&l also
    length = len(price)
    if length == 9:
        x = 10
    elif length == 8:
        x = 16
    elif length == 7:
        x = 22
    elif length == 6:
        x = 28
    elif length == 5:
        x = 34
    elif length == 5:
        x = 48
    else:
        x = 10
    return x
