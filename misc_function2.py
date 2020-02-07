# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 18:48:21 2019

@author: Theodore
"""

# -*- coding: utf-8 -*-
"""

@author: Theodore
"""

import numpy as np
API_KEY = "WWLN1J8UJ2I7Q8ML"

# get data from worldtradingdata
def stock_url(function, symbol, outputsize): 
    url = (f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={outputsize}&apikey={API_KEY}")
    return url

def forex_url(function, symbol1, symbol2, outputsize):
    url = (f"https://www.alphavantage.co/query?function={function}&from_symbol={symbol1}&to_symbol={symbol2}&outputsize={outputsize}&apikey={API_KEY}")
    return url

def get_mape(y_true, y_pred): 
    """
    Compute mean absolute percentage error (MAPE)
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100