import cbpro
import matplotlib.pyplot as plt
import pandas as pd
import graphics  # personal module

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
# ----------------------------------------------------------------------------------------
"""create a new image"""
btc_price = public_client.get_product_ticker(product_id='BTC-USD').get("price")
graphics.GenerateImage("BTC-USD", btc_price, btc_df)
eth_price = public_client.get_product_ticker(product_id='ETH-USD').get("price")
graphics.GenerateImage("ETH-USD", eth_price, eth_df)

# ----------------------------------------------------------------------------------------
"""Calculate P&L using previous day's close"""
eth_24hr = public_client.get_product_24hr_stats('ETH-USD')
# print(eth_24hr)
eth_last = eth_24hr.get('last')
eth_current_high = eth_df['high'].loc[0]
# TODO: high based on current granularity, might want to do a separate poll for this section in case user sets
#       the granularity higher (edge case would be comparing 1-day to 1-day)

# print("Current high:", eth_current_high, "Close:", eth_last)
eth_last = float(eth_last)
eth_pl = ((eth_last - eth_current_high) / eth_last) * 100
# pl = '{0:.2f}'.format(pl)
eth_pl = round(eth_pl, 2)
print("ETH P&L:", eth_pl)

btc_24hr = public_client.get_product_24hr_stats('BTC-USD')
# print(btc_24hr)
btc_last = btc_24hr.get('last')
btc_current_high = btc_df['high'].loc[0]
# print("Current high:", btc_current_high, "Close:", btc_last)
btc_last = float(btc_last)
btc_pl = ((btc_last - btc_current_high) / btc_last) * 100
btc_pl = round(btc_pl, 2)
print("BTC P&L:", btc_pl)

coins = [("BTC", btc_price, btc_pl), ("ETH", eth_price, eth_pl)]
graphics.four_boxes_image(coins)
