# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:34:40 2018; @author: mh70
"""
import pandas as pd
import pyodbc 
from sqlalchemy import create_engine
import urllib


f_name = r"C:\Users\m.houska\Downloads\KGZ_customercodes_all.xlsx"
s_name = "data"
t_name = "data" # jméno tabulky (bez dbo. )


# DB   collation jsem nastavil na Cyrillic_General_CI_AS 
conn_str = (r'DRIVER={ODBC Driver 13 for SQL Server};'
            r'SERVER=HOUSKAM\SQLEXPRESS;'
            r'DATABASE=mh;'
            r'Trusted_Connection=yes')  

def write_to_db(df):
    """
    pandas vyžadují pro MS SQL 
    sqlalchemy > create_engine, nefunguje to s conn = create_connection_mssql() 
    
    z dokumentace:
    DataFrame.to_sql(name, con, flavor=None, schema=None, if_exists='fail', 
    index=True, index_label=None, chunksize=None, dtype=None)
    con  SQLAlchemy engine or DBAPI2 connection (legacy mode)
    Using SQLAlchemy makes it possible to use any DB supported by that library. 
    If a DBAPI2 object, only sqlite3 is supported.
    
    řešení ukradeno na:
    https://stackoverflow.com/questions/47402225/python-sqlalchemy-trying-to-write-pandas-dataframe-to-sql-server-using-to-sql
    """
        
    #params = urllib.parse.quote_plus(r'DRIVER={SQL Server};SERVER=HOUSKAM\SQLEXPRESS;DATABASE=mh;Trusted_Connection=yes')
    params = urllib.parse.quote_plus(conn_str)
    conn_str_quo = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
    engine = create_engine(conn_str_quo)
    # 
    #reload(sys) 
    #sys.setdefaultencoding('utf8')

    print(engine)
    df.to_sql(t_name , engine,  
              index=True, index_label=None, if_exists='replace',)
    
    """
    if_exists : {‘fail’, ‘replace’, ‘append’}, default ‘fail’
    
    fail: If table exists, do nothing.
    replace: If table exists, drop it, recreate it, and insert data.
    append: If table exists, insert data. Create if does not exist.
    """




   
#""" create a database connection to MSSQL """
#conn = pyodbc.connect(
#    r'DRIVER={ODBC Driver 13 for SQL Server};'
#    r'SERVER=HOUSKAM\SQLEXPRESS;'
#    r'DATABASE=mh;'
#    r'Trusted_Connection=yes'
#    )

def select_rows():
    """ test inserted rows """
    conn = pyodbc.connect(conn_str)
    c = conn.cursor()
    qry = """SELECT TOP 10 * FROM data; """
    
    rsl = c.execute(qry)
    for r in rsl:
        print (r)
        
    c.execute("select count(*) from data;")
    r = c.fetchone()
    print ("\n***\nnumber of rows in table: " + str(r))
    
    c.close()
    conn.close()   
    
    
def sample_qry():
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone() 
    while row: 
        print (row[0] )
        row = cursor.fetchone()
    cursor.close()        
    conn.close()

# načti z excelu do pandas dataframe
df = pd.read_excel(f_name, sheet_name=s_name)     

# zapiš do db
write_to_db(df)

# vypiš prvních pár řádků a počet řádků
select_rows()