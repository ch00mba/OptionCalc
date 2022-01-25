# -*- coding: utf-8 -*-

import re

import datetime
from yahoo_fin import options
from sqlalchemy import create_engine
import pandas as pd
import time
from yahoo_fin import stock_info



# snapshot metrics to collect 

# PC ratio oi and vol 

# max pain oi and vol 

# valuate bull spread call 5 10 30 $ move and bull put spread

# volatility smile 

# compare to spot performace 





# get spot price 



# execution timer

d = datetime.datetime.strptime('15:30','%H:%M')

dnow = datetime.datetime.now()

dnow.time() < d.time()



# days to expiration 
dte = datetime1 - datetime.datetime.now()
dte1 = int(dte.days)



#while True:
    
    
statsEngine = create_engine('postgresql+psycopg2://postgres:example@172.17.0.1:5432/mydb')
postgreSQLConnection = statsEngine.raw_connection()

tqqq_dates_exp = options.get_expiration_dates("tqqq")

tqqq_spot = stock_info.get_live_price("tqqq") # get spot price 



for i, val in enumerate(tqqq_dates_exp):
    
    timestamp = int(time.time())
    datetime1 = datetime.datetime.strptime(tqqq_dates_exp[i], '%B %d, %Y')


    df_spot = [[timestamp, tqqq_spot]]
    df_spot1 = pd.DataFrame (df_spot, columns = ['timestamp','tqqq_spot'], )


    opt_data = options.get_options_chain("tqqq", tqqq_dates_exp[i])
    
    df_calls = pd.DataFrame(opt_data['calls'], columns=opt_data['calls'].keys())
    df_calls = df_calls.replace('-', 0)
    df_calls['snapshot_time'] = timestamp # unix time
    df_calls['calls'] = 1
    df_calls['exp_date'] = datetime1
    df_calls['exp_date_unix'] = int(datetime1.date().strftime("%s"))
    
    d1c = df_calls['Implied Volatility'].str.replace('%','').astype(float)
    
    df_calls['IV'] = d1c
    
    df_calls.drop('Implied Volatility', axis =1, inplace = True)
        



    df_puts = pd.DataFrame(opt_data['puts'], columns=opt_data['puts'].keys())
    df_puts = df_puts.replace('-', 0)
    df_puts['snapshot_time'] = timestamp # unix time
    df_puts['calls'] = 0
    df_puts['exp_date'] = datetime1
    df_puts['exp_date_unix'] = int(datetime1.date().strftime("%s"))
    
    d1p = df_puts['Implied Volatility'].str.replace('%','').astype(float)
    
    df_puts['IV'] = d1p
    
    df_puts.drop('Implied Volatility', axis =1, inplace = True)



    #    metrics 
    # PC ratio oi and vol 
    
    df_calls["Open Interest"] = df_calls["Open Interest"].astype(int)
    df_puts["Open Interest"] = df_puts["Open Interest"].astype(int)
    
    df_calls["Volume"] = df_calls["Volume"].astype(int)
    df_puts["Volume"] = df_puts["Volume"].astype(int)
    

        
    df_puts.to_sql(val, statsEngine, if_exists='append', index=False)
    df_puts.to_sql("all_options", statsEngine, if_exists='append', index=False)
    
    
    df_calls.to_sql(val, statsEngine, if_exists='append', index=False)
    df_calls.to_sql("all_options", statsEngine, if_exists='append', index=False)
    

    # PC ratio OI
    

    put_call_r_oi = df_puts["Open Interest"].sum()/df_calls["Open Interest"].sum() # might need to add strike filter 

    put_call_r_oi = [[timestamp, datetime1 ,put_call_r_oi]]
    
    df_pcoi = pd.DataFrame (put_call_r_oi, columns = ['timestamp', 'expiration','put_call_ratio_oi'], )
  
    df_pcoi.to_sql('PC_OI', statsEngine, if_exists='append', index=False)

    # PC ratio VOL

    put_call_r_vol = df_puts["Volume"].sum()/df_calls["Volume"].sum() # might need to add strike filter 

    put_call_r_vol = [[timestamp, datetime1 ,put_call_r_vol]]
        
    df_pcvol = pd.DataFrame (put_call_r_oi, columns = ['timestamp', 'expiration','put_call_ratio_vol'], )

    df_pcvol.to_sql('PC_VOL', statsEngine, if_exists='append', index=False)
    
    





postgreSQLConnection.close()  



      
 # df = pd.DataFrame (put_call_r, columns = ['timestamp','put_call_ratio'], )
  #    print (df)





# max pain oi and vol 

# valuate bull spread call 5 10 30 $ move and bull put spread

# volatility smile 

# compare to spot performace 





#    time.sleep(900)



# convurent version https://stackoverflow.com/questions/20170251/how-to-run-a-script-forever