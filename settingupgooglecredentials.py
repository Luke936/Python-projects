# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import bq_helper 
from google.cloud import bigquery
from apiclient import discovery
import os
credentials = GoogleCredentials.get_application_default()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:\\Users\\lukek\\Desktop\\SQL\\lschlab2weather-495aae5d3687.json'




# create a helper object for our bigquery dataset
bqh = bq_helper.BigQueryHelper(active_project= "bigquery-public-data", dataset_name= "noaa_gsod")

# build and run a series of queries to get annual temperatures for the US
# WARNING: each year takes 5+ mins to run and the resultant dataset is about 100MB!

START_YEAR = 2009
END_YEAR = 2009

for year in range(START_YEAR, END_YEAR):
    query = "SELECT * FROM `bigquery-public-data.noaa_gsod.gsod{}`".format(year)

    df_wthr = bqh.query_to_pandas_safe(query, max_gb_scanned=5)
    filename = 'US_weather_{}.csv'.format(year)
    df_wthr.to_csv(filename, index = False)
    print ("Saved {}".format(filename))


GOOGLE_APPLICATION_CREDENTIALS= 'C:\\Users\\lukek\\Desktop\\SQL\\lschlab2weather-495aae5d3687.json'
