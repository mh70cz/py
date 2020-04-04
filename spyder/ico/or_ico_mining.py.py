#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 20:49:21 2019

@author: mh70
"""

import requests
#import r_rc_ico
from bs4 import BeautifulSoup  
from time import sleep
import csv
import re

def main():
    
    ico_lst = [
         '25088068',
         '02464411',
         '25894293',
         '28582993',
         '27446123',
         '29321417',
         '25554255',
         '07232365',
         '05308151',
         '04328841',
         '29454964',
         '01573241',
         '18595677',
         '29023670',
         '22767134',
         '25878751',
         '63811430',
         '26325241',
         '01798375',
         '67673210',
         '24160938',
         ]
    
    with open('ico_po.txt', 'w') as f:
        for idx, ico in enumerate(ico_lst):
            #ico = r_rc_ico.r_ico()
            #ico = '24160938'
            print(idx, ico)
            r = make_request(ico)
            rsp = resp_found(r)
            if rsp is not None:
                trade_name, spis_znacka,  den_zapisu, sidlo = response_parse(rsp)
                
                f.write(ico  + "; " +
                        trade_name + "; " +
                        spis_znacka + "; " +
                        den_zapisu + "; " +
                        sidlo + "\n")
            sleep(5)
            


# https://or.justice.cz/ias/ui/rejstrik-$firma?ico=91546931&jenPlatne=PLATNE

def make_request(ico):
    url_1 = "https://or.justice.cz/ias/ui/rejstrik-$firma?ico="
    url_2 = "&jenPlatne=PLATNE"        
    url = url_1 + ico + url_2    
    r = requests.get(url)
    return r

def resp_found(r):
    if r.status_code == 200:
        txt  = r.text
        pns_idx = txt.find("Počet nalezených")
        pns_txt = txt[pns_idx : pns_idx + 50]
        #print(pns_txt)
        span_left_idx = pns_txt.find("<span>")
        span_right_idx = pns_txt.find("</span>")
        n_found = pns_txt[span_left_idx + 6 : span_right_idx]
        print(n_found)
        if int(n_found) == 1:
            return txt
        return None

def response_parse(rsp):
    soup = BeautifulSoup(rsp)
        
    search_results = soup.select("#SearchResults > div.section-c > div > ol > li > div > table")
    td = search_results[0].select("td")
                                 
    trade_name = td[0].text.strip()                          
    spis_znacka = td[2].text.strip()
    den_zapisu = td[3].text.strip()
    sidlo = td[4].text.strip() 
    
    return (trade_name, spis_znacka,  den_zapisu, sidlo)

def file_parse():
    companies = []

    rx_zip = re.compile("\d\d\d\s?\d\d")
    
    with open("ico_po_2019-03-10.txt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            ico = row[0].strip()
            trade_name = row[1].strip()
            spis_znacka = row[2].strip()
            den_zapisu = row[3].strip()
            sidlo = row[4].strip()
            
            sf_idx = spis_znacka.find(" vedená")
            RegistrationSectionFileNo = spis_znacka[:sf_idx]
            RegistrationOfficeName = spis_znacka[sf_idx + 8 :]
            
            HomeAddressCity = ""
            HomeAddressZip = ""
            sidlo_spl = sidlo.split(", ")
            
            
            HomeAddressStreet = sidlo_spl[0]
            
            if len( sidlo_spl) == 2:
                streetcity_raw = sidlo_spl[1]
                zip_raw_match = rx_zip.search(streetcity_raw)
                if zip_raw_match is not None:
                    zip_raw = zip_raw_match.group(0)
                    HomeAddressCity = streetcity_raw.replace(zip_raw, "")
                    HomeAddressZip = zip_raw.replace(" ","")
                    
            if len( sidlo_spl) == 3:
                    a = sidlo_spl[1]
                    b = sidlo_spl[2]
                    zip_raw_match = rx_zip.search(b)
                    if zip_raw_match is not None:
                        zip_raw = zip_raw_match.group(0)
                        b = b.replace(zip_raw, "")
                        b = b.replace("PSČ","")
                        HomeAddressCity = a + " " + b
                        HomeAddressZip = zip_raw.replace(" ","")
    
    
            companies.append((
                    ico, 
                    trade_name,
                    RegistrationSectionFileNo,
                    RegistrationOfficeName,
                    #spis_znacka,  
                    den_zapisu, 
                    sidlo,
                    HomeAddressStreet,
                    HomeAddressCity,
                    HomeAddressZip,
                    ))