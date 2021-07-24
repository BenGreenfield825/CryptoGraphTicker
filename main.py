import time
import cbpro
import threading
import linkedList
# import display
import graphics
# import display
import data
# import buttonTesting

coins_to_use = ['BTC-USD', 'ETH-USD', 'LTC-USD', 'REN-USD']


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
        # display.write_to_screen(current_display)
        # TODO: Need a system of knowing what is currently on the screen so we can call write_to_screen to update ^
        #       Perhaps a class for handling all of this
        time.sleep(300)


update_thread = threading.Thread(target=update_data)
update_thread.start()
# while True:  # button logic goes here
#     buttonTesting.button_control()

# TODO: matplotlib does not like to be run on secondary threads on the pi, but only makes errors sometimes...

# TODO: If linked list doesn't work, just try a normal list like ["image1", "image2", etc ] and a button input
#       would add or subtract the index we are on - this list will most likely only ever be 5 images long,
#       so checking for out of bounds or wraparound should be easy enough

