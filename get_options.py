# -*- coding: utf-8 -*-



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
    
        df = pd.DataFrame(opt_data['calls'], columns=opt_data['calls'].keys())
        df = df.replace('-', 0.00)
        df['snapshot_time'] = timestamp # unix time
        df.to_sql(val, statsEngine, if_exists='append', index=False)
        df.to_sql("all_options", statsEngine, if_exists='append', index=False)

    
        df = pd.DataFrame(opt_data['puts'], columns=opt_data['puts'].keys())
        df = df.replace('-', 0.00)
        df['snapshot_time'] = timestamp # unix time
        df.to_sql(val, statsEngine, if_exists='append', index=False)
        df.to_sql("all_options", statsEngine, if_exists='append', index=False)

    postgreSQLConnection.close()
    time.sleep(900)


#TODO

# create one big table for everyting 

# create table for each expiation puts and calls separately

# convurent version https://stackoverflow.com/questions/20170251/how-to-run-a-script-forever