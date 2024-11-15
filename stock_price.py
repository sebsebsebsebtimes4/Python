import requests

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "H0BMOR4H4DXZYFD4"




def nvda_price():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "NVDA",
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]

    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"][0:7]
    a = (f"${yesterday_closing_price} is NVDA latest price")

    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"][0:7]
    b = (f"${day_before_yesterday_closing_price} is NVDA latest_day -1")

    yesterday_2_data = data_list[2]
    yesterday_2_price = yesterday_2_data["4. close"][0:7]
    c = (f"${yesterday_2_price} is NVDA latest_day -2")

    list_1 = [a, b, c]
    return (',\n'.join(list_1))




def aapl_price():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "AAPL",
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]

    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"][0:7]
    d = (f"${yesterday_closing_price} is AAPL latest price")

    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"][0:7]
    e = (f"${day_before_yesterday_closing_price} is AAPL latest_day -1")

    yesterday_2_data = data_list[2]
    yesterday_2_price = yesterday_2_data["4. close"][0:7]
    f = (f"${yesterday_2_price} is AAPL latest_day -2")

    list_2 = [d, e, f]
    return (',\n'.join(list_2))


def googl_price():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "googl",
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]

    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"][0:7]
    g = (f"${yesterday_closing_price} is GOOGL latest price")

    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"][0:7]
    h = (f"${day_before_yesterday_closing_price} is GOOGL latest_day -1")

    yesterday_2_data = data_list[2]
    yesterday_2_price = yesterday_2_data["4. close"][0:7]
    i = (f"${yesterday_2_price} is GOOGL latest_day -2")

    list_3 = [g, h, i]
    return (',\n'.join(list_3))

