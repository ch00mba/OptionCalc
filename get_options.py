# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import pandas_datareader.data as web
import numpy as np

FB = web.YahooOptions('FB')


for exp in FB.expiry_dates:
     print(exp.isoformat())
     
     
     
     
     
calls = FB.get_call_data()



import  pandas_datareader as pdr
aapl = Options('aapl')
calls = aapl.get_call_data() 

#-----

from yahoo_fin import options

nflx_dates = options.get_expiration_dates("tqqq")


#-----


chain = options.get_options_chain("tqqq")


chain["calls"]
 
chain["puts"]

list(chain["calls"].columns.values)

# pip install html5lib
#options.get_options_chain("nflx", "01/18/2022")


TQQQ220121C00005000

TQQQ220121C00275000



TQQQ220121P00005000
TQQQ220121P00270000


tqqq_dates_exp = options.get_expiration_dates("tqqq")


opt_data = options.get_options_chain("tqqq", tqqq_dates_exp[1])







