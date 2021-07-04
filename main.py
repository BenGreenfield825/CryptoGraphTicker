import time
import cbpro
import graphics
# import display
import data

coins_to_use = ['BTC-USD', 'ETH-USD', 'LTC-USD', 'REN-USD']
while True:
    coins = []
    for coin in coins_to_use:
        current = data.get_current_price(coin)
        pc = data.calculate_24hr_percent_change(coin, current)
        # df = data.create_dataframe(coin, 900)
        coins.append((coin, current, pc))

    graphics.four_boxes_image(coins)
    # display.write_to_screen()
    time.sleep(300)
# TODO: needs to not be sleep, unless interrupts/threads for reading buttons can work in tandem
#       with this so that it will still update every 5 minutes while also allowing
#       the screen to be updated or other things
