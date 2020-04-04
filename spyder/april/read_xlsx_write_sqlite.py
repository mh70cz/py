# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:34:40 2018; @author: mh70
"""
import pandas as pd
import sqlite3 
from sqlite3 import Error

f_name = r"C:\Users\m.houska\Downloads\KGZ_customercodes_all.xlsx"
s_name = "data"
t_name = "data" # table name in sql db
db_file = "my_sqlite3.db"

dfs = pd.read_excel(f_name, sheet_name=s_name)



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

def write_to_db():    
    conn = create_connection(db_file)
    dfs.to_sql(t_name , conn,  index=True, index_label=None)
    """
    if_exists : {‘fail’, ‘replace’, ‘append’}, default ‘fail’

        fail: If table exists, do nothing.
        replace: If table exists, drop it, recreate it, and insert data.
        append: If table exists, insert data. Create if does not exist.

    """   
    
    
    
    conn.close()    
    
def select_rows():
    conn = create_connection(db_file)
    c = conn.cursor()
    qry = """SELECT * FROM data LIMIT 10 ; """
    
    rsl = c.execute(qry, {})
    for r in rsl:
        print (r)
    
    c.close()
    conn.close()    