#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:02:52 2021

@author: alexei
"""

import psycopg2

import pandas as pds

from sqlalchemy import create_engine


alchemyEngine  = create_engine('postgresql+psycopg2://postgres:example@172.17.0.1:5432/mydb', pool_recycle=3600);

dbConnection = alchemyEngine.connect();


dataFrame = pds.read_sql("select * from \"ss_dataframe_final\"", dbConnection);

pds.set_option('display.expand_frame_repr', False);

# Print the DataFrame

print(dataFrame)

 

# Close the database connection

dbConnection.close()