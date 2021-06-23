import time

import cbpro
import matplotlib.pyplot as plt
import pandas as pd
import graphics  # personal module
import display
from datetime import datetime, timedelta

public_client = cbpro.PublicClient()

# TODO: main.py still needs to be formatted for actual use, everything is for testing at the moment

# ----------------------------------------------------------------------------------------


def create_dataframes():  # TODO: update to be more flexible, perhaps pass in a list of coin names
    """Make a line graph of time vs. high in 15 minute granularity"""
    global btc_df, eth_df, ltc_df, ren_df

    btc_historic_rates = public_client.get_product_historic_rates('BTC-USD', granularity=900)
    btc_df = pd.DataFrame(btc_historic_rates, columns=['date', 'low', 'high', 'open', 'close', 'volume'])
    btc_df['date'] = pd.to_datetime(btc_df['date'], unit='s')
    print(btc_df)  # print all data

    eth_historic_rates = public_client.get_product_historic_rates('ETH-USD', granularity=900)
    eth_df = pd.DataFrame(eth_historic_rates, columns=['date', 'low', 'high', 'open', 'close', 'volume'])
    eth_df['date'] = pd.to_datetime(eth_df['date'], unit='s')
    print(eth_df)  # print all data

    ltc_historic_rates = public_client.get_product_historic_rates('LTC-USD', granularity=900)
    ltc_df = pd.DataFrame(ltc_historic_rates, columns=['date', 'low', 'high', 'open', 'close', 'volume'])
    ltc_df['date'] = pd.to_datetime(ltc_df['date'], unit='s')
    print(ltc_df)  # print all data

    ren_historic_rates = public_client.get_product_historic_rates('REN-USD', granularity=900)
    ren_df = pd.DataFrame(ren_historic_rates, columns=['date', 'low', 'high', 'open', 'close', 'volume'])
    ren_df['date'] = pd.to_datetime(ren_df['date'], unit='s')
    print(ren_df)  # print all data
# ----------------------------------------------------------------------------------------


"""create a new image"""


def generate_graph():  # TODO: remove getting prices here, also make function singular? pass in only one coin
    btc_price = public_client.get_product_ticker(product_id='BTC-USD').get("price")
    eth_price = public_client.get_product_ticker(product_id='ETH-USD').get("price")
    ltc_price = public_client.get_product_ticker(product_id='LTC-USD').get("price")
    ren_price = public_client.get_product_ticker(product_id='REN-USD').get("price")

    graphics.GenerateImage("BTC-USD", btc_price, btc_df)
    graphics.GenerateImage("ETH-USD", eth_price, eth_df)
    graphics.GenerateImage("LTC-USD", ltc_price, ltc_df)
    graphics.GenerateImage("REN-USD", ren_price, ren_df)


def get_current_prices():  # TODO: make singular, basically don't do any of these things (i.e. globals, mult coins)
    global btc_price, eth_price, ltc_price, ren_price
    btc_price = public_client.get_product_ticker(product_id='BTC-USD').get("price")
    eth_price = public_client.get_product_ticker(product_id='ETH-USD').get("price")
    ltc_price = public_client.get_product_ticker(product_id='LTC-USD').get("price")
    ren_price = public_client.get_product_ticker(product_id='REN-USD').get("price")

# ----------------------------------------------------------------------------------------
"""Calculate P&L using previous day's close"""

# TODO: move to calculations/data file

# TODO: Mess with getting local time for more accurate p&l, get_product_24hr_stats doesn't take a start or end point
#       for time. Would need to use an additional historic_rates pull with time points, but that's extra overhead
#       that a pi zero really doesn't need. Update: having "incorrect" p&l is really annoying

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", now)
# yesterday = now - timedelta(hours=24)
# print("24hrs ago: =", yesterday)


def calculate_pl():  # TODO: make function singular?, i.e. pass in one coin to calculate and get a return
    btc_24hr = public_client.get_product_24hr_stats('BTC-USD')
    btc_last = btc_24hr.get('last')
    btc_last = float(btc_last)
    btc_pl = ((btc_last - float(btc_price)) / btc_last) * 100
    btc_pl = round(btc_pl, 2)
    print("BTC P&L:", btc_pl)

    eth_24hr = public_client.get_product_24hr_stats('ETH-USD')
    eth_last = eth_24hr.get('last')
    eth_last = float(eth_last)
    eth_pl = ((eth_last - float(eth_price)) / eth_last) * 100
    eth_pl = round(eth_pl, 2)
    print("ETH P&L:", eth_pl)

    ltc_24hr = public_client.get_product_24hr_stats('LTC-USD')
    ltc_last = ltc_24hr.get('last')
    ltc_last = float(ltc_last)
    ltc_pl = ((ltc_last - float(ltc_price)) / ltc_last) * 100
    ltc_pl = round(ltc_pl, 2)
    print("LTC P&L:", ltc_pl)

    ren_24hr = public_client.get_product_24hr_stats('REN-USD')
    ren_last = ren_24hr.get('last')
    ren_last = float(ren_last)
    ren_pl = ((ren_last - float(ren_price)) / ren_last) * 100
    ren_pl = round(ren_pl, 2)
    print("REN P&L:", ren_pl)

    coins = [("BTC", btc_price, btc_pl), ("ETH", eth_price, eth_pl), ("LTC", ltc_price, ltc_pl), ("REN", ren_price, ren_pl)]
    graphics.four_boxes_image(coins)  # TODO: don't do this here, set up a return


while True:
    # create_dataframes()
    get_current_prices()
    calculate_pl()
    # TODO: use calculate_pl to get a return of one coin, add that coin to a list so that we can pass it to 4 coins screen
    display.write_to_screen()
    time.sleep(300)  # TODO: needs to not be sleep, unless interrupts/threads for reading buttons can work in tandem
#                            with this so that it will still update every 5 minutes while also allowing
#                            the screen to be updated or other things
