import cbpro
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import mplfinance as mpf
from datetime import datetime
from PIL import Image

public_client = cbpro.PublicClient()
# print(public_client.get_currencies())
# print(public_client.get_product_trades(product_id='ETH-USD'))
print("Bitcoin Price:", public_client.get_product_ticker(product_id='BTC-USD').get("price"))
# print(public_client.get_product_24hr_stats('BTC-USD'))


# print(public_client.get_product_historic_rates('BTC-USD', granularity=21600))
# ----------------------------------------------------------------------------------------
"""Make a line graph of time vs. high in 15 minute granularity"""
historic_rates = public_client.get_product_historic_rates('BTC-USD', granularity=900)
df = pd.DataFrame(historic_rates, columns=['date', 'low', 'high', 'open', 'close', 'volume'])
df['date'] = pd.to_datetime(df['date'], unit='s')
print(df)  # print all data
# df.plot(x='date', y='high')
ax = df.plot(x='date', y='high', legend=False)  # turn off legend
# ax.set_facecolor('black')
plt.axis('off')  # remove axes
# plt.show()
ax.figure.savefig('test.png', transparent=True)  # save graph with a transparent background
im = Image.open(r"test.png")
im = im.resize((240, 240))
im.save("resized.png")
# print(df['date'])
# df.info()
# mpf.plot(df, type='candle')
# ----------------------------------------------------------------------------------------
"""create a new image"""
img = Image.new('RGB', (320, 240), 0)  # make a new black canvas of 320x240 (screen size)
img2 = Image.new('RGB', (80, 240), 'blue')  # placeholder box for info
img.paste(img2, (0, 0))
img.paste(im, (80, 0))
img.show()
# ----------------------------------------------------------------------------------------
# historic_rates = public_client.get_product_historic_rates('BTC-USD', granularity=900)
# dates = []
# counter = 0
# for data_point in historic_rates:
#     dates.append(data_point[0])
#     historic_rates[counter].pop(0)
#     counter += 1
# print(historic_rates)
# print(dates)
# reformatted = zip(dates, historic_rates)
# reformatted = list(reformatted)
# # reformatted = dict(reformatted)
# print(reformatted)
# dates = []
# data = []
# for data_point in historic_rates:
#     dates.append(data_point[0])
#     data.append(data_point[1])
#     data.append(data_point[2])
#     data.append(data_point[3])
#     data.append(data_point[4])
#     data.append(data_point[5])
# date_dict = {'date': dates}
# data_dict = {'data': data}
# print(date_dict)
# print(data_dict)
# df = pd.DataFrame(date_dict, data_dict)
# print(df)
# ----------------------------------------------------------------------------------------
# historic_rates = public_client.get_product_historic_rates('BTC-USD', granularity=900)
# print(historic_rates)
# for data in historic_rates:
#     temp = datetime.fromtimestamp(data[0]).strftime("%A, %B %d, %Y %I:%M:%S")
#     data[0] = temp
# df = pd.DataFrame(historic_rates, columns=['date', 'low', 'high', 'open', 'close', 'volume'])
# print(df)
# mpf.plot(df, type='candle')

# for data_point in historic_rates:
#     for data in data_point:
#         fig = go.Figure(data=[go.Candlestick(x=)])
# fig = go.Figure(data=[go.Candlestick(x=df[0],
#                 open=df[1],
#                 high=df[2],
#                 low=df[3],
#                 close=df[4])])
# fig.update_layout(xaxis_rangeslider_visible=False)
# fig.show()
# Parameters are optional
# wsClient = cbpro.WebsocketClient(url="wss://ws-feed.pro.coinbase.com",
#                                  products="REN-USD",
#                                  channels=["ticker"])
# wsClient.start()
# print(wsClient)
# # print(wsClient.products)
# # print(wsClient.products)
#
# wsClient.close()

