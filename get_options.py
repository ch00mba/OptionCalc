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
        datetime1 = datetime.datetime.strptime(tqqq_dates_exp[i], '%B %d, %Y')

        opt_data = options.get_options_chain("tqqq", tqqq_dates_exp[i])
    
        df_calls = pd.DataFrame(opt_data['calls'], columns=opt_data['calls'].keys())
        df_calls = df_calls.replace('-', 0)
        df_calls['snapshot_time'] = timestamp # unix time
        df_calls['calls'] = 1
        df_calls['exp_date'] = datetime1
        df_calls['exp_date_unix'] = int(datetime1.date().strftime("%s"))
        
        df_calls.to_sql(val, statsEngine, if_exists='append', index=False)
        df_calls.to_sql("all_options", statsEngine, if_exists='append', index=False)


        put_call_r = [[timestamp, 100]]
        
        df = pd.DataFrame (put_call_r, columns = ['timestamp','put_call_ratio'], )
        print (df)


        df_puts = pd.DataFrame(opt_data['puts'], columns=opt_data['puts'].keys())
        df_puts = df_puts.replace('-', 0)
        df_puts['snapshot_time'] = timestamp # unix time
        df_puts['calls'] = 0
        df_puts['exp_date'] = datetime1
        df_puts['exp_date_unix'] = int(datetime1.date().strftime("%s"))        
        

        df_puts.to_sql(val, statsEngine, if_exists='append', index=False)
        df_puts.to_sql("all_options", statsEngine, if_exists='append', index=False)

    postgreSQLConnection.close()
    time.sleep(900)



# convurent version https://stackoverflow.com/questions/20170251/how-to-run-a-script-forever