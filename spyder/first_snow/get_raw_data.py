#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 22:58:23 2017

@author: mh70
"""

import sqlite3
from sqlite3 import Error
import platform
import pandas as pd

def get_db_fname():
    db_file_name = "History"
    if platform.system() == 'Linux':
        db_path = r"/home/mh/.config/google-chrome/Default"
        db_file = db_path + '/' + db_file_name
    else:    
        db_path = r"C:\Users\m.houska\AppData\Local\Google\Chrome\User Data\Default"
        db_file = db_path + '\\' + db_file_name
    return db_file

def create_connection(db_file):
    """ create a database connection to the SQLite db specified by the db_file
    :param db_file: database file
    :return: Connection object or None    
    """
    
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return None


def get_data_from_db(db_file):
    
        
    # create a database connection        
    conn = create_connection(db_file)
    with conn:
                
        # visit_time + last_visit_time
        # number of microseconds since midnight UTC of 1 January 1601
        #        
        # time shift 
        # dt_1601 = datetime(1601, 1, 1, 0, 0, 0, 0)
        # dt_1970 = datetime(1970, 1, 1, 0, 0, 0, 0)
        # (dt_1970 - dt_1601).total_seconds()  ->  11644473600.0

        
        sql_urls = """select id, url,
        datetime(last_visit_time/1000000-11644473600,'unixepoch'),         
        visit_count 
        from  urls 
        order by last_visit_time desc;
        """
        
        sql_visits = """select 
        datetime(visit_time/1000000-11644473600,'unixepoch'), url, transition  
        from visits
        order by visit_time desc;
        """
        cur = conn.cursor()
        
        cur.execute(sql_urls)
        rows_urls = cur.fetchall() #raw sql data
        
        cur.execute(sql_visits)
        rows_visits = cur.fetchall() #raw sql data
        
        
    return (rows_urls, rows_visits)



def main():
    
    #read from db , close chrome first
    raw_urls, raw_visits  = get_data_from_db(get_db_fname()) 
    
    #read into pandas DF
    df_visits = pd.DataFrame(raw_visits,
                             columns=['datetime', 'url_fk', 'transition'])
    df_urls = pd.DataFrame(raw_urls,
                           columns=['id', 'url', 'datetime', 'visitcount'])
    
    
    #convert the datetime string column into a column of Pandas datetime elements
    # Since pandas represents timestamps in nanosecond resolution, 
    # the timespan that can be represented using a 64-bit integer is limited 
    # to approximately 584 years 
    # '1677-09-22 00:12:43.145225' to '2262-04-11 23:47:16.854775807'
    # see pd.Timestamp.min ; pd.Timestamp.max
    # errors='coerce' create NaT for invalid values
    
    df_urls.datetime = pd.to_datetime(df_urls.datetime, errors='coerce')
    df_visits.datetime = pd.to_datetime(df_visits.datetime, errors='coerce')

    df_visits['trans_type'] = df_visits['transition'].apply(lambda t: t & 0xff)
    # https://groups.google.com/a/chromium.org/forum/#!topic/chromium-discuss/r7UQ2i98Lu4
    # https://developer.chrome.com/extensions/history

    return (df_visits, df_urls)



"""
dt_1677 = datetime(1677, 9, 22, 0, 12, 43, 145225)
dt_1601 = datetime(1601, 1, 1, 0, 0, 0, 0)
dt_1970 = datetime(1970, 1, 1, 0, 0, 0, 0)
(dt_1970 - dt_1601).total_seconds()
"""

