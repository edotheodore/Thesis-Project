# -*- coding: utf-8 -*-
"""

@author: Theodore
"""

import numpy as np

# get data from worldtradingdata
def stock_url(function, symbol, from_date):
    API_KEY = "YFl1bfK9zAddFzcsOgenstMkFg3Vl84lb6rtf80vAbQ2yj1ldqM4lv75cE5q"
    url = (f"https://api.worldtradingdata.com/api/v1/{function}?"
            f"symbol={symbol}"
            f"&date_from={from_date}"
            "&sort=newest"
            f"&api_token={API_KEY}")
    return url


def get_mape(y_true, y_pred): 
    """
    Compute mean absolute percentage error (MAPE)
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100