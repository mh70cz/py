#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:01:31 2017

@author: mh70

Compare duration of data load from SQL to Pnadas DF + convert datetime
1. datetime is converted on SQL level
2. datetime is converted in Pandas  ~3% faster
"""

import sqlite3
from sqlite3 import Error
import platform
import pandas as pd
import time


def get_db_name():
    db_file_name = "History"
    if platform.system() == 'Linux':
        db_path = r"/home/mh/.config/google-chrome/Default"
        database = db_path + '/' + db_file_name
    else:    
        db_path = r"C:\Users\m.houska\AppData\Local\Google\Chrome\User Data\Default"
        database = db_path + '\\' + db_file_name
    return database


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


def def_sql_commands(type):
    if type == 'date':
        sql_urls = """select 
        datetime(last_visit_time/1000000-11644473600,'unixepoch'),         
        url,  visit_count 
        from  urls 
        order by last_visit_time desc;
        """        
        sql_visits = """select 
        datetime(visit_time/1000000-11644473600,'unixepoch'), url  
        from visits
        order by visit_time desc;
        """
        
    elif type == 'seconds':
        sql_urls = """select 
        last_visit_time, url, visit_count 
        from  urls 
        order by last_visit_time desc;
        """        
        sql_visits = """select 
        visit_time, url  
        from visits
        order by visit_time desc;
        """        
    else:
        sql_urls, sql_visits = None, None
    
    return (sql_urls, sql_visits)

def get_raw_data(sql_urls, sql_visits):
            
    # create a database connection        
    conn = create_connection(db_name)
    with conn:
        
        cur = conn.cursor()
        
        cur.execute(sql_urls)
        rows_urls = cur.fetchall() 
        
        cur.execute(sql_visits)
        rows_visits = cur.fetchall() 
                
    return (rows_urls, rows_visits)


def read_from_db_date():
    raw_urls_date, raw_visits_date  = get_raw_data(*sql_commands)
    df_visits_d = pd.DataFrame(raw_visits_date, columns=['datetime', 'url_fk'])
    df_urls_d = pd.DataFrame(raw_urls_date, columns=['datetime', 'url', 'visitcount'])
    df_visits_d.datetime = pd.to_datetime(df_visits_d.datetime, errors='coerce')
    df_urls_d.datetime = pd.to_datetime(df_urls_d.datetime, errors='coerce')


def read_from_db_seconds():
    raw_urls_secs, raw_visits_secs  = get_raw_data(*sql_commands)
    
    
    df_visits_s = pd.DataFrame(raw_visits_secs, columns=['datetime', 'url_fk'])
    df_urls_s = pd.DataFrame(raw_urls_secs, columns=['datetime', 'url', 'visitcount'])
    
    # number of microseconds from midnight UTC of 1 January 1601 
    #                          to midnight UTC of 1 January 1970 
    #11644473600 * 1000 * 1000
    df_visits_s.datetime = (df_visits_s.datetime - 11644473600 * 1000_000) 
    df_urls_s.datetime = (df_urls_s.datetime - 11644473600 * 1000_000)
    
    df_visits_s.datetime = pd.to_datetime(df_visits_s.datetime, errors='coerce', unit='us')
    df_urls_s.datetime = pd.to_datetime(df_urls_s.datetime, errors='coerce', unit='us')


db_name = get_db_name()



sql_commands = def_sql_commands("date")
t0 = time.time()
for n in range(20):
    read_from_db_date()
elapsed_d = time.time() - t0


sql_commands = def_sql_commands("seconds")
t0 = time.time()
for n in range(20):    
    read_from_db_seconds()
elapsed_s = time.time() - t0 
