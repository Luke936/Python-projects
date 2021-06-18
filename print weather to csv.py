# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:16:23 2019

@author: lukek
"""
import numpy as np
import pandas as pd
import bq_helper 
from google.cloud import bigquery
from bq_helper import BigQueryHelper
import os
credentials = GoogleCredentials.get_application_default()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:\\Users\\lukek\\Desktop\\SQL\\lschlab2weather-495aae5d3687.json'
os.chdir(r'C:\Users\lukek\Desktop\SQL\huge datasets')
GOOGLE_APPLICATION_CREDENTIALS= 'C:\\Users\\lukek\\Desktop\\SQL\\lschlab2weather-495aae5d3687.json'


# create a helper object for our bigquery dataset
bqh = bq_helper.BigQueryHelper(active_project= "bigquery-public-data", dataset_name= "noaa_gsod")

# build and run a series of queries to get annual temperatures for the US
# WARNING: each year takes 5+ mins to run and the resultant dataset is about 100MB!
weather= BigQueryHelper("bigquery-public-data","noaa_gsod")
weather.list_tables()




import time
start = time.time()
START_YEAR = 2017
END_YEAR = 2020
    
for year in range(START_YEAR, END_YEAR):
    query = "SELECT stn,year,mo,da,temp,dewp,slp,stp,visib,wdsp,mxpsd,gust,max,min,prcp,sndp,fog,rain_drizzle,snow_ice_pellets,hail,thunder,tornado_funnel_cloud FROM `bigquery-public-data.noaa_gsod.gsod{}`".format(year)
    df_wthr = bqh.query_to_pandas_safe(query, max_gb_scanned=5)
    filename = 'US_weather_{}.csv'.format(year)
    df_wthr.to_csv(filename, index = False)
    print ("Saved {}".format(filename))
    
print ('It took', time.time()-start, 'seconds.')
