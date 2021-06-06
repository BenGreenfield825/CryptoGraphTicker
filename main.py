import cbpro
import matplotlib.pyplot as plt
import pandas as pd
import display  # personal module
from PIL import Image

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
display.GenerateImage("BTC-USD", btc_price, btc_df)
eth_price = public_client.get_product_ticker(product_id='ETH-USD').get("price")
display.GenerateImage("ETH-USD", eth_price, eth_df)
coins = [("BTC", btc_price), ("ETH", eth_price)]
display.four_boxes_image(coins)
# ----------------------------------------------------------------------------------------
