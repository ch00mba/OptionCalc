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

nflx_dates = options.get_expiration_dates("nflx")


#-----



chain = options.get_options_chain("nflx")


chain["calls"]
 
chain["puts"]

list(chain["calls"].columns.values)

# pip install html5lib
options.get_options_chain("nflx", "01/18/2022")
