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


#ts = int(time.time())

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
#print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


alchemyEngine  = create_engine('postgresql+psycopg2://postgres:example@172.17.0.1:5432/mydb', pool_recycle=3600);

dbConnection = alchemyEngine.connect();


#dataFrame = pd.read_sql("select * from \"Contract Name\"", dbConnection);



#--select * from all_options_test where exp_date >= now();



#dataFrame = pd.read_sql("select \"Contract Name\" from \"all_options\"", dbConnection);

df_calls = pd.read_sql("select * from all_options where exp_date >= now() and calls = 1", dbConnection);
df_puts = pd.read_sql("select * from all_options where exp_date >= now() and calls = 0", dbConnection);

oi_calls = df_calls["Open Interest"]
oi_puts = df_puts["Open Interest"]

# select * from all_options where exp_date >= now() and calls = 1;


tickers = dataFrame.drop_duplicates()


# total put/call ratio OI














TQQQ240119P00245000

import re

with open('textfile.txt') as f:
    a = f.readlines()
    pattern = r'psnr_y:([\d.]+)'
    for line in a:
        print(re.search(pattern, line)[1])
        
        
              
psnr_y = TQQQ




tickers["Contract Name"][1]

# find expiration 

singleString = tickers["Contract Name"][1]


import re

pattern = "TQQQ(.*?)C"

substring = re.search(pattern, singleString).group(1)
print(substring)

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




        
        singleString = df["Contract Name"][1]

        pattern = "TQQQ(.*?)P"

        substring = re.search(pattern, singleString).group(1)
       
        print(substring)

        t = iter(substring)
        date1 = '-'.join(a+b for a,b in zip(t, t))
        date2 = "20" + date1

        #input = date2
          

        #format = '%Y-%m-%d'
          

        #datetime1 = datetime.datetime.strptime(input, format)
        
        datetime1 = datetime.datetime.strptime(tqqq_dates_exp[1], '%B %d, %Y')
        
        