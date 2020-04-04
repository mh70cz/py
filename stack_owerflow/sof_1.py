#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 22:58:26 2018; @author: mh70
reply to
https://stackoverflow.com/questions/49638244/python-sqlite3-printing-result-of-two-combined-tables-makes-problems/49639532#49639532
"""

import sqlite3

def create_tables():
    conn = sqlite3.connect("Alchemy_Data_Bank.dat")
    c = conn.cursor()
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS recipie(id, name, iid_1, iid_2, iid_3);
    """)
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS ingredient(id, name);
    """)
    conn.commit()
    c.close()
    conn.close()
    

def insert_records():
    conn = sqlite3.connect ("Alchemy_Data_Bank.dat")
    c = conn.cursor()
    idata=[(0,"Salami"),
           (1,"Pasta"),
           (2,"Oil"),
           (3,"Olive"),
           (4,"Funghi"),           
           ]
    
    rdata=[(0,"Recipie1",0,1,1),
           (1,"Recipie2",4,1,3),
           (2,"Recipie3",2,1,1),
           (3,"Recipie4",3,4,1),
           (4,"Recipie5",1,2,3),
    ]
        
    c.executemany("insert into recipie(id, name, iid_1, iid_2, iid_3) values (?,?,?,?,?)", rdata)
    c.executemany("insert into ingredient(id, name) values (?,?)", idata)
    conn.commit()
    c.close()
    conn.close()

def select_all_rows():
    conn = sqlite3.connect ("Alchemy_Data_Bank.dat")
    c = conn.cursor()
    qry1 = """select name,  
        (select name from ingredient where ingredient.id = recipie.iid_1), 
        (select name from ingredient where ingredient.id = recipie.iid_2), 
        (select name from ingredient where ingredient.id = recipie.iid_3)
        from recipie;"""
    
    rsl = c.execute(qry1)
    for r in rsl:
        print (r)
    
    c.close()
    conn.close()
    
def select_rows(rec_names):
    conn = sqlite3.connect ("Alchemy_Data_Bank.dat")
    c = conn.cursor()
    qry2 = """select name,  
        (select name from ingredient where ingredient.id = recipie.iid_1), 
        (select name from ingredient where ingredient.id = recipie.iid_2), 
        (select name from ingredient where ingredient.id = recipie.iid_3)
        from recipie
        where name = ?;"""
    
    for rec_name in rec_names:
        #a single member tupple requires a trailing comma
        rsl = c.execute(qry2, (rec_name,)) 
        for r in rsl:
            print (r)
    
    c.close()
    conn.close()   
    
def select_rows_fetch(rec_names):
    conn = sqlite3.connect ("Alchemy_Data_Bank.dat")
    c = conn.cursor()
    qry2 = """select name,  
        (select name from ingredient where ingredient.id = recipie.iid_1), 
        (select name from ingredient where ingredient.id = recipie.iid_2), 
        (select name from ingredient where ingredient.id = recipie.iid_3)
        from recipie
        where name = :r_name;"""
    
    for rec_name in rec_names:
        c.execute(qry2, {"r_name": rec_name}) 
        r = c.fetchone()
        print (r)
    
    c.close()
    conn.close()  
    
def select_rows_where_in(rec_names):
    conn = sqlite3.connect ("Alchemy_Data_Bank.dat")
    c = conn.cursor()
    qry_part = """select name,  
        (select name from ingredient where ingredient.id = recipie.iid_1), 
        (select name from ingredient where ingredient.id = recipie.iid_2), 
        (select name from ingredient where ingredient.id = recipie.iid_3)
        from recipie
        where name in """
    rec_names_str = ', '.join("'{0}'".format(w) for w in rec_names) 
    qry = qry_part + "(" + rec_names_str + ") ;"
    c.execute(qry) 
    for r in c.fetchall():
        print (r)
    
    c.close()
    conn.close()      
    
#create_tables() #run once
#insert_records() #run once

print("all rows: " )
select_all_rows()
print('****')

print ("\nselected rows in the argument:")
select_rows(("Recipie3", "Recipie4"))

print ("\nselected row in the argument:"
       "\n(note that a single member tupple requires a trailing comma)")
select_rows(("Recipie3",))


print('****')
rec_names = ("Recipie1", "Recipie2")
rec_name = ("Recipie3", ) #a single member tupple requires a trailing comma
print("\nselected rows " + str(rec_names) + " : ")
select_rows(rec_names)
print("\nselected row " + str(rec_name) + " : ")
select_rows(rec_name)


print('\n1. alternative method  select_rows_fetch(rec_names) ')
print("\nselected rows " + str(rec_names) + " : ")
select_rows_fetch(rec_names)
print("\nselected row " + str(rec_name) + " : ")
select_rows_fetch(rec_name)


print('\n2. alternative method   select_rows_where_in(rec_names)')
print("\nselected rows" + str(rec_names) + " : ")
select_rows_where_in(rec_names)
print("\nselected row" + str(rec_name) + " : ")
select_rows_where_in(rec_name)
 




        
        
        