#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 23:34:57 2017

@author: mh70
"""
import fetch_data_form_db
import pandas as pd
from urllib.parse import urlparse

from datetime import datetime

raw_urls, raw_visits  = fetch_data_form_db.get_raw_data() #read from db , close chrome first

df_visits = pd.DataFrame(raw_visits, columns=['datetime', 'url_fk'])
df_urls = pd.DataFrame(raw_urls, columns=['datetime', 'url', 'visitcount'])

#convert the datetime string column into a column of Pandas datetime elements
# Since pandas represents timestamps in nanosecond resolution, 
# the timespan that can be represented using a 64-bit integer is limited 
# to approximately 584 years 
# '1677-09-22 00:12:43.145225' to '2262-04-11 23:47:16.854775807'
# see pd.Timestamp.min ; pd.Timestamp.max
# errors='coerce' create NaT for invalid values

df_visits.datetime = pd.to_datetime(df_visits.datetime, errors='coerce')
df_urls.datetime = pd.to_datetime(df_urls.datetime, errors='coerce')





"""
dt_1677 = datetime(1677, 9, 22, 0, 12, 43, 145225)
dt_1601 = datetime(1601, 1, 1, 0, 0, 0, 0)
dt_1970 = datetime(1970, 1, 1, 0, 0, 0, 0)
(dt_1970 - dt_1601).total_seconds()
"""