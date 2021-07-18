import time
import cbpro
import threading
import graphics
# import display
import data

coins_to_use = ['BTC-USD', 'ETH-USD', 'LTC-USD', 'REN-USD']


def update_data():
    coins = []
    for coin in coins_to_use:
        current = data.get_current_price(coin)
        pc = data.calculate_24hr_percent_change(coin, current)
        df = data.create_dataframe(coin, 900)
        graphics.PriceGraph(coin, current, df, pc)
        coins.append((coin, current, pc))

    graphics.four_boxes_image(coins)


update_thread = threading.Timer(300, update_data)
update_thread.start()

# TODO: needs to not be sleep, unless interrupts/threads for reading buttons can work in tandem
#       with this so that it will still update every 5 minutes while also allowing
#       the screen to be updated or other things

# TODO: have the main while loop have the button control and then put threads/interrupts inside for data updates?
