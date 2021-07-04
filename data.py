import cbpro
import pandas as pd
# from datetime import datetime, timedelta

public_client = cbpro.PublicClient()

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

def get_current_price(coin_name):
    """coin_name should be a USD formatted coin as a string literal, i.e. 'BTC-USD'"""
    current_price = public_client.get_product_ticker(product_id=coin_name).get("price")
    return current_price

# ----------------------------------------------------------------------------------------

# TODO: add a "today's" percent change that starts at 00:00:00 as another option


def calculate_24hr_percent_change(coin_name, current_price):
    """coin_name should be a USD formatted coin as a string literal, i.e. 'BTC-USD'"""
    coin_24hr = public_client.get_product_24hr_stats(coin_name)
    open_24hr = float(coin_24hr.get('open'))
    percent_change = ((float(current_price) - open_24hr) / open_24hr) * 100
    percent_change = round(percent_change, 2)
    print(coin_name + " percent change:", percent_change)
    return percent_change


# ----------------------------------------------------------------------------------------
