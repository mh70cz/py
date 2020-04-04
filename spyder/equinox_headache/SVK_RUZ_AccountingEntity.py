#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 20:39:09 2017

@author: mh70

IČO35804564
DIČ2021557802
IČ DPH SK2021557802 
http://www.registeruz.sk/cruz-public/api/uctovne-jednotky?zmenene-od=2000-01-01&pokracovat-za-id=1&max-zaznamov=100&ico=35804564
http://www.registeruz.sk/cruz-public/api/uctovna-jednotka?id=241588
http://www.registeruz.sk/cruz-public/api/uctovna-zavierka?id=3111647
"""

import requests
#import json

class MyException(Exception):
    pass

"""
35804564  CIS SK
31322832  SLOVNAFT, a.s.. - multiple hit
00190284  Poľnohospodárske družstvo Vajnory - multiple hit
36458147  SANA, výrobné družstvo
34129260  STAVBY, OBCHOD, SLUŽBY s.r.o.
36862126  AGROFERT, a. s., organizačná zložka Agrochémia
44545371  Ján Novák
"""


ico = "35804564" # 


uctove_zaverky = list() #závěrky - základní info
idUctovnychZavierok = list()
idUctovnychVykazov_all = list() # pro všechny závěrky vstup do druhého konektoru

url_base = "http://www.registeruz.sk/cruz-public/api/"
url_uctovne_jednotky_suff =  "uctovne-jednotky?zmenene-od=2000-01-01&pokracovat-za-id=1&max-zaznamov=100"
url_uctovna_jednotka_suff = "uctovna-jednotka?"
url_uctovna_zavierka_suff =  "uctovna-zavierka?"
url_uctovne_jednotky = url_base + url_uctovne_jednotky_suff + "&ico=" + ico

try:
    response1 = requests.get(url_uctovne_jednotky)
    if not response1.status_code == 200:
        raise MyException("some problem with response1")
    
    ids = response1.json()['id']
    
    if  len(ids) > 1:
        raise MyException("multiple hit")
    uj_id = str(ids[0]) # id účtovné jednotky
    
    url_uctovna_jednotka = url_base + url_uctovna_jednotka_suff + "id=" + uj_id
    
    response2 = requests.get(url_uctovna_jednotka)
    if not response2.status_code == 200:
        raise MyException("some problem with response2")

    try:            
        idUctovnychZavierok = response2.json()['idUctovnychZavierok']
    except:
        raise MyException("nejsou ucetni zaverky")

    
    for iuz in idUctovnychZavierok:
        url_uz = url_base + url_uctovna_zavierka_suff + "id=" + str(iuz)
        response3 = requests.get(url_uz)
        if not response3.status_code == 200:
            raise MyException("some problem with response1: " + str(iuz))        
        idUctovnychVykazov = response3.json()['idUctovnychVykazov']
        if len(idUctovnychVykazov) < 1:
            raise MyException("nejsou účetní výkazy pro iuz: " + str(iuz))
        idUctovnychVykazov_all.extend(idUctovnychVykazov)
        uctove_zaverky.append(response1.json())
    
        
except MyException as e:
    print(e)
    pass
except Exception as e:
    #print(e)
    pass