#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 18:28:45 2022

@author: choomba
"""

from datetime import datetime
import psycopg2
import pandas as pd
from sqlalchemy import create_engine


ts = int(time.time())

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


alchemyEngine  = create_engine('postgresql+psycopg2://postgres:example@172.17.0.1:5432/mydb', pool_recycle=3600);

dbConnection = alchemyEngine.connect();


#dataFrame = pd.read_sql("select * from \"Contract Name\"", dbConnection);

dataFrame = pd.read_sql("select \"Contract Name\" from \"all_options\"", dbConnection);


tickers = dataFrame.drop_duplicates()

tickers["Contract Name"][1]

# find expiration 

singleString = tickers["Contract Name"][1]


import re

pattern = "TQQQ(.*?)C"

substring = re.search(pattern, singleString).group(1)
print(substring)



s = '12345678'

t = iter(substring)
date1 = '-'.join(a+b for a,b in zip(t, t))
date2 = "20" + date1


import datetime

input = date2
  

format = '%Y-%m-%d'
  

datetime = datetime.datetime.strptime(input, format)
  

print(datetime.date())



# TQQQ220121C00006250


# TQQQ240119P00245000

pd.set_option('display.expand_frame_repr', False);


# get rows containing "C"
# get row containg "P"
# match them by timestamp 
# get p/c volume
# get p/c open interest 
# put results to db


#select * from "all_options" where "Contract Name" like '%C%'

#select "Contract Name" from "all_options";


# Print the DataFrame

print(dataFrame)

 

# Close the database connection

dbConnection.close()



chain["calls"]
 
chain["puts"]

list(chain["calls"].columns.values)