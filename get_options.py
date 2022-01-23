# -*- coding: utf-8 -*-

import re

import datetime
from yahoo_fin import options
from sqlalchemy import create_engine
import pandas as pd
import time



while True:
    statsEngine = create_engine('postgresql+psycopg2://postgres:example@172.17.0.1:5432/mydb')
    postgreSQLConnection = statsEngine.raw_connection()
    tqqq_dates_exp = options.get_expiration_dates("tqqq")
        
    for i, val in enumerate(tqqq_dates_exp):
    
        timestamp = int(time.time())
        
        
        

        opt_data = options.get_options_chain("tqqq", tqqq_dates_exp[i])
    
        df_calls = pd.DataFrame(opt_data['calls'], columns=opt_data['calls'].keys())
        df_calls = df.replace('-', 0.00)
        df_calls['snapshot_time'] = timestamp # unix time
        df_calls['calls'] = 1
        df_calls['exp_date']
        df_calls['exp_date_unix']
        df_calls['strike']
        
        int(datetime1.date().strftime("%s"))
        
        
        df.to_sql(val, statsEngine, if_exists='append', index=False)
        df.to_sql("all_options", statsEngine, if_exists='append', index=False)

    




        df = pd.DataFrame(opt_data['puts'], columns=opt_data['puts'].keys())
        df = df.replace('-', 0.00)
        df['snapshot_time'] = timestamp # unix time
        
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
        
        
        
        
        
        tqqq_dates_exp[1]
          

        print(datetime1.date())
        
        df.to_sql(val, statsEngine, if_exists='append', index=False)
        df.to_sql("all_options", statsEngine, if_exists='append', index=False)

    postgreSQLConnection.close()
    time.sleep(900)


#TODO

# create one big table for everyting 

# create table for each expiation puts and calls separately

# convurent version https://stackoverflow.com/questions/20170251/how-to-run-a-script-forever