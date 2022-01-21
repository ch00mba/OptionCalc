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


dataFrame = pd.read_sql("select * from \"ss_dataframe_final\"", dbConnection);

pd.set_option('display.expand_frame_repr', False);


# get rows containing "C"
# get row containg "P"
# match them by timestamp 
# get p/c volume
# get p/c open interest 
# put results to db


# Print the DataFrame

print(dataFrame)

 

# Close the database connection

dbConnection.close()



chain["calls"]
 
chain["puts"]

list(chain["calls"].columns.values)