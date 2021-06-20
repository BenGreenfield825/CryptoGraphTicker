import cbpro
import matplotlib.pyplot as plt
import pandas as pd
import graphics  # personal module
from datetime import datetime, timedelta

public_client = cbpro.PublicClient()

# TODO: main.py still needs to be formatted for actual use, everything is for testing at the moment

# ----------------------------------------------------------------------------------------
"""Make a line graph of time vs. high in 15 minute granularity"""
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
btc_price = public_client.get_product_ticker(product_id='BTC-USD').get("price")
graphics.GenerateImage("BTC-USD", btc_price, btc_df)
eth_price = public_client.get_product_ticker(product_id='ETH-USD').get("price")
graphics.GenerateImage("ETH-USD", eth_price, eth_df)
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
graphics.four_boxes_image(coins)
