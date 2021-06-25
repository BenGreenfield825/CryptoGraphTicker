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


def create_dataframe(coin_name, gran_time):
    """coin_name should be a USD formatted coin as a string literal, i.e. 'BTC-USD'
        gran_time should be one of these: 60, 300, 900, 3600, 21600, 86400
        returns a formatted dataframe"""
    historic_rates = public_client.get_product_historic_rates(coin_name, granularity=gran_time)
    df = pd.DataFrame(historic_rates, columns=['date', 'low', 'high', 'open', 'close', 'volume'])
    df['date'] = pd.to_datetime(df['date'], unit='s')
    print(df)  # print all data
    return df


# ----------------------------------------------------------------------------------------


"""create a new image"""


# def generate_graph():  # TODO: remove this function and just call GenerateGraph from display when needed
#     b_price = public_client.get_product_ticker(product_id='BTC-USD').get("price")
#     e_price = public_client.get_product_ticker(product_id='ETH-USD').get("price")
#     l_price = public_client.get_product_ticker(product_id='LTC-USD').get("price")
#     r_price = public_client.get_product_ticker(product_id='REN-USD').get("price")
#
#     graphics.GenerateGraph("BTC-USD", b_price, btc_df)
#     graphics.GenerateGraph("ETH-USD", e_price, eth_df)
#     graphics.GenerateGraph("LTC-USD", l_price, ltc_df)
#     graphics.GenerateGraph("REN-USD", r_price, ren_df)


def get_current_price(coin_name):
    """coin_name should be a USD formatted coin as a string literal, i.e. 'BTC-USD'"""
    current_price = public_client.get_product_ticker(product_id=coin_name).get("price")
    return current_price

# ----------------------------------------------------------------------------------------


"""Calculate P&L using previous day's close"""

# TODO: move to calculations/data file

# TODO: Mess with getting local time for more accurate p&l, get_product_24hr_stats doesn't take a start or end point
#       for time. Would need to use an additional historic_rates pull with time points, but that's extra overhead
#       that a pi zero really doesn't need. Update: having "incorrect" p&l is really annoying

# after some research, crypto 24hr% change is based on 24hrs ago compared to current time, so doing this below
# would probably make it the most accurate, given we match everything correctly to the data frames
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", now)
# yesterday = now - timedelta(hours=24)
# print("24hrs ago: =", yesterday)
# otherwise we could look at 00:00:00 time (start of day) and compare to current price
# In the end, the way I have it might be fine as it seems that different sites use different methods anyways


def calculate_percent_change(coin_name, current_price):
    """coin_name should be a USD formatted coin as a string literal, i.e. 'BTC-USD'"""
    coin_24hr = public_client.get_product_24hr_stats(coin_name)
    close = float(coin_24hr.get('last'))
    percent_change = ((float(current_price) - close) / close) * 100
    percent_change = round(percent_change, 2)
    print(coin_name + " percent change:", percent_change)
    return percent_change


# ----------------------------------------------------------------------------------------


coins_to_use = ['BTC-USD', 'ETH-USD', 'LTC-USD', 'REN-USD']
while True:
    coins = []
    for coin in coins_to_use:
        current = get_current_price(coin)
        pc = calculate_percent_change(coin, current)
        # df = create_dataframe(coin, 900)
        coins.append((coin, current, pc))

    graphics.four_boxes_image(coins)
    display.write_to_screen()
    time.sleep(300)  # TODO: needs to not be sleep, unless interrupts/threads for reading buttons can work in tandem
#                            with this so that it will still update every 5 minutes while also allowing
#                            the screen to be updated or other things
