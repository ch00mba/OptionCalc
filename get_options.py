# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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

"""


from yahoo_fin import options
from sqlalchemy import create_engine
import pandas as pd
import time




'''
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

'''

statsEngine = create_engine('postgresql+psycopg2://postgres:example@172.17.0.1:5432/mydb')

postgreSQLConnection = statsEngine.raw_connection()


tqqq_dates_exp = options.get_expiration_dates("tqqq")


#opt_data = options.get_options_chain("tqqq", tqqq_dates_exp[1])


for i, val in enumerate(tqqq_dates_exp):
    timestamp = int(time.time())
    #print(val)
    opt_data = options.get_options_chain("tqqq", tqqq_dates_exp[i])
    #print(opt_data)
    df = pd.DataFrame(opt_data['calls'], columns=opt_data['calls'].keys())
    
    df['snapshot_time'] = timestamp # unix time

    #print(df)
    
    df.to_sql(val, statsEngine, if_exists='append', index=False)
    
    df = pd.DataFrame(opt_data['puts'], columns=opt_data['puts'].keys())
    
    df['snapshot_time'] = timestamp # unix time
    
    df.to_sql(val, statsEngine, if_exists='append', index=False)


    
    #df.to_sql(val, engine)




#statsEngine = create_engine('postgresql+psycopg2://postgres:example@172.17.0.1:5432/mydb')

#postgreSQLConnection = statsEngine.raw_connection()

#df.to_sql(val, statsEngine)

postgreSQLConnection.close()




#TODO

# create one big table for everyting 

# create table for each expiation puts and calls separately

'''
try:
    
   # http://3.86.81.140
    statsEngine = create_engine('postgresql+psycopg2://postgres:example@172.17.0.1:5432/mydb')
    
    df.to_sql('table_name', statsEngine)

    
    postgreSQLConnection = statsEngine.raw_connection()
    cur = postgreSQLConnection.cursor()
    # create table one by one
    #for command in commands:
    cur.execute(commands)
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    postgreSQLConnection.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if postgreSQLConnection is not None:
        postgreSQLConnection.close()
'''