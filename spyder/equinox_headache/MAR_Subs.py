# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:51:55 2017

@author: mh70
"""

import csv

subs_old = list()
subs_new = list()


filename = r"C:\Users\m.houska\Downloads\SubscriberList2017_10_23_02_41_21.csv"

with open(filename, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     header = next(csvreader)
     for row in csvreader:
         #print(', '.join(row))
         sub_name = row[0]
         sub_id = row[2]
         subs_old.append(sub_id)
         #print(sub_name +"; " + sub_id)
         print("<Subscriber>\n  <SubscriberId>" + sub_id + "</SubscriberId>\n" +
               "  <SubscriberName>" + sub_name + "</SubscriberName>\n</Subscriber>")
         
         
         
src = """
40	CPM
60	CDG
360	UMNIA Bank
361	BMCI NAJMAH
362	BANK ASSAFA
363	DAR AL AMANE 
364	ARREDA
365	AL AKHDAR BANK 
366	BANK AL YOUSR  
367	BTI BANK 
101	BP CENTRE SUD
127	BP FES - TAZA
143	BP LAAYOUNE
145	BP MARRAKECH - BENI MELLAL
148	BP MEKNES
150	BP NADOR - AL HOCEIMA
157	BP OUJDA
164	BP TANGER - TETOUAN
181	BP RABAT - KENITRA
""".strip()



src_lines = src.split('\n')
subs = [sub.split('\t') for sub in src_lines]


for s in subs:
    print("<Subscriber>\n  <SubscriberId>" + s[0] + "</SubscriberId>\n" +
          "  <SubscriberName>" + s[1].strip() + "</SubscriberName>\n</Subscriber>")
    subs_new.append(s[0])
    
    

      