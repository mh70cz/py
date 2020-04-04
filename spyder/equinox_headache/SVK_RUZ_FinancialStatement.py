#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:39:09 2017

@author: mh70


http://www.registeruz.sk/cruz-public/api/uctovny-vykaz?id=5569453
http://www.registeruz.sk/cruz-public/api/sablona?id=699

"""

import requests
import json

class MyException(Exception):
    pass

def append_id_sablon(idSablon, ico = "N/A"):
    fname_sablony_id = "./sablony/sablony_id.txt"
    
    with open(fname_sablony_id, 'a', encoding='utf-8') as outfile:
        for s_id in idSablon:
            outfile.write(str(s_id) + ", " + str(ico) + "\n")


#request do konektoru: 
"""    
idUctovnychVykazov_all = [
        2029652, 1862915, 3254919, 3144726, 3796328, 3796329, 3796330, 4172181,
        4643283, 4817413, 5336261, 5128543, 5569453
        ]
"""
#uctove_zaverky = list() #závěrky - základní info - presunuto do 1. "konektoru"
idSablon = list() #šablony pro všechny stažené výkazy
uctove_vykazy = list() #všechy účetní výkazy pro všechny závěrky
sablony = list() #všecny unikátní šabony pro všechny účetní výkazy

url_base = "http://www.registeruz.sk/cruz-public/api/"
url_uctovna_zavierka_suff =  "uctovna-zavierka?"
url_uctovny_vykaz_suff = "uctovny-vykaz?"
url_sablona_suff = "sablona?"

try:    
    if len(idUctovnychVykazov_all) == 0:
        raise MyException("zadne uctove vykazy ")
    for iuv in idUctovnychVykazov_all:
        url_uv = url_base + url_uctovny_vykaz_suff + "id=" + str(iuv)         
        response2 = requests.get(url_uv)
        if not response2.status_code == 200:
            raise MyException("some problem with response2 " + str(iuv))
        uctove_vykazy.append(response2.json())
        idSablony = response2.json()['idSablony']
        idSablon.append(idSablony)
     
    idSablon = list(set(idSablon))    #pouze unikátní id šablon 
    # vrátit jako list, protože spyder nezobrazuje set ve Variable explorer
    for ids in idSablon:
        url_sab = url_base + url_sablona_suff + "id=" + str(ids)         
        response3 = requests.get(url_sab)
        if not response3.status_code == 200:
            raise MyException("some problem with response3 " + str(ids))  
        sablony.append(response3.json())
        
    append_id_sablon(idSablon, ico)
        
except MyException as e:    
    print("Custom ex: " + str(e))
    pass
except Exception as e:
    print(e)
    pass


"""    
 [ uv['idSablony'] for uv in uctove_vykazy ]
    
"""