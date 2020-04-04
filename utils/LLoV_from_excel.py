# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:46:15 2017

@author: mh70
"""
import unicodedata
import pandas
df = pandas.read_excel(r'C:\Users\m.houska\Documents\_CIS\MultiConnector\SVK_Justice_Insolvency_Reg.xlsx')

LLoV = dict()    
for idx, k  in enumerate(df["Label"]):
    LLoV[k] = {"cs-CZ": df["cs-CZ"][idx],
               "sk-SK": df["sk-SK"][idx],
               "en-US": df["en-US"][idx]
        }

######### wrk  ######
svk_list = [
        'Dátum podania návrhu na vyhlásenie konkurzu',
        'Dátum začatia konkurzného konania',
        'Dátum prerušenia konkurzného konania',
        'Dátum vyhlásenia konkurzu',
        'Dátum zastavenia konkurzného konania',
        'Dátum podania návrhu na povolenie reštrukturalizácie',
        'Dátum začatia reštrukturalizačného konania',
        'Dátum prerušenia reštrukturalizačného konania',
        'Dátum povolenia reštrukturalizácie',
        'Dátum skončenia reštrukturalizácie',
        'Dátum podania',
        'Dátum začatia procesu',
        'Dátum ukončenia',
        'Dátum podania návrhu na určenie SK',
        'Dátum poskytnutia ochrany pred veriteľmi',
        'Dátum ukončenia konania',
        'Dátum začatia konania',
        'Dátum prerušenia konania'
        ]

svk_labels = list()

for s in svk_list:

    # change unicode to ascii 
    s = ''.join((c for c in unicodedata.normalize('NFD', s)if unicodedata.category(c) != 'Mn'))
    s = s.title()
    s_lst = s.split(" ")
    s1 = ""
    for x in s_lst:
        if len(x) > 3:
            x = x[:3]
        s1 = str(s1) + str(x)
    #s = s.replace(" ", "")
    svk_labels.append(s1)
    
svk_dict = dict()
for idx, q in enumerate(svk_list):
    svk_dict[q] = svk_labels[idx]
    

    