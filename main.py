import time
import cbpro
import threading
import graphics
# import display
import data
import buttonTesting

coins_to_use = ['BTC-USD', 'ETH-USD', 'LTC-USD', 'REN-USD']


# class test:
#     def __init__(self):
#         self.stopFlag = threading.Event()
#         self.update_thread = threading.Timer(300, self.update_data)
#         self.update_data()
#         self.update_thread.start()
#
#     def update_data(self):
#         coins = []
#         for coin in coins_to_use:
#             current = data.get_current_price(coin)
#             pc = data.calculate_24hr_percent_change(coin, current)
#             df = data.create_dataframe(coin, 900)
#             graphics.PriceGraph(coin, current, df, pc)
#             coins.append((coin, current, pc))
#
#         graphics.four_boxes_image(coins)
#         self.stopFlag.set()
#         self.update_thread.start()
def update_data():
    while True:
        coins = []
        for coin in coins_to_use:
            current = data.get_current_price(coin)
            pc = data.calculate_24hr_percent_change(coin, current)
            df = data.create_dataframe(coin, 900)
            graphics.PriceGraph(coin, current, df, pc)
            coins.append((coin, current, pc))

        graphics.four_boxes_image(coins)
        time.sleep(10)

# test()
# update_data()
# update_thread = threading.Timer(300, update_data)


update_thread = threading.Thread(target=update_data)
update_thread.start()
while True:  # button logic goes here
    buttonTesting.button_control()


